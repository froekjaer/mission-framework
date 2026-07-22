# Codex implementation

Canonical rule: [`../OP-001-Mission-Operational-Preamble.md`](../OP-001-Mission-Operational-Preamble.md)

## Repository mode — recommended

Place [`AGENTS.md`](./AGENTS.md) at the repository root, or merge its loader into an existing root `AGENTS.md`. Install the loader only in Mission Framework repositories that explicitly adopt OP-001.

## Global mode

Add the loader to Codex's persistent user instructions and broaden the scope to every substantive engineering or repository command.

Global mode consumes context in unrelated repositories. Repository mode is therefore preferred.

## Runtime behaviour

Codex should read the repository-local OP-001 before substantive work, inspect authoritative files and Git state, execute with verified identifiers, then inspect the resulting diff or files. It should emit only a short preamble status.

## Validation

Ask Codex to demonstrate instruction discovery, a no-write verification run, stop behaviour for an invented path, and estimated recurring token overhead.
