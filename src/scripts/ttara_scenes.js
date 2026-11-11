const S_INK = 'stroke="#17130f" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"';
const svg = (bg, body) => `<svg viewBox="0 0 400 190" preserveAspectRatio="xMidYMax slice" xmlns="http://www.w3.org/2000/svg"><rect width="400" height="190" fill="${bg}"/>${body}</svg>`;
const hats = {
  bucket: (c) => `<path d="M-33 66c2-36 64-36 66 0z" fill="${c}" ${S_INK}/><path d="M-50 70c0-9 100-9 100 0 2 7-102 7-100 0z" fill="${c}" ${S_INK}/>`,
  beanie: (c) => `<path d="M-37 74c-4-54 78-54 74 0z" fill="${c}" ${S_INK}/><rect x="-41" y="62" width="82" height="17" rx="8" fill="#fffdf7" ${S_INK}/>`,
  hair: (c) => `<path d="M-38 84c-7-58 83-58 76 0-12-22-62-22-76 0z" fill="${c}" ${S_INK}/>`,
  bun: (c) => `<circle cy="36" r="13" fill="${c}" ${S_INK}/><path d="M-38 84c-7-58 83-58 76 0-12-22-62-22-76 0z" fill="${c}" ${S_INK}/>`,
};
const camper = (x, shirt, skin, hat, hatColor, s = 1) => `<g transform="translate(${x} ${190 - 190 * s}) scale(${s})"><g class="bob"><path d="M-60 194c0-46 27-66 60-66s60 20 60 66z" fill="${shirt}" ${S_INK}/><rect x="-13" y="106" width="26" height="29" fill="${skin}" ${S_INK}/><circle cy="84" r="37" fill="${skin}" ${S_INK}/>${hats[hat](hatColor)}</g></g>`;
const waves = (x, y, flip = 1) => `<g class="waves" transform="translate(${x} ${y}) scale(${flip} 1)"><path d="M0-14c9 8 9 20 0 28"/><path d="M15-25c16 14 16 36 0 50"/><path d="M30-36c23 20 23 52 0 72"/></g>`;
const bubble = (x, y, text, fill = "#fffdf7") => `<g transform="translate(${x} ${y})"><path d="M-46-24h92a10 10 0 0 1 10 10v26a10 10 0 0 1-10 10h-66l-16 16 2-16h-12a10 10 0 0 1-10-10v-26a10 10 0 0 1 10-10z" fill="${fill}" ${S_INK}/><text y="7" text-anchor="middle" font-family="Bricolage Grotesque, Segoe UI, sans-serif" font-weight="800" font-size="24" fill="#17130f">${text}</text></g>`;
const burst = (cx, cy, R, r, n, fill) => {
  let d = "";
  for (let i = 0; i < n * 2; i++) {
    const a = Math.PI * i / n - Math.PI / 2, k = i % 2 ? r : R;
    d += (i ? "L" : "M") + (cx + k * Math.cos(a)).toFixed(1) + " " + (cy + k * Math.sin(a)).toFixed(1);
  }
  return `<path d="${d}z" fill="${fill}" ${S_INK}/>`;
};
const BIG_TEXT = 'text-anchor="middle" font-family="Bricolage Grotesque, Segoe UI, sans-serif" font-weight="800" fill="#17130f"';

