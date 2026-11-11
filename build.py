"""Build index.html for GitHub Pages from site/page.html.

site/page.html is the page source without a document skeleton (the same file
is published as the Claude artifact). This script wraps it in a full HTML
document so GitHub Pages renders it in standards mode.

Usage: python build.py
"""
from pathlib import Path

root = Path(__file__).parent
src = (root / "site" / "page.html").read_text(encoding="utf-8")

split = src.index("<header")
head, body = src[:split].rstrip(), src[split:].strip()

doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="Torque &amp; Code: our team for the 2026 NASA Space Apps Challenge in Eindhoven, building a Lunar Landing Site Navigator.">
<style>:root{{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}}body{{margin:0}}img{{max-width:100%}}[hidden]{{display:none!important}}</style>
{head}
</head>
<body>
{body}
</body>
</html>
"""
(root / "index.html").write_text(doc, encoding="utf-8")
print("wrote index.html")
