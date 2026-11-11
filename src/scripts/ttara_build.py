"""Rebuild ttara.html: new look and content around the original data and logic. Usage: ttara_build.py <src_dir>"""
import json
import pathlib
import shutil
import sys

base = sys.argv[1]
page = f"{base}/ttara.html"
source = f"{base}/ttara_v2.html"
try:
    open(source, encoding="utf-8").close()
except FileNotFoundError:
    shutil.copy(page, source)  # Keep the functional version so reruns patch the same input.

old = open(source, encoding="utf-8").read()
script = old[old.rindex("<script>") + 8 : old.rindex("</script>")]
head = open(f"{base}/scripts/ttara_head.html", encoding="utf-8").read()
scenes = open(f"{base}/scripts/ttara_scenes.js", encoding="utf-8").read()

TRAVEL = [
    ("Where is the check-in counter?", "체크인 카운터가 어디에 있나요?"),
    ("Can I have an aisle seat, please?", "통로 쪽 좌석으로 주실 수 있나요?"),
    ("My bag didn't arrive.", "제 가방이 도착하지 않았어요."),
    ("How do I get to the city center?", "시내 중심가까지 어떻게 가나요?"),
    ("Does this bus go to the airport?", "이 버스 공항에 가나요?"),
    ("Could you take me to this address?", "이 주소로 가 주시겠어요?"),
    ("Is it within walking distance?", "걸어갈 수 있는 거리인가요?"),
    ("I have a reservation for two nights.", "2박 예약했어요."),
    ("Can I leave my luggage here?", "여기에 짐을 맡겨도 될까요?"),
    ("What time is checkout?", "체크아웃은 몇 시인가요?"),
    ("The Wi-Fi isn't working in my room.", "제 방 와이파이가 안 돼요."),
    ("What's the most popular dish here?", "여기서 제일 인기 있는 메뉴가 뭐예요?"),
    ("Can I get the check, please?", "계산서 주시겠어요?"),
    ("Do you take credit cards?", "신용카드 받으시나요?"),
    ("Could you take a picture of us?", "저희 사진 좀 찍어 주시겠어요?"),
    ("I lost my passport.", "여권을 잃어버렸어요."),
]
for en, _ in TRAVEL:
    assert f'"{en}"' not in script, en
travel_rows = "".join(f'\n  ["여행", "{en}", "{ko}"],' for en, ko in TRAVEL)

# Travel sits right after the daily sentences, so it follows 일상 in the 전체 list too.
last_daily = [l for l in script.split("\n") if l.startswith('  ["일상"')][-1]

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import ttara_content as C  # noqa: E402

js = lambda v: json.dumps(v, ensure_ascii=False)  # noqa: E731
known_en = [en for en, _ in TRAVEL]
for cat, en, _ in C.NEW_SENTENCES:
    assert f'"{en}"' not in script and en not in known_en, en
    assert cat in C.CATS, cat
    known_en.append(en)
new_rows = "".join(f"\n  [{js(cat)}, {js(en)}, {js(ko)}]," for cat, en, ko in C.NEW_SENTENCES)


def listen_js(item):
    cat, title, q, a, lines = item
    assert cat in C.LCATS, cat
    rows = "".join(f"\n    n({js(en)}, {js(ko)})," if not who else f"\n    [{js(who)}, {js(en)}, {js(ko)}]," for who, en, ko in lines)
    return f"\n  {{ cat: {js(cat)}, title: {js(title)}, q: {js(q)}, a: {js(a)}, lines: [{rows}\n  ] }},"


new_listens = "".join(listen_js(item) for item in C.NEW_LISTENS)
reset = (f"\n// New material sits at the front; send everyone back to item 1 once when it arrives.\nconst CONTENT = {C.CONTENT_VERSION};\n"
         "if (state.content !== CONTENT) { state.index = 0; state.lIndex = 0; state.content = CONTENT; }")
show_pressed = lambda box: f'\n  $("{box}").querySelector?.(\'[aria-pressed="true"]\')?.scrollIntoView?.({{ block: "nearest", inline: "nearest" }});'  # noqa: E731