const SCENES = {
  family: { paper: "#fbeedd", art: () => svg("#ffa94d", `
    <rect x="150" y="14" width="100" height="60" rx="5" fill="#fffdf7" ${S_INK}/><path d="M162 64l24-26 16 16 12-10 24 20z" fill="#12a58c" ${S_INK}/><circle cx="230" cy="32" r="7" fill="#ffce3a" ${S_INK}/>
    ${camper(80, "#2b62f6", "#f1c6a2", "hair", "#4a2c17", .8)}${camper(320, "#12a58c", "#d9a06f", "beanie", "#ff5c8a", .8)}${camper(200, "#ff5c8a", "#e7b48c", "bun", "#2b1a10", .58)}
    <rect x="-6" y="150" width="412" height="46" fill="#7a4221" ${S_INK}/>
    <path d="M106 136h40a20 14 0 0 1-40 0z" fill="#fffdf7" ${S_INK}/><path d="M254 136h40a20 14 0 0 1-40 0z" fill="#fffdf7" ${S_INK}/>
    ${waves(134, 88)}`) },
  react: { paper: "#fbe3e0", art: () => svg("#ff6b5c", `
    <rect x="0" y="164" width="400" height="28" fill="#ffce3a" ${S_INK}/>
    ${burst(300, 78, 66, 48, 12, "#fffdf7")}<text x="300" y="88" ${BIG_TEXT} font-size="25">WOW!</text>
    <path d="M30 28l10 46h10l10-46z" fill="#fffdf7" ${S_INK}/><circle cx="45" cy="90" r="7" fill="#fffdf7" ${S_INK}/>
    ${camper(120, "#2b62f6", "#f1c6a2", "bucket", "#ffce3a", .92)}${waves(178, 100)}`) },
  story: { paper: "#e4e0f4", art: () => svg("#3b2a6e", `
    <path d="M352 22a24 24 0 1 0 14 40 20 20 0 1 1-14-40z" fill="#fff3c4" ${S_INK}/>
    <g fill="#fff3c4"><circle class="twinkle" cx="60" cy="34" r="4"/><circle cx="250" cy="24" r="3"/><circle class="twinkle" cx="300" cy="66" r="4"/><circle cx="28" cy="96" r="3"/></g>
    <rect x="0" y="164" width="400" height="28" fill="#2f7d52" ${S_INK}/>
    <circle cx="310" cy="126" r="36" fill="#ffce3a" opacity=".3"/><path d="M298 104a12 12 0 0 1 24 0" fill="none" ${S_INK}/><rect x="298" y="106" width="24" height="34" rx="5" fill="#ffce3a" ${S_INK}/><rect x="292" y="140" width="36" height="12" rx="3" fill="#7a4221" ${S_INK}/>
    ${camper(150, "#ff5c8a", "#e7b48c", "bun", "#2b1a10", .82)}
    <path d="M96 140 150 150v36l-54-10z" fill="#fffdf7" ${S_INK}/><path d="M204 140 150 150v36l54-10z" fill="#fffdf7" ${S_INK}/>
    <g fill="#ffce3a"><circle class="twinkle" cx="86" cy="124" r="4"/><circle class="twinkle" cx="220" cy="136" r="3.5"/></g>
    ${waves(214, 90)}`) },
  gear: { paper: "#f1e6d8", art: () => svg("#c98b4f", `
    <rect x="0" y="176" width="400" height="16" fill="#2f7d52" ${S_INK}/>
    <path d="M182 140v50M374 140v50" fill="none" ${S_INK}/><rect x="164" y="128" width="230" height="14" fill="#7a4221" ${S_INK}/>
    <circle cx="222" cy="100" r="30" fill="#fff3c4" opacity=".45"/><path d="M210 72a12 12 0 0 1 24 0" fill="none" ${S_INK}/><rect x="206" y="72" width="32" height="10" rx="3" fill="#17130f"/>
    <rect x="210" y="82" width="24" height="34" rx="4" fill="#ffce3a" ${S_INK}/><rect x="204" y="116" width="36" height="12" rx="3" fill="#2f7d52" ${S_INK}/>
    <rect x="258" y="106" width="22" height="22" rx="3" fill="#fffdf7" ${S_INK}/>
    <path d="M310 66v-10a13 13 0 0 1 26 0v10" fill="none" ${S_INK}/><rect x="292" y="66" width="62" height="62" rx="16" fill="#ff7a2b" ${S_INK}/><rect x="304" y="96" width="38" height="24" rx="6" fill="#ffce3a" ${S_INK}/>
    ${camper(92, "#ffce3a", "#d9a06f", "beanie", "#2b62f6", .9)}${waves(150, 84)}`) },
  daily: { paper: "#ece6dc", art: () => svg("#ff7a2b", `
    <rect x="232" y="24" width="126" height="98" rx="6" fill="#bfe4ff" ${S_INK}/><circle cx="330" cy="58" r="17" fill="#ffce3a" ${S_INK}/><path d="M295 26v94M234 73h122" fill="none" ${S_INK}/>
    <path d="M118 0v22" fill="none" ${S_INK}/><path d="M92 46c0-32 52-32 52 0z" fill="#ffce3a" ${S_INK}/>
    <rect x="0" y="162" width="400" height="30" fill="#7a4221" ${S_INK}/>
    <path d="M286 138h40v22a10 10 0 0 1-10 10h-20a10 10 0 0 1-10-10z" fill="#fffdf7" ${S_INK}/><path d="M326 144c18-3 18 18 0 16" fill="none" ${S_INK}/>
    ${camper(112, "#2b62f6", "#f1c6a2", "hair", "#4a2c17", .94)}${waves(178, 92)}`) },
  camp: { paper: "#e2e8f6", art: () => svg("#2854d8", `
    <circle cx="330" cy="44" r="24" fill="#fff3c4" ${S_INK}/>
    <g fill="#fff3c4"><circle class="twinkle" cx="52" cy="30" r="4"/><circle cx="130" cy="20" r="3"/><circle class="twinkle" cx="238" cy="36" r="4"/><circle cx="282" cy="16" r="3"/></g>
    <path d="M-10 134 76 54l58 56 42-36 92 76z" fill="#17388f" ${S_INK}/>
    <rect x="0" y="146" width="400" height="46" fill="#2f7d52" ${S_INK}/>
    <path d="M198 158 262 66l64 92z" fill="#ffce3a" ${S_INK}/><path d="M262 66v92M246 158l16-40 16 40z" fill="#ff7a2b" ${S_INK}/>
    <g transform="translate(160 164)"><path class="flame" d="M0-42c16 16 20 26 12 38H-12C-20-16-14-26 0-42z" fill="#ff7a2b" ${S_INK}/><path d="M-22 2 22-6M-22-6 22 2" fill="none" stroke="#7a4221" stroke-width="9" stroke-linecap="round"/></g>
    ${camper(70, "#ff5c8a", "#e7b48c", "bucket", "#e8dcae", .78)}${waves(120, 118)}`) },
  edit: { paper: "#f7e4ec", art: () => svg("#ffce3a", `
    <rect x="142" y="18" width="232" height="132" rx="10" fill="#fffdf7" ${S_INK}/>
    <rect x="160" y="34" width="196" height="62" rx="5" fill="#2b62f6" ${S_INK}/><path d="M246 50v30l26-15z" fill="#ffce3a" ${S_INK}/>
    <rect x="160" y="108" width="62" height="13" rx="4" fill="#ff5c8a"/><rect x="226" y="108" width="84" height="13" rx="4" fill="#12a58c"/><rect x="314" y="108" width="42" height="13" rx="4" fill="#ff7a2b"/>
    <rect x="160" y="126" width="118" height="10" rx="4" fill="#b7aa95"/><rect x="284" y="126" width="72" height="10" rx="4" fill="#b7aa95"/>
    <rect class="head" x="178" y="102" width="4" height="40" fill="#17130f"/>
    <rect x="236" y="150" width="44" height="26" fill="#d9cdb9" ${S_INK}/><rect x="0" y="174" width="400" height="18" fill="#17130f"/>
    ${camper(72, "#12a58c", "#d9a06f", "beanie", "#ff5c8a", .9)}${waves(136, 86)}`) },
  yt: { paper: "#f7e6d8", art: () => svg("#ff6fa3", `
    <rect x="0" y="160" width="400" height="32" fill="#fff3c4" ${S_INK}/>
    <path d="M300 112 266 176M300 112v64M300 112l34 64" fill="none" ${S_INK}/>
    <rect x="256" y="58" width="88" height="58" rx="9" fill="#17130f"/><circle cx="300" cy="87" r="20" fill="#2b62f6" stroke="#fffdf7" stroke-width="5"/><circle cx="330" cy="70" r="5" fill="#ff3b30"/>
    <path transform="translate(42 44)" d="M0 26C-30 6-18-14 0-2 18-14 30 6 0 26z" fill="#fffdf7" ${S_INK}/><path transform="translate(190 34) scale(.68)" d="M0 26C-30 6-18-14 0-2 18-14 30 6 0 26z" fill="#ffce3a" ${S_INK}/>
    ${camper(120, "#ffce3a", "#f1c6a2", "bucket", "#2f7d52", .9)}<path d="M190 164c20-14 26-34 28-52" fill="none" stroke="#17130f" stroke-width="20" stroke-linecap="round"/><path d="M190 164c20-14 26-34 28-52" fill="none" stroke="#ffce3a" stroke-width="10" stroke-linecap="round"/><circle cx="219" cy="102" r="13" fill="#f1c6a2" ${S_INK}/>${waves(226, 66)}`) },
  travel: { paper: "#dcf0f7", art: () => svg("#5cc8f2", `
    <circle cx="44" cy="40" r="20" fill="#ffce3a" ${S_INK}/>
    <path d="M196 62c-4-20 26-26 32-10 12-12 34-2 28 12 14 4 10 20-4 20h-52c-16 0-18-20-4-22z" fill="#fffdf7" ${S_INK}/>
    <g transform="translate(332 36) rotate(-9) scale(.8)"><path d="M-42-8-58-32h17l18 24z" fill="#ff5c8a" ${S_INK}/><rect x="-54" y="-13" width="110" height="26" rx="13" fill="#fffdf7" ${S_INK}/><path d="M-8 5-34 38h20L24 5z" fill="#ffce3a" ${S_INK}/><g fill="#2b62f6"><circle cx="-24" cy="-3" r="3.5"/><circle cx="-8" cy="-3" r="3.5"/><circle cx="8" cy="-3" r="3.5"/><circle cx="24" cy="-3" r="3.5"/></g></g>
    <rect x="0" y="166" width="400" height="26" fill="#f4dfae" ${S_INK}/>
    <path d="M286 106V88a8 8 0 0 1 8-8h24a8 8 0 0 1 8 8v18" fill="none" ${S_INK}/>
    <rect x="262" y="104" width="88" height="62" rx="10" fill="#ff7a2b" ${S_INK}/><path d="M284 106v58M328 106v58" fill="none" ${S_INK}/>
    <circle cx="306" cy="134" r="11" fill="#ffce3a" ${S_INK}/>
    ${camper(112, "#12a58c", "#f1c6a2", "bucket", "#ff5c8a", .9)}${waves(178, 96)}`) },
  news: { paper: "#dff1ec", art: () => svg("#12a58c", `
    <rect x="228" y="20" width="146" height="82" rx="8" fill="#17130f"/><text x="301" y="72" text-anchor="middle" font-family="Bricolage Grotesque, Segoe UI, sans-serif" font-weight="800" font-size="38" fill="#ffce3a">NEWS</text><circle cx="248" cy="38" r="7" fill="#ff3b30"/>
    ${camper(112, "#17388f", "#e7b48c", "hair", "#2b1a10", .96)}<path d="M112 128l-10 16 10 38 10-38z" fill="#ff5c8a" ${S_INK}/>
    <rect x="-6" y="154" width="412" height="42" fill="#fffdf7" ${S_INK}/><rect x="0" y="168" width="400" height="10" fill="#ff5c8a"/>
    <rect x="220" y="124" width="92" height="30" rx="3" fill="#fff3c4" ${S_INK}/>${waves(178, 92)}`) },
  speech: { paper: "#e9e2fa", art: () => svg("#7450f0", `
    <path d="M150-10h100l50 210H100z" fill="#ffe99a" opacity=".55"/>
    <path d="M-5-5h96c-4 74-30 144-96 200z" fill="#e23d5b" ${S_INK}/><path d="M405-5H309c4 74 30 144 96 200z" fill="#e23d5b" ${S_INK}/>
    ${camper(200, "#fffdf7", "#d9a06f", "bun", "#17130f", .84)}
    <path d="M154 134h92l-12 62h-68z" fill="#ffce3a" ${S_INK}/><path d="M150 124h100l4 14H146z" fill="#7a4221" ${S_INK}/><circle cx="200" cy="164" r="11" fill="#fffdf7" ${S_INK}/>
    ${waves(258, 88)}`) },
  talk: { paper: "#eef3d4", art: () => svg("#a8d63f", `
    <rect x="0" y="162" width="400" height="30" fill="#2f7d52" ${S_INK}/>
    ${bubble(132, 40, "Hi!")}${bubble(278, 42, "Hey!", "#ffce3a")}
    ${camper(104, "#2b62f6", "#f1c6a2", "bucket", "#ff7a2b", .82)}${camper(296, "#ff5c8a", "#a86f46", "hair", "#17130f", .82)}${waves(176, 122)}`) },
};
const REPEAT_SCENE = { 가족: "family", 리액션: "react", 일상: "daily", 여행: "travel", 캠핑: "camp", 편집: "edit", 유튜브: "yt" };
const LISTEN_SCENE = { 여행: "travel", 이야기: "story", 장비: "gear", 뉴스: "news", 연설: "speech", 대화: "talk" };
const STICKER = { listen: "잘 들어 봐요", turn: "이제 따라 해요!" };

