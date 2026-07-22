# Operational AI Integration

This directory contains vendor-specific, token-efficient ways to activate [OP-001](./OP-001-Mission-Operational-Preamble.md).

## Design rule

Do not copy OP-001 into every prompt. Each integration uses a short loader that instructs the AI to retrieve the canonical file only for substantive Mission Framework work.

Routine conversation is out of scope. Repository reads, writes, architecture, governance, research, reviews, releases and canonical identifiers are in scope.

## Implementations

- [ChatGPT](./chatgpt/README.md)
- [Claude](./claude/README.md)
- [Codex](./codex/README.md)
- [Mistral](./mistral/README.md)
- [Z.ai](./z-ai/README.md)

Each directory distinguishes:

1. **Global mode** — applies to all substantive commands in that AI environment.
2. **Repository mode** — applies only inside `froekjaer/mission-framework` or another repository that explicitly installs the loader.

## Validation request

Each AI should be asked to verify that its implementation:

- loads the canonical OP-001 rather than a copied version;
- does not activate for routine conversation;
- stops when authoritative state cannot be verified;
- verifies write results by reading them back;
- adds minimal recurring token overhead.
