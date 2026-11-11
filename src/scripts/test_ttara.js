// Runs the app's real script against a small fake DOM and speech engine. Usage: node test_ttara.js <page.html>
const fs = require('fs');
const vm = require('vm');
const html = fs.readFileSync(process.argv[2], 'utf8');
const code = html.slice(html.lastIndexOf('<script>') + 8, html.lastIndexOf('</script>'));

class El {
  constructor() {
    this.children = []; this.dataset = {}; this.style = {}; this.attrs = {}; this.handlers = {};
    this.textContent = ''; this.hidden = false; this.className = '';
    const self = this; const set = new Set();
    this.classList = { toggle(c, on) { on ? set.add(c) : set.delete(c); }, has: (c) => set.has(c) };
    this.self = self;
  }
  appendChild(c) { this.children.push(c); return c; }
  append(...c) { this.children.push(...c); }
  replaceChildren() { this.children = []; }
  setAttribute(k, v) { this.attrs[k] = v; }
  addEventListener(k, f) { this.handlers[k] = f; }
  click() { this.handlers.click(); }
}
const els = {};
const document = {
  getElementById: (id) => (els[id] = els[id] || new El()),
  createElement: () => new El(),
  addEventListener() {},
  hidden: false,
  documentElement: { style: { setProperty() {} } },
};
const spoken = [];
const speechSynthesis = {
  getVoices: () => [{ lang: 'en-US', name: 'Google US English' }, { lang: 'en-US', name: 'Other' }],
  addEventListener() {}, resume() {}, cancel() {},
  speak(u) { spoken.push({ text: u.text, pitch: u.pitch }); setTimeout(() => u.onstart(), 1); setTimeout(() => u.onend(), 25); },
};
const sandbox = {
  document, speechSynthesis, performance, setTimeout, clearTimeout, console,
  navigator: {}, localStorage: { getItem: () => null, setItem() {} },
  SpeechSynthesisUtterance: function (t) { this.text = t; },
};
sandbox.window = sandbox;
vm.createContext(sandbox);
vm.runInContext(code, sandbox);

const $ = (id) => els[id];
const wait = (ms) => new Promise((r) => setTimeout(r, ms));
const check = (name, ok, extra = '') => { console.log((ok ? 'PASS ' : 'FAIL ') + name, extra); if (!ok) process.exitCode = 1; };

(async () => {
  check('hidden attribute wins over display rules', /\[hidden\]\s*\{\s*display:\s*none\s*!important/.test(html));
  check('new sentences come first', /const SENTENCES = \[\s*\n  \["가족", "Good morning! Did you sleep well\?"/.test(html));
  check('new listening comes first', /const LISTENS = \[\s*\n  \{ cat: "여행", title: "Boarding Announcement"/.test(html));
  const missing = vm.runInContext('[...CATS.slice(1).filter((c) => !SCENES[REPEAT_SCENE[c]]), ...LCATS.slice(1).filter((c) => !SCENES[LISTEN_SCENE[c]])]', sandbox);
  check('every topic has a picture', missing.length === 0, missing.join(','));
  check('starts on 1/86', $('count').textContent === '1 / 86', $('count').textContent);
  $('play').click();
  await wait(16500);
  const first = spoken.filter((s) => s.text === 'Good morning! Did you sleep well?').length;
  check('sentence read 3 times', first === 3, 'times=' + first);
  check('advanced to sentence 2', $('count').textContent === '2 / 86', $('count').textContent);
  $('play').click();
  check('stop returns to idle', $('play').textContent === '시작');
  $('next').click();
  check('next moves on', $('count').textContent === '3 / 86', $('count').textContent);

  $('cats').children[4].click();
  check('travel category', $('count').textContent === '1 / 24' && $('tag').textContent === '여행 표현', $('count').textContent + ' ' + $('tag').textContent);
  check('new travel sentence first', $('en').children.map((w) => w.textContent).join('').trim() === 'A table for three, please.');

  spoken.length = 0;
  $('modeListen').click();
  check('listen view shows', $('listenView').hidden === false && $('repeatView').hidden === true);
  check('text hidden first', $('lscript').hidden === true);
  $('lcats').children[6].click();
  check('dialogue category', $('lkind').textContent === '대화', $('lkind').textContent);
  $('lplay').click();
  await wait(9000);
  check('all three passes read', spoken.length === 18, 'lines=' + spoken.length);
  check('speakers have different pitch', spoken[0].pitch === 0.92 && spoken[1].pitch === 1.18);
  check('text revealed after 2 listens', $('lscript').hidden === false && $('lans').hidden === false, $('lans').textContent);
  check('listen finished idle', $('lplay').textContent === '시작', $('lcue').textContent);
  spoken.length = 0;
  $('lscript').children[4].click();
  await wait(400);
  check('tap line replays it', spoken.length === 1 && spoken[0].text === 'Is there hot water?', spoken[0] && spoken[0].text);
  $('lnext').click();
  check('next hides text', $('lscript').hidden === true && $('lcount').textContent === '2 / 4', $('lcount').textContent);
  process.exit(process.exitCode || 0);
})().catch((e) => { console.error(e); process.exit(1); });