PATCHES = [
    (last_daily, last_daily + travel_rows),
    ("const SENTENCES = [", "const SENTENCES = [" + new_rows),
    ("const LISTENS = [", "const LISTENS = [" + new_listens),
    ('const CATS = ["전체", "일상", "캠핑", "편집", "유튜브"];', f"const CATS = {js(C.CATS)};"),
    ('const LCATS = ["전체", "뉴스", "연설", "대화"];', f"const LCATS = {js(C.LCATS)};"),
    ('if (!CATS.includes(state.cat)) state.cat = "전체";', 'if (!CATS.includes(state.cat)) state.cat = "전체";' + reset),
    ('  [...$("cats").children].forEach((b) => b.setAttribute("aria-pressed", String(b.dataset.cat === state.cat)));',
     '  [...$("cats").children].forEach((b) => b.setAttribute("aria-pressed", String(b.dataset.cat === state.cat)));' + show_pressed("cats")),
    ('  [...$("lcats").children].forEach((b) => b.setAttribute("aria-pressed", String(b.dataset.cat === state.lCat)));',
     '  [...$("lcats").children].forEach((b) => b.setAttribute("aria-pressed", String(b.dataset.cat === state.lCat)));' + show_pressed("lcats")),
    ('[...$("lscript").children].forEach((el, k) => el.classList.toggle("now", k === i));',
     '[...$("lscript").children].forEach((el, k) => {\n    el.classList.toggle("now", k === i);\n    if (k === i) el.scrollIntoView?.({ block: "nearest", behavior: "smooth" });\n  });'),
    ('const KEY = "ttara-v1";', 'const KEY = "ttara-v1";\n\n' + scenes),
    ('  $("en").textContent = s.en;', "  paintWords(s.en);"),
    ('  p.setAttribute("aria-pressed", String(running));\n  save();', '  p.setAttribute("aria-pressed", String(running));\n  paintRepeat();\n  save();'),
    ('  $("modeListen").setAttribute("aria-pressed", String(state.mode === "listen"));\n  save();', '  $("modeListen").setAttribute("aria-pressed", String(state.mode === "listen"));\n  paintListen();\n  save();'),
    ("    u.onstart = () => { started = performance.now(); };", '    u.onstart = () => { started = performance.now(); opts.onStart?.(); };\n    u.onboundary = (ev) => { if (ev.name === undefined || ev.name === "word") opts.onChar?.(ev.charIndex); };'),
    ("    for (let r = 0; r < REPEATS && live(id); r++) {", "    let known = 0;\n    for (let r = 0; r < REPEATS && live(id); r++) {"),
    ('      setCue("잘 들어 보세요", false);\n      const spoken = await speak(s.en, id);',
     '      setCue("잘 들어 보세요", false);\n      setStage("listen");\n      let heard = false, over = false;\n      const span = known || estimate(s.en);\n      const spoken = await speak(s.en, id, {\n        onChar: (c) => { heard = true; markChar(c); },\n        onStart: () => sweep(s.en.length, span, id, () => over || heard),\n      });\n      over = true;\n      known = spoken || known;\n      clearWords();'),
    ('      setCue("이제 따라 말해 보세요", true);', '      setCue("이제 따라 말해 보세요", true);\n      setStage("turn");'),
    ("  setListenCue(LISTEN_IDLE);\n  renderListen();\n  wake = null;", '  setListenCue(LISTEN_IDLE);\n  setStage("idle");\n  clearWords();\n  renderListen();\n  wake = null;'),
    ('    setListenCue("글자 없이 듣기 " + round + " / 2");', '    setListenCue("글자 없이 듣기 " + round + " / 2");\n    setStage("listen");'),
    ('  setListenCue("글을 보며 듣기");', '  setListenCue("글을 보며 듣기");\n  setStage("listen");'),
]
for before, after in PATCHES:
    assert script.count(before) == 1, (script.count(before), before)
    script = script.replace(before, after)

with open(page, "w", encoding="utf-8", newline="\n") as f:
    f.write(head + "\n<script>" + script + "</script>\n")
print("built", len(head) + len(script), "chars")
