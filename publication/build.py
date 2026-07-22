#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import html
import json
import os
import shutil
import subprocess
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
WORK = ROOT / "build" / "publication"
COMMIT = os.getenv("GITHUB_SHA") or subprocess.run(
    ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True, capture_output=True, check=True
).stdout.strip()
REPOSITORY = os.getenv("GITHUB_REPOSITORY", "froekjaer/mission-framework")
GENERATOR_VERSION = "1.0.0"


def run(*args: str) -> None:
    print("+", " ".join(args))
    subprocess.run(args, cwd=ROOT, check=True)


def clean() -> None:
    shutil.rmtree(DIST, ignore_errors=True)
    shutil.rmtree(WORK, ignore_errors=True)
    for path in [DIST / "book", DIST / "brief", DIST / "presentation", DIST / "site", DIST / "review-package", DIST / "manifests", WORK]:
        path.mkdir(parents=True, exist_ok=True)


def read_config() -> dict:
    return yaml.safe_load((ROOT / "publication" / "book.yml").read_text(encoding="utf-8"))


def existing_sources(config: dict) -> tuple[list[Path], list[str]]:
    declared = list(config.get("sources", [])) + list(config.get("appendices", []))
    found, missing = [], []
    for relative in declared:
        path = ROOT / relative
        (found if path.is_file() else missing).append(path if path.is_file() else relative)
    return found, missing


def provenance_header(title: str) -> str:
    generated = datetime.now(timezone.utc).isoformat()
    return (
        "---\n"
        f"title: {title}\n"
        f"source-repository: {REPOSITORY}\n"
        f"source-commit: {COMMIT}\n"
        f"generator-version: {GENERATOR_VERSION}\n"
        f"generated-at: {generated}\n"
        "review-status: pre-review\n"
        "---\n\n"
        "> **Derived publication.** Canonical meaning remains in the repository Markdown at the source commit shown above.\n\n"
    )


def assemble_book(config: dict, sources: list[Path]) -> Path:
    target = WORK / "book.md"
    parts = [provenance_header(config.get("title", "Mission Framework"))]
    for source in sources:
        relative = source.relative_to(ROOT)
        parts.append(f"\n\n<!-- source: {relative} -->\n\n")
        parts.append(source.read_text(encoding="utf-8"))
    target.write_text("".join(parts), encoding="utf-8")
    return target


def pandoc(source: Path, target: Path, *extra: str) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    run("pandoc", str(source), "--from=gfm+yaml_metadata_block", "--standalone", "--toc", *extra, "-o", str(target))


def render_book(book_md: Path) -> None:
    pandoc(book_md, DIST / "book" / "Mission-Framework.html", "--metadata", "title=Mission Framework")
    pandoc(book_md, DIST / "book" / "Mission-Framework.docx")
    pandoc(book_md, DIST / "book" / "Mission-Framework.epub")
    html_file = DIST / "book" / "Mission-Framework.html"
    run("weasyprint", str(html_file), str(DIST / "book" / "Mission-Framework.pdf"))
    shutil.copy2(book_md, DIST / "book" / "Mission-Framework.md")


def render_brief() -> None:
    source = ROOT / "publication" / "executive-brief.md"
    md = WORK / "executive-brief.md"
    md.write_text(provenance_header("Mission Framework — Executive Brief") + source.read_text(encoding="utf-8"), encoding="utf-8")
    pandoc(md, DIST / "brief" / "Mission-Framework-Executive-Brief.html")
    pandoc(md, DIST / "brief" / "Mission-Framework-Executive-Brief.docx")
    run("weasyprint", str(DIST / "brief" / "Mission-Framework-Executive-Brief.html"), str(DIST / "brief" / "Mission-Framework-Executive-Brief.pdf"))
    shutil.copy2(md, DIST / "brief" / "Mission-Framework-Executive-Brief.md")


def render_presentation() -> None:
    source = ROOT / "publication" / "presentation.md"
    md = WORK / "presentation.md"
    md.write_text(provenance_header("Mission Framework — Presentation") + source.read_text(encoding="utf-8"), encoding="utf-8")
    run("pandoc", str(md), "--from=gfm+yaml_metadata_block", "--slide-level=1", "-o", str(DIST / "presentation" / "Mission-Framework-Introduction.pptx"))
    run("pandoc", str(md), "--from=gfm+yaml_metadata_block", "--standalone", "-t", "revealjs", "-o", str(DIST / "presentation" / "index.html"))
    shutil.copy2(md, DIST / "presentation" / "Mission-Framework-Introduction.md")