function putScene(el, key) {
  if (el.dataset.key === key) return;
  el.dataset.key = key;
  el.innerHTML = SCENES[key].art();
}
function paintRepeat() {
  const key = REPEAT_SCENE[current().cat];
  putScene($("scene"), key);
  $("tag").textContent = current().cat + " 표현";
  if (state.mode === "repeat") document.documentElement.style.setProperty("--paper", SCENES[key].paper);
}
function paintListen() {
  const key = LISTEN_SCENE[currentListen().cat];
  putScene($("lscene"), key);
  $("lstage").classList.toggle("compact", revealed);
  if (state.mode === "listen") document.documentElement.style.setProperty("--paper", SCENES[key].paper);
}
function setStage(phase) {
  for (const [stage, sticker] of [["stage", "sticker"], ["lstage", "lsticker"]]) {
    $(stage).dataset.phase = phase;
    $(sticker).hidden = phase === "idle";
    $(sticker).textContent = STICKER[phase] || "";
  }
}

let wordSpans = [];
function paintWords(text) {
  let pos = 0;
  const box = $("en");
  box.replaceChildren();
  wordSpans = text.split(" ").map((w) => {
    const s = document.createElement("span");
    s.className = "w";
    s.textContent = w + " ";
    s.dataset.start = pos;
    pos += w.length + 1;
    box.appendChild(s);
    return s;
  });
}
function markChar(ci) {
  let cur = 0;
  wordSpans.forEach((s, i) => { if (+s.dataset.start <= ci) cur = i; });
  wordSpans.forEach((s, i) => { s.className = "w " + (i < cur ? "past" : i === cur ? "cur" : "todo"); });
}
function clearWords() { wordSpans.forEach((s) => { s.className = "w"; }); }
// Many Android voices never report word positions, so a timed sweep drives the highlight until one arrives.
async function sweep(len, ms, id, over) {
  const t0 = performance.now();
  while (live(id) && !over()) {
    const p = (performance.now() - t0) / ms;
    if (p < 1) markChar(p * len);
    await sleep(50, id);
  }
}
