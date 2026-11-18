"""Bygger index.html från template.html, innehållsfilerna och bilderna.
Kör från repots rot:  python src/build.py
"""
import base64, pathlib
src = pathlib.Path(__file__).parent
b64 = lambda p: base64.b64encode((src / p).read_bytes()).decode()
html = (src / "template.html").read_text(encoding="utf-8")
html = html.replace("__CH__", (src / "content_ch.js").read_text(encoding="utf-8"))
html = html.replace("__INFO__", (src / "content_info.js").read_text(encoding="utf-8"))
html = html.replace("__LOGO__", b64("logo.png"))
for k in ["hero", "ov", "plan", "steg", "logg", "fragor"]:
    html = html.replace(f"__BG_{k}__", b64(f"bg/{k}.jpg"))
(src.parent / "index.html").write_text(html, encoding="utf-8")
print("index.html byggd,", len(html) // 1024, "KB")
