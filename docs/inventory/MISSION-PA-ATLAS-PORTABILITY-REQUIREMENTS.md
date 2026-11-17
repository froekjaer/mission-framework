# Mission PA — Project Atlas / Mindmap portability contract

Status: **proposed integration requirement**, not implemented. Decision source: project-owner conversation, 2026-11-17.

## Purpose
Preserve an inspectable project/repository/branch/PR/document relationship graph that can later be imported into Mission PA without treating the visualization as the authoritative source.

## Authority and provenance
- GitHub is authoritative for Git refs, commits, pull requests, and repository files.
- Mission PA may store project classifications, decisions, and cross-system links with explicit provenance.
- User-confirmed activity state ("under development") is separate from independently verified build/test/deploy state.
- No production change, database migration, or external sync is authorized by this proposal.

## Proposed portable record shape
Use versioned UTF-8 JSON or YAML, validated against a future schema. Stable IDs should be namespaced (e.g. `github:repo:froekjaer/mission-pa`, `github:branch:froekjaer/mission-pa:main`). Do not infer relationships from filenames alone.

```json
{
  "schema_version": "0.1-proposal",
  "nodes": [
    {"id": "github:repo:froekjaer/mission-pa", "type": "repository", "label": "mission-pa", "source": "https://github.com/froekjaer/mission-pa", "observed_at": "2026-11-17", "verification": "indexed"}
  ],
  "edges": [],
  "unresolved": ["local uncommitted changes", "cross-branch content review", "GRC data mapping"]
}
```

Each edge should carry `from`, `to`, `relation_type`, `evidence_uri`, `observed_at`, `confidence_status` (verified / reported / inferred / unknown), and optional decision reference. Keep evidence of disagreement rather than collapsing contradictory sources.

## Migration and acceptance criteria
1. Export/import round trip preserves IDs, source URLs, timestamps, decisions, and unknowns.
2. Reimport is idempotent; source updates do not overwrite human decisions silently.
3. Visual graph and tabular inventory are views of the same records.
4. Branch and PR pagination is exhausted before a snapshot is marked complete.
5. Local worktree state is reported separately; absence of access is never interpreted as clean.
6. No production deployment until access, security, backup and recovery gates are explicitly approved.

## Current evidence limits
The main-branch file inventory was recorded separately in `docs/inventory/REPOSITORY-READING-LEDGER-2026-11-17.md` on this working branch. Branch inventory and PR content assessment are not complete in that document. The TimeLapse Pro GRC database has not been inspected; integration awaits a functioning Mission PA.
