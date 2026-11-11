"""Phone-size screenshots of ttara.html states. Usage: ttara_shots.py <scratchpad> <out.png> [height]"""
import pathlib
import subprocess
import sys
import time

base = pathlib.Path(sys.argv[1])
out = sys.argv[2]
height = int(sys.argv[3]) if len(sys.argv) > 3 else 560
shots = base / "work" / "shots"
shots.mkdir(parents=True, exist_ok=True)
page = (base / "ttara.html").read_text(encoding="utf-8")
SKELETON = '<!doctype html><html><head><meta charset=utf8><meta name=viewport content="width=device-width,initial-scale=1"></head><body style="margin:0">'

STATES = {
    'family': 'document.getElementById("modeRepeat").click();document.getElementById("cats").children[1].click();',
    'react': 'document.getElementById("modeRepeat").click();document.getElementById("cats").children[2].click();',
    'travel_listen': 'document.getElementById("modeListen").click();document.getElementById("lcats").children[1].click();',
    'story': 'document.getElementById("modeListen").click();document.getElementById("lcats").children[2].click();',
    'gear': 'document.getElementById("modeListen").click();document.getElementById("lcats").children[3].click();',
    'story_text': 'document.getElementById("modeListen").click();document.getElementById("lcats").children[2].click();document.getElementById("lshow").click();',
}
# Report anything still clipped straight onto the screenshot.
PROBE = """setTimeout(()=>{const c=[...document.querySelectorAll('.card')].find(e=>e.offsetParent);
const b=document.createElement('div');b.style='position:fixed;left:0;top:0;background:#000;color:#0f0;font:11px monospace;z-index:9;padding:1px 3px';
b.textContent=c.clientHeight+'/'+c.scrollHeight;document.body.append(b);},700);"""
for name, code in STATES.items():
    (shots / f"{name}.html").write_text(SKELETON + page + f"<script>{code}{PROBE}</script></body></html>", encoding="utf-8")

frames = "".join(
    f'<iframe src="{name}.html" width="360" height="{height}" style="border:1px solid #888;margin:4px"></iframe>' for name in STATES
)
wrap = shots / f"wrap{height}.html"
wrap.write_text(f'<!doctype html><body style="margin:0;background:#555;white-space:nowrap">{frames}</body>', encoding="utf-8")

edge = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
out = str(pathlib.Path(out).resolve())
pathlib.Path(out).unlink(missing_ok=True)
r = subprocess.run([edge, "--headless=new", "--disable-gpu", "--no-first-run", f"--user-data-dir={shots / f'profile{height}_{time.time_ns()}'}",
                    "--virtual-time-budget=4000", "--hide-scrollbars",
                    f"--window-size={len(STATES) * 372},{height + 14}", f"--screenshot={out}", wrap.as_uri()],
                   check=False, timeout=90, capture_output=True, text=True, errors="replace")
# The Edge launcher can return before the headless process has written the file.
for _ in range(60):
    if pathlib.Path(out).exists():
        time.sleep(1)
        break
    time.sleep(.5)
print(out, pathlib.Path(out).exists(), r.returncode, r.stderr[-400:])
