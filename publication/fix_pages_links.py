#!/usr/bin/env python3
from pathlib import Path
import os
import re
import sys

site = Path("dist/site")
index = site / "index.html"
if not index.is_file():
    raise SystemExit("dist/site/index.html is missing")

repository = os.getenv("GITHUB_REPOSITORY", "froekjaer/mission-framework")
repo_name = repository.split("/", 1)[-1]
base_href = f"/{repo_name}/"

text = index.read_text(encoding="utf-8")
if "<base " not in text:
    text = text.replace("<head>", f'<head>\n<base href="{base_href}">', 1)
index.write_text(text, encoding="utf-8")

required = [
    "book/Mission-Framework.html",
    "brief/Mission-Framework-Executive-Brief.html",
    "presentation/index.html",
    "review-package/Mission-Framework-Review-Package.zip",
    "publication-catalog.json",
    "manifests/publication-manifest.json",
    "manifests/SHA256SUMS",
]
missing = [relative for relative in required if not (site / relative).is_file()]
if missing:
    print("Missing required GitHub Pages files:", file=sys.stderr)
    for relative in missing:
        print(f"- {relative}", file=sys.stderr)
    raise SystemExit(1)

hrefs = re.findall(r'href="([^"]+)"', text)
for href in hrefs:
    if href.startswith(("http://", "https://", "#", "mailto:")):
        continue
    relative = href.lstrip("/")
    if relative.startswith(f"{repo_name}/"):
        relative = relative[len(repo_name) + 1:]
    if not (site / relative).exists():
        raise SystemExit(f"Broken local link in publication hub: {href}")

print(f"Validated Publication Hub for base path {base_href}")
