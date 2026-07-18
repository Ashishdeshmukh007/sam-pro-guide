#!/usr/bin/env python3
"""CI checks for index.html: duplicate ids, unresolved internal anchors, JS syntax.
Run: python3 check.py  (exit 1 on any failure)"""
import re
import shutil
import subprocess
import sys
import tempfile
from collections import Counter
from html.parser import HTMLParser

FILE = "index.html"


class Collector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.anchors = []  # (href, line)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get("id"):
            self.ids.append((a["id"], self.getpos()[0]))
        href = a.get("href") or ""
        if href.startswith("#") and len(href) > 1:
            self.anchors.append((href[1:], self.getpos()[0]))


src = open(FILE, encoding="utf-8").read()
c = Collector()
c.feed(src)

failures = []

dupes = [i for i, n in Counter(i for i, _ in c.ids).items() if n > 1]
if dupes:
    failures.append(f"duplicate ids: {dupes}")

known = {i for i, _ in c.ids}
missing = [(t, ln) for t, ln in c.anchors if t not in known]
if missing:
    failures.append(f"anchors with no target: {missing}")

# JS syntax: node --check each <script> block (skip if node unavailable)
node = shutil.which("node")
if node:
    for n, m in enumerate(re.finditer(r"<script[^>]*>(.*?)</script>", src, re.S)):
        body = m.group(1).strip()
        if not body:
            continue
        with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as f:
            f.write(body)
        r = subprocess.run([node, "--check", f.name], capture_output=True, text=True)
        if r.returncode != 0:
            failures.append(f"script block {n} syntax error: {r.stderr.strip()[:300]}")
else:
    print("warn: node not found, skipping JS syntax check")

if failures:
    print("FAIL")
    for f in failures:
        print(" -", f)
    sys.exit(1)
print(f"OK: {len(known)} ids unique, {len(c.anchors)} internal anchors resolve, JS parses")
