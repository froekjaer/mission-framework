# Mistral implementation

Canonical rule: [`../OP-001-Mission-Operational-Preamble.md`](../OP-001-Mission-Operational-Preamble.md)

## Repository mode — recommended

Use [`SYSTEM-PROMPT.md`](./SYSTEM-PROMPT.md) as the project/system instruction only for `froekjaer/mission-framework` and repositories explicitly governed by it. Provide repository access or the relevant authoritative files.

## Global mode

Use the same loader as a persistent system instruction and broaden its scope to all substantive engineering, research, governance, documentation and repository commands.

Repository mode avoids recurring token use in unrelated conversations.

## Runtime behaviour

Mistral should retrieve OP-001 only for in-scope work, keep the visible preamble compact, and stop rather than infer unavailable operational facts. Writes must be verified by reading back the result.

## Validation

Ask Mistral to confirm source retrieval, scope boundaries, stop conditions and estimated recurring prompt overhead.
