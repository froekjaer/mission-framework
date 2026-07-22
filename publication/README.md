# Mission Framework Publication Hub

This directory contains the configuration and generator for the governed Mission Framework publication suite.

The public user experience is the generated **Publication Hub** on GitHub Pages. Readers and reviewers should not need to navigate repository folders to find the current book, executive brief, presentation or review package.

## What the pipeline publishes

- **Book:** online HTML, PDF, EPUB, DOCX and Markdown;
- **Executive Brief:** online HTML, PDF, DOCX and Markdown;
- **Presentation:** online presentation, PPTX, PDF and Markdown;
- **Review Package:** a single downloadable ZIP;
- **Machine resources:** publication catalog, provenance manifest and SHA-256 checksums.

## Author workflow

1. Edit canonical Markdown in the repository.
2. Add or reorder book sources in `publication/book.yml` when necessary.
3. Edit `publication/executive-brief.md` for the short decision-maker entry point.
4. Edit `publication/presentation.md` for the project presentation.
5. Commit or merge to `main`.
6. GitHub Actions builds and publishes the complete suite.

Generated files are never editing sources.

## Audience-Adaptive Knowledge Delivery

The hub implements the model in [`docs/publication/AUDIENCE-ADAPTIVE-KNOWLEDGE-DELIVERY.md`](../docs/publication/AUDIENCE-ADAPTIVE-KNOWLEDGE-DELIVERY.md).

Human visitors receive a clear project introduction, purpose-based choices, direct download buttons, responsive layout and progressive disclosure of technical details. Machine consumers receive a stable JSON catalog, provenance manifest and checksums.

## Configuration

- `book.yml` declares the ordered canonical source set for the book.
- `executive-brief.md` is publication-specific orientation content.
- `presentation.md` is publication-specific slide content.
- `profiles/*.yml` declares publication intent, audience and expected output types.
- `build.py` performs the traceable transformations.

The normative publication model is defined in [`docs/publication/PUBLICATION-PIPELINE.md`](../docs/publication/PUBLICATION-PIPELINE.md).

## Local build

The supported build environment requires Python 3.12, PyYAML, Pandoc and WeasyPrint.

```bash
python publication/build.py
```

Outputs are created in `dist/`. The website entry point is `dist/site/index.html`.

## GitHub Pages

The repository should use **Settings → Pages → Build and deployment → Source: GitHub Actions**. The workflow publishes `dist/site` after successful builds on `main`.
