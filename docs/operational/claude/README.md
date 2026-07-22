# Claude implementation

Canonical rule: [`../OP-001-Mission-Operational-Preamble.md`](../OP-001-Mission-Operational-Preamble.md)

## Repository mode — recommended

Place [`CLAUDE.md`](./CLAUDE.md) at the root of `froekjaer/mission-framework`, or copy its loader into the repository's existing `CLAUDE.md`. Install it only in other repositories that are explicitly governed by Mission Framework.

## Global mode

Place the loader in Claude's user- or project-level instructions and change its scope to all substantive engineering, research, governance, documentation and repository work.

Repository mode is preferred because it avoids loading the rule in unrelated conversations.

## Runtime behaviour

Claude should retrieve OP-001 only when work is in scope, show a compact execution trace, and verify writes by reading the resulting state. The full procedure should not be repeated in normal responses.

## Validation

Ask Claude to verify file discovery, scope boundaries, stop conditions and approximate recurring context overhead.
