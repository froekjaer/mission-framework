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
GENERATOR_VERSION = "1.1.0"
GENERATED_AT = datetime.now(timezone.utc).isoformat()


def run(*args: str) -> None:
    print("+", " ".join(args))
    subprocess.run(args, cwd=ROOT, check=True)


def clean() -> None:
    shutil.rmtree(DIST, ignore_errors=True)
    shutil.rmtree(WORK, ignore_errors=True)
    for path in [
        DIST / "book",
        DIST / "brief",
        DIST / "presentation",
        DIST / "site",
        DIST / "review-package",
        DIST / "manifests",
        WORK,
    ]:
        path.mkdir(parents=True, exist_ok=True)


def read_config() -> dict:
    return yaml.safe_load((ROOT / "publication" / "book.yml").read_text(encoding="utf-8"))


def existing_sources(config: dict) -> tuple[list[Path], list[str]]:
    declared = list(config.get("sources", [])) + list(config.get("appendices", []))
    found: list[Path] = []
    missing: list[str] = []
    for relative in declared:
        path = ROOT / relative
        if path.is_file():
            found.append(path)
        else:
            missing.append(relative)
    return found, missing


def provenance_header(title: str) -> str:
    return (
        "---\n"
        f"title: {title}\n"
        f"source-repository: {REPOSITORY}\n"
        f"source-commit: {COMMIT}\n"
        f"generator-version: {GENERATOR_VERSION}\n"
        f"generated-at: {GENERATED_AT}\n"
        "review-status: pre-review\n"
        "audience-profile: declared-by-publication\n"
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


def pandoc(source: Path, target: Path, *extra: str, toc: bool = True) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    command = ["pandoc", str(source), "--from=gfm+yaml_metadata_block", "--standalone"]
    if toc:
        command.append("--toc")
    command.extend(extra)
    command.extend(["-o", str(target)])
    run(*command)


def render_book(book_md: Path) -> None:
    pandoc(book_md, DIST / "book" / "Mission-Framework.html", "--metadata", "title=Mission Framework")
    pandoc(book_md, DIST / "book" / "Mission-Framework.docx")
    pandoc(book_md, DIST / "book" / "Mission-Framework.epub")
    run("weasyprint", str(DIST / "book" / "Mission-Framework.html"), str(DIST / "book" / "Mission-Framework.pdf"))
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
    pandoc(md, DIST / "presentation" / "Mission-Framework-Introduction.html", toc=False)
    run("weasyprint", str(DIST / "presentation" / "Mission-Framework-Introduction.html"), str(DIST / "presentation" / "Mission-Framework-Introduction.pdf"))
    shutil.copy2(md, DIST / "presentation" / "Mission-Framework-Introduction.md")


def site_page(source: Path, target: Path, title: str) -> None:
    run("pandoc", str(source), "--from=gfm+yaml_metadata_block", "--standalone", "--toc", "--metadata", f"title={title}", "-o", str(target))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def write_manifest(missing: list[str]) -> Path:
    files = []
    for path in sorted(p for p in DIST.rglob("*") if p.is_file() and "manifests" not in p.parts and "site" not in p.parts):
        files.append({"path": str(path.relative_to(DIST)), "sha256": sha256(path), "bytes": path.stat().st_size})
    manifest = {
        "pipeline_status": "rendered",
        "generator_version": GENERATOR_VERSION,
        "repository": REPOSITORY,
        "source_commit": COMMIT,
        "generated_at": GENERATED_AT,
        "review_status": "pre-review",
        "audience_delivery_model": "Audience-Adaptive Knowledge Delivery",
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
    for relative in [
        "reviews/MIAR/README.md",
        "reviews/MIAR/INTRODUCTION-AND-ASSURANCE-FLOW.md",
        "reviews/MIAR/ORGANISATION-INTRODUCTION-TEMPLATE.md",
        "docs/publication/AUDIENCE-ADAPTIVE-KNOWLEDGE-DELIVERY.md",
    ]:
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


def publication_catalog() -> dict:
    return {
        "schema": "https://mission-framework.example/schemas/publication-catalog-v1",
        "project": "Mission Framework",
        "source_repository": REPOSITORY,
        "source_commit": COMMIT,
        "generated_at": GENERATED_AT,
        "review_status": "pre-review",
        "publications": [
            {
                "id": "book",
                "title": "Mission Framework Book",
                "audience": ["practitioner", "researcher", "reviewer", "machine-assisted-reader"],
                "purpose": "Complete, sustained reading edition",
                "formats": {
                    "read_online": "book/Mission-Framework.html",
                    "pdf": "book/Mission-Framework.pdf",
                    "epub": "book/Mission-Framework.epub",
                    "docx": "book/Mission-Framework.docx",
                    "markdown": "book/Mission-Framework.md",
                },
            },
            {
                "id": "executive-brief",
                "title": "Executive Brief",
                "audience": ["decision-maker", "new-reader", "reviewer"],
                "purpose": "Rapid orientation before deeper reading",
                "formats": {
                    "read_online": "brief/Mission-Framework-Executive-Brief.html",
                    "pdf": "brief/Mission-Framework-Executive-Brief.pdf",
                    "docx": "brief/Mission-Framework-Executive-Brief.docx",
                    "markdown": "brief/Mission-Framework-Executive-Brief.md",
                },
            },
            {
                "id": "presentation",
                "title": "Project Presentation",
                "audience": ["meeting-participant", "speaker", "reviewer"],
                "purpose": "Facilitated introduction to the project",
                "formats": {
                    "view_online": "presentation/index.html",
                    "pptx": "presentation/Mission-Framework-Introduction.pptx",
                    "pdf": "presentation/Mission-Framework-Introduction.pdf",
                    "markdown": "presentation/Mission-Framework-Introduction.md",
                },
            },
            {
                "id": "review-package",
                "title": "MIAR Review Package",
                "audience": ["independent-reviewer", "assurance-agent"],
                "purpose": "Bounded material for independent review",
                "formats": {"zip": "review-package/Mission-Framework-Review-Package.zip"},
            },
        ],
        "machine_resources": {
            "provenance": "manifests/publication-manifest.json",
            "checksums": "manifests/SHA256SUMS",
            "catalog": "publication-catalog.json",
        },
    }


def render_site(sources: list[Path]) -> None:
    site = DIST / "site"
    for directory in ["book", "brief", "presentation", "review-package", "manifests"]:
        shutil.copytree(DIST / directory, site / directory, dirs_exist_ok=True)

    source_links = []
    source_dir = site / "source"
    source_dir.mkdir(parents=True, exist_ok=True)
    for source in sources:
        relative = source.relative_to(ROOT)
        slug = str(relative).replace("/", "--").replace(".md", ".html")
        target = source_dir / slug
        site_page(source, target, relative.stem.replace("_", " ").replace("-", " ").title())
        source_links.append((relative, f"source/{slug}"))

    catalog = publication_catalog()
    (site / "publication-catalog.json").write_text(json.dumps(catalog, indent=2) + "\n", encoding="utf-8")

    cards = [
        ("📘", "Bog", "Den komplette og senest genererede læseudgave af Mission Framework.", "book/Mission-Framework.html", "Læs online", [("PDF", "book/Mission-Framework.pdf"), ("EPUB", "book/Mission-Framework.epub"), ("DOCX", "book/Mission-Framework.docx")]),
        ("📄", "Executive Brief", "En kort introduktion til formål, principper og anvendelse.", "brief/Mission-Framework-Executive-Brief.html", "Læs brief", [("PDF", "brief/Mission-Framework-Executive-Brief.pdf"), ("DOCX", "brief/Mission-Framework-Executive-Brief.docx")]),
        ("🎤", "Præsentation", "En præsentabel introduktion til møder, dialog og review.", "presentation/index.html", "Se online", [("PPTX", "presentation/Mission-Framework-Introduction.pptx"), ("PDF", "presentation/Mission-Framework-Introduction.pdf")]),
        ("📦", "Review Package", "Samlet materiale til MIAR og uafhængig vurdering.", "review-package/Mission-Framework-Review-Package.zip", "Hent ZIP", []),
    ]
    card_html = []
    for icon, title, description, primary_href, primary_label, secondary in cards:
        buttons = [f'<a class="button primary" href="{html.escape(primary_href)}">{html.escape(primary_label)}</a>']
        buttons.extend(f'<a class="button" href="{html.escape(href)}">{html.escape(label)}</a>' for label, href in secondary)
        card_html.append(
            f'<article class="card"><div class="icon" aria-hidden="true">{icon}</div><h2>{html.escape(title)}</h2>'
            f'<p>{html.escape(description)}</p><div class="actions">{"".join(buttons)}</div></article>'
        )

    source_list = "".join(f'<li><a href="{html.escape(slug)}">{html.escape(str(relative))}</a></li>' for relative, slug in source_links)
    short_commit = html.escape(COMMIT[:12])
    index = f"""<!doctype html>
<html lang="da">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="Mission Framework Publication Hub — latest governed publications, review material and provenance.">
<title>Mission Framework — Publication Hub</title>
<style>
:root{{--bg:#f5f7fb;--surface:#ffffff;--text:#182033;--muted:#5f6b7a;--line:#dfe5ee;--accent:#2457d6;--accent-dark:#183f9f;--soft:#eaf0ff;--radius:18px}}
*{{box-sizing:border-box}}html{{scroll-behavior:smooth}}body{{margin:0;background:var(--bg);color:var(--text);font-family:system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;line-height:1.6}}
a{{color:var(--accent)}}a:focus-visible,button:focus-visible{{outline:3px solid #ffbf47;outline-offset:3px}}
.skip{{position:absolute;left:-999px;top:0}}.skip:focus{{left:1rem;top:1rem;background:#fff;padding:.8rem;z-index:10}}
header{{background:linear-gradient(135deg,#13254a,#2457d6);color:#fff;padding:4.8rem 1.25rem 4rem}}.wrap{{max-width:1120px;margin:auto}}.eyebrow{{font-weight:700;letter-spacing:.08em;text-transform:uppercase;font-size:.78rem;opacity:.82}}h1{{font-size:clamp(2.4rem,7vw,5rem);line-height:1.04;margin:.5rem 0 1rem;max-width:900px}}.lead{{font-size:clamp(1.05rem,2vw,1.35rem);max-width:780px;color:#e8eeff}}.status{{display:flex;flex-wrap:wrap;gap:.7rem;margin-top:1.5rem}}.pill{{background:rgba(255,255,255,.13);border:1px solid rgba(255,255,255,.28);padding:.45rem .75rem;border-radius:999px;font-size:.9rem}}
main{{padding:2.5rem 1.25rem 5rem}}.intro{{display:grid;grid-template-columns:2fr 1fr;gap:1.5rem;margin-bottom:2rem}}.panel,.card{{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);box-shadow:0 8px 30px rgba(22,34,64,.06)}}.panel{{padding:1.5rem}}.panel h2{{margin-top:0}}.grid{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:1.25rem}}.card{{padding:1.6rem;display:flex;flex-direction:column;min-height:270px}}.card .icon{{font-size:2rem}}.card h2{{margin:.6rem 0 .2rem}}.card p{{color:var(--muted);flex:1}}.actions{{display:flex;flex-wrap:wrap;gap:.65rem;margin-top:1rem}}.button{{display:inline-block;text-decoration:none;border:1px solid var(--line);border-radius:10px;padding:.65rem .9rem;font-weight:650;background:#fff;color:var(--text)}}.button:hover{{border-color:var(--accent);color:var(--accent)}}.button.primary{{background:var(--accent);border-color:var(--accent);color:#fff}}.button.primary:hover{{background:var(--accent-dark)}}
details{{margin-top:2rem;background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);padding:1rem 1.25rem}}summary{{cursor:pointer;font-weight:750}}.machine{{margin-top:2rem;background:var(--soft);border-radius:var(--radius);padding:1.4rem}}code{{background:#eef1f5;padding:.15rem .35rem;border-radius:5px;overflow-wrap:anywhere}}footer{{border-top:1px solid var(--line);padding:2rem 1.25rem;color:var(--muted)}}
@media(max-width:760px){{.intro,.grid{{grid-template-columns:1fr}}header{{padding-top:3.2rem}}.card{{min-height:auto}}}}
@media(prefers-reduced-motion:reduce){{html{{scroll-behavior:auto}}}}
</style>
</head>
<body>
<a class="skip" href="#publications">Gå til publikationer</a>
<header><div class="wrap"><div class="eyebrow">Official Publication Hub</div><h1>Mission Framework</h1><p class="lead">Et åbent, evidens- og governance-orienteret framework. Her finder mennesker og maskiner de nyeste afledte publikationer fra den samme kanoniske viden.</p><div class="status"><span class="pill">Status: Pre-review</span><span class="pill">Generator {GENERATOR_VERSION}</span><span class="pill">Kilde {short_commit}</span><span class="pill">Opdateret {html.escape(GENERATED_AT[:10])}</span></div></div></header>
<main class="wrap" id="publications">
<section class="intro" aria-labelledby="start"><div class="panel"><h2 id="start">Start her</h2><p>Vælg den form, der passer til dit formål. Du behøver ikke kende GitHub, mapper eller build-systemet. Alle filer nedenfor er genereret fra projektets styrede Markdown-kilder.</p><p><strong>Ny læser:</strong> begynd med Executive Brief. <strong>Dyb forståelse:</strong> vælg bogen. <strong>Møde eller oplæg:</strong> hent PPTX. <strong>Uafhængig vurdering:</strong> hent Review Package.</p></div><aside class="panel"><h2>Princip</h2><p><strong>Availability is not usability, and usability is not understanding.</strong></p><p>Platformen anvender Audience-Adaptive Knowledge Delivery.</p></aside></section>
<section class="grid" aria-label="Tilgængelige publikationer">{''.join(card_html)}</section>
<section class="machine"><h2>For maskiner og verificering</h2><p>Struktureret opdagelse, provenance og integritetskontrol er tilgængelig uden at belaste den menneskelige navigation.</p><div class="actions"><a class="button" href="publication-catalog.json">Publication Catalog (JSON)</a><a class="button" href="manifests/publication-manifest.json">Provenance Manifest</a><a class="button" href="manifests/SHA256SUMS">SHA-256 Checksums</a></div></section>
<details><summary>Kanoniske kilder og teknisk sporbarhed</summary><p>Genererede artefakter er afledte. Semantiske rettelser foretages i repositoryets Markdown-kilder.</p><ul>{source_list}</ul><p><a href="https://github.com/{html.escape(REPOSITORY)}">Åbn repository på GitHub</a></p></details>
</main>
<footer><div class="wrap">Mission Framework Publication Hub · Source commit <code>{html.escape(COMMIT)}</code> · Generated {html.escape(GENERATED_AT)}</div></footer>
</body></html>"""
    (site / "index.html").write_text(index, encoding="utf-8")


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
    write_manifest(missing)
    review_package()
    write_manifest(missing)
    render_site(sources)
    print(f"Built {sum(1 for p in DIST.rglob('*') if p.is_file())} files in {DIST}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
