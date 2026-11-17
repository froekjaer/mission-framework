# Branch and PR reconnaissance — 2026-11-17

Read-only GitHub discovery; not code review. First 100 branches and first 100 open PRs per repository. Local uncommitted files not accessible. No production changes.

| Repository | Branches returned | Open PRs |
|---|---:|---:|
| mission-framework | 15 | 8 |
| collaborative-intelligence | 11 | 7 |
| Mission-Platform | 14 | 4 |
| -Publication-Pipeline | 6 | 4 |
| mission-pa | 2 | 0 |
| timelapse-pro | 100 | 23 |
| waterworks-pro | 1 | 0 |
| mission-resilience | 15 | 1 |
| mission-solar-eclipse | 2 | 1 |
| conference-copilot | 2 | 0 |

Total: at least 168 branches and 48 open PRs. TimeLapse Pro hit the 100-branch page limit, so more branches may exist. Other repositories remain to be scanned. Remote branches do not prove unmerged changes.

## Priority leads

- [collaborative-intelligence PR #14](https://github.com/froekjaer/collaborative-intelligence/pull/14) — V2 foundations; content not yet reviewed.
- [collaborative-intelligence PR #13](https://github.com/froekjaer/collaborative-intelligence/pull/13) — cross-model review; content not yet reviewed.
- [mission-framework PR #11](https://github.com/froekjaer/mission-framework/pull/11) — hybrid intelligence corpus; content not yet reviewed.
- [Mission-Platform PR #7](https://github.com/froekjaer/Mission-Platform/pull/7) — ADR index and published-content concerns; content not yet reviewed.
- [-Publication-Pipeline PR #5](https://github.com/froekjaer/-Publication-Pipeline/pull/5) — integrated presentation; content not yet reviewed.
- [timelapse-pro PR #248](https://github.com/froekjaer/timelapse-pro/pull/248) — GRC consolidation; content not yet reviewed.
- [timelapse-pro PR #310](https://github.com/froekjaer/timelapse-pro/pull/310) — connectivity; content not yet reviewed.
- [mission-resilience PR #1](https://github.com/froekjaer/mission-resilience/pull/1) — cloud architecture; content not yet reviewed.

## Next checks

Paginate TimeLapse Pro branches; enumerate remaining repositories; fetch closed/merged PRs; compare branches against main for unique commits and changed files; inspect local worktrees, stashes and untracked files only with authorized host access. The PR 310 head branch did not appear on the first branch page; this does not prove deletion.
