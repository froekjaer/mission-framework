# Publication Pipeline

This directory contains the executable publication configuration for Mission Framework.

The normative publication model is defined in [`docs/publication/PUBLICATION-PIPELINE.md`](../docs/publication/PUBLICATION-PIPELINE.md).

## What the build produces

`publication/build.py` renders one source revision into:

- a book in Markdown, HTML, PDF, DOCX and EPUB;
- an executive brief in Markdown, HTML, PDF and DOCX;
- an introductory presentation in PPTX and reveal.js HTML;
- a navigable static website suitable for GitHub Pages;
- a review package in directory and ZIP form;
- a provenance manifest and SHA-256 checksum list.

Generated files are written to `dist/`. They are derived publications and do not replace the repository Markdown as canonical source.

## Canonical book assembly

`book.yml` defines the ordered source set. A declared source that is absent is reported in the manifest and as a build warning. The build fails when no declared canonical source is available.

## Automated build

`.github/workflows/publication-pipeline.yml` validates the profiles, installs Pandoc and WeasyPrint, runs the renderer, uploads the complete distribution as a GitHub Actions artifact and publishes `dist/site` through GitHub Pages on pushes to `main`.

GitHub Pages must be configured in the repository settings to use **GitHub Actions** as its source. Until that repository-level setting is enabled, the publication artifact can still build successfully while the deployment job may be rejected by GitHub.

## Local build

On a system with Python 3.12+, Pandoc and WeasyPrint:

```bash
python -m pip install pyyaml weasyprint
python publication/build.py
```

## Profiles

The profile files under `profiles/` declare the intended audience, source policy and outputs for:

- book;
- article;
- executive brief;
- review package;
- presentation;
- GitHub Pages.

The executable renderer currently implements the shared publication suite. Profile-specific selection and templating can evolve without changing the canonical-source principle.