def site_page(source: Path, target: Path, title: str) -> None:
    run("pandoc", str(source), "--from=gfm+yaml_metadata_block", "--standalone", "--toc", "--metadata", f"title={title}", "-o", str(target))


def render_site(sources: list[Path]) -> None:
    site = DIST / "site"
    links = []
    for source in sources:
        relative = source.relative_to(ROOT)
        slug = str(relative).replace("/", "--").replace(".md", ".html")
        target = site / slug
        site_page(source, target, relative.stem.replace("_", " ").title())
        links.append((relative, slug))
    index = ["<!doctype html><html><head><meta charset='utf-8'><title>Mission Framework</title>",
             "<style>body{font-family:system-ui;max-width:980px;margin:3rem auto;padding:0 1.2rem;line-height:1.55}li{margin:.45rem 0}code{background:#eee;padding:.15rem .3rem}</style></head><body>",
             "<h1>Mission Framework</h1>",
             "<p>A navigable publication generated from canonical repository Markdown.</p>",
             f"<p><strong>Source commit:</strong> <code>{html.escape(COMMIT)}</code></p>",
             "<h2>Publications</h2><ul>",
             "<li><a href='book/Mission-Framework.html'>Book</a></li>",
             "<li><a href='brief/Mission-Framework-Executive-Brief.html'>Executive Brief</a></li>",
             "<li><a href='presentation/index.html'>Presentation</a></li></ul>",
             "<h2>Canonical source views</h2><ul>"]
    for relative, slug in links:
        index.append(f"<li><a href='{html.escape(slug)}'>{html.escape(str(relative))}</a></li>")
    index.append("</ul><p>Generated artefacts are derived. Semantic corrections belong in Markdown.</p></body></html>")
    (site / "index.html").write_text("\n".join(index), encoding="utf-8")
    shutil.copytree(DIST / "book", site / "book", dirs_exist_ok=True)
    shutil.copytree(DIST / "brief", site / "brief", dirs_exist_ok=True)
    shutil.copytree(DIST / "presentation", site / "presentation", dirs_exist_ok=True)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def write_manifest(missing: list[str]) -> Path:
    files = []
    for path in sorted(p for p in DIST.rglob("*") if p.is_file() and "manifests" not in p.parts):
        files.append({"path": str(path.relative_to(DIST)), "sha256": sha256(path), "bytes": path.stat().st_size})
    manifest = {
        "pipeline_status": "rendered",
        "generator_version": GENERATOR_VERSION,
        "repository": REPOSITORY,
        "source_commit": COMMIT,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "review_status": "pre-review",
        "missing_declared_sources": missing,
        "artefacts": files,
    }
    target = DIST / "manifests" / "publication-manifest.json"
    target.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    checksum = DIST / "manifests" / "SHA256SUMS"
    checksum.write_text("\n".join(f"{item['sha256']}  {item['path']}" for item in files) + "\n", encoding="utf-8")
    return target


def review_package() -> None:
    package_dir = DIST / "review-package" / "Mission-Framework-Review-Package"
    package_dir.mkdir(parents=True, exist_ok=True)
    for directory in ["book", "brief", "presentation", "manifests"]:
        shutil.copytree(DIST / directory, package_dir / directory, dirs_exist_ok=True)
    for relative in ["reviews/MIAR/README.md", "reviews/MIAR/INTRODUCTION-AND-ASSURANCE-FLOW.md", "reviews/MIAR/ORGANISATION-INTRODUCTION-TEMPLATE.md"]:
        source = ROOT / relative
        if source.is_file():
            target = package_dir / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
    zip_path = DIST / "review-package" / "Mission-Framework-Review-Package.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in package_dir.rglob("*"):
            if path.is_file():
                archive.write(path, path.relative_to(package_dir.parent))


def main() -> int:
    clean()
    config = read_config()
    sources, missing = existing_sources(config)
    if not sources:
        print("No declared book sources exist.", file=sys.stderr)
        return 1
    if missing:
        print("Warning: declared sources not found:", *missing, sep="\n- ")
    book_md = assemble_book(config, sources)
    render_book(book_md)
    render_brief()
    render_presentation()
    render_site(sources)
    write_manifest(missing)
    review_package()
    write_manifest(missing)
    print(f"Built {sum(1 for p in DIST.rglob('*') if p.is_file())} files in {DIST}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
