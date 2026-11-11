"""Package ttara.html as an installable web app (PWA). Usage: ttara_app.py <scratchpad> <out_dir>"""
import json
import pathlib
import sys

from PIL import Image, ImageDraw, ImageFont

base = pathlib.Path(sys.argv[1])
out = pathlib.Path(sys.argv[2])
out.mkdir(parents=True, exist_ok=True)

NAME, SHORT = "따라말하기 영어", "따라말하기"
INK, PAPER, YELLOW = "#17130f", "#ece6dc", "#ffce3a"

page = (base / "ttara.html").read_text(encoding="utf-8")
claude_meta = '<meta name="claude:viewport-fit-sides" content="cover">\n'
assert page.count(claude_meta) == 1
page = page.replace(claude_meta, "")

head = f"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="{INK}">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="{SHORT}">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" href="icon-192.png">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<style>html, body {{ margin: 0; }}</style>
<script>if ("serviceWorker" in navigator) addEventListener("load", () => navigator.serviceWorker.register("sw.js").catch(() => {{}}));</script>
</head>
<body>
"""
(out / "index.html").write_text(head + page + "</body>\n</html>\n", encoding="utf-8", newline="\n")

manifest = {
    "name": NAME, "short_name": SHORT, "lang": "ko",
    "start_url": "./", "scope": "./", "display": "standalone", "orientation": "portrait",
    "background_color": PAPER, "theme_color": INK,
    "icons": [
        {"src": "icon-192.png", "sizes": "192x192", "type": "image/png", "purpose": "any"},
        {"src": "icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any"},
        {"src": "icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"},
    ],
}
(out / "manifest.webmanifest").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

# Network first for the app's own files, so a new version shows up on the next online launch;
# the cache only answers when the phone is offline. Fonts rarely change, so they come from the cache.
SW = """const CACHE = "ttara";
const CORE = ["./", "index.html", "manifest.webmanifest", "icon-192.png", "icon-512.png", "apple-touch-icon.png"];
self.addEventListener("install", (e) => { e.waitUntil(caches.open(CACHE).then((c) => c.addAll(CORE))); self.skipWaiting(); });
self.addEventListener("activate", (e) => e.waitUntil(self.clients.claim()));

const timeout = (ms) => new Promise((_, no) => setTimeout(() => no(new Error("slow")), ms));
async function networkFirst(req) {
  const cache = await caches.open(CACHE);
  try {
    const res = await Promise.race([fetch(req, { cache: "no-cache" }), timeout(4000)]);
    if (res.ok) cache.put(req, res.clone());
    return res;
  } catch (e) {
    return (await cache.match(req, { ignoreSearch: true })) || (await cache.match("index.html")) || Response.error();
  }
}
async function cacheFirst(req) {
  const cache = await caches.open(CACHE);
  const hit = await cache.match(req);
  if (hit) return hit;
  const res = await fetch(req);
  if (res.ok || res.type === "opaque") cache.put(req, res.clone());
  return res;
}
self.addEventListener("fetch", (e) => {
  if (e.request.method !== "GET") return;
  const url = new URL(e.request.url);
  if (url.origin === location.origin) e.respondWith(networkFirst(e.request));
  else if (/fonts\\.(googleapis|gstatic)\\.com$/.test(url.hostname)) e.respondWith(cacheFirst(e.request));
});
"""
(out / "sw.js").write_text(SW, encoding="utf-8", newline="\n")
(out / ".nojekyll").write_text("", encoding="utf-8")


def icon(size: int) -> Image.Image:
    """Yellow tile with a white sticker speech bubble; the art stays inside the maskable safe zone."""
    k = 4  # Draw large, then shrink for smooth edges.
    s = size * k
    im = Image.new("RGB", (s, s), YELLOW)
    d = ImageDraw.Draw(im)
    w = round(s * 0.035)
    box = (s * 0.2, s * 0.24, s * 0.8, s * 0.66)
    shadow = tuple(v + s * 0.025 for v in box)
    tail = [(s * 0.33, s * 0.62), (s * 0.29, s * 0.79), (s * 0.47, s * 0.64)]
    d.rounded_rectangle(shadow, radius=s * 0.09, fill=INK)
    d.polygon([(x + s * 0.025, y + s * 0.025) for x, y in tail], fill=INK)
    d.polygon(tail, fill="#fffdf7", outline=INK, width=w)
    d.rounded_rectangle(box, radius=s * 0.09, fill="#fffdf7", outline=INK, width=w)
    # Erase the bubble's bottom edge where the tail joins: a shrunken copy of the tail stays clear of its outline.
    cx, cy = sum(x for x, _ in tail) / 3, sum(y for _, y in tail) / 3
    d.polygon([(cx + (x - cx) * 0.55, cy + (y - cy) * 0.55) for x, y in tail], fill="#fffdf7")
    font = ImageFont.truetype(r"C:\Windows\Fonts\seguibl.ttf", round(s * 0.2))
    d.text((s * 0.5, s * 0.45), "Hi!", font=font, fill=INK, anchor="mm")
    return im.resize((size, size), Image.LANCZOS)


icon(512).save(out / "icon-512.png")
icon(192).save(out / "icon-192.png")
icon(180).save(out / "apple-touch-icon.png")
print("app written to", out, sorted(p.name for p in out.iterdir()))
