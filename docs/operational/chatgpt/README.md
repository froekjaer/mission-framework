# ChatGPT implementation

Canonical rule: [`../OP-001-Mission-Operational-Preamble.md`](../OP-001-Mission-Operational-Preamble.md)

## Repository mode — recommended

Add the contents of [`PROJECT-INSTRUCTIONS.md`](./PROJECT-INSTRUCTIONS.md) to the Mission Framework project's instructions. This limits activation to substantive work in `froekjaer/mission-framework` and repositories explicitly identified as related.

## Global mode

Add the same loader to ChatGPT Custom Instructions and replace the scope sentence with:

> Apply this procedure to every substantive engineering, research, governance, documentation or repository command.

Global mode increases recurring context use. Repository mode is preferred.

## Runtime behaviour

ChatGPT should fetch the current OP-001 when a task enters scope, perform the procedure, show only a compact visible status, execute, and read back writes. It must not paste the full OP-001 into every response.

## Validation

Ask ChatGPT to identify the canonical file, explain when the loader activates, perform one read-only test and report estimated recurring prompt overhead.
