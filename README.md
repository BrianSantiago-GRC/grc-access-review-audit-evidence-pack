# Access Review and Audit Evidence Pack

**A synthetic 15-record access-review exercise showing decisions, exceptions, remediation ownership, and evidence traceability.**

## Problem, Action, Result

**Problem:** An access review is difficult to audit when decisions, exceptions, owners, due dates, and validation evidence are scattered.

**Action:** I reviewed 15 synthetic access records, documented `Keep`, `Modify`, or `Remove` decisions, logged exceptions, assigned remediation actions, and mapped the workflow to access-control concepts.

**Result:** The pack contains 10 `Keep`, 2 `Modify`, and 3 `Remove` decisions with a clear path from review to finding to remediation. It demonstrates process design and documentation, not authority over a live audit or identity system.

## 90-Second Review

1. Open the [`access-review table`](ACCESS_REVIEW_TABLE.md).
2. Compare the [`exception log`](EXCEPTION_LOG.md) with the [`remediation tracker`](REMEDIATION_TRACKER.md).
3. Read the [`findings summary`](FINDINGS.md).
4. Use the [`evidence request list`](AUDIT_EVIDENCE_REQUEST_LIST.md) to see how proof would be gathered.

## Evidence Map

| Artifact | Reviewer takeaway |
|---|---|
| `ACCESS_REVIEW_TABLE.md` | Record-level decisions and rationale |
| `EXCEPTION_LOG.md` | Risk, owner, and follow-up visibility |
| `REMEDIATION_TRACKER.md` | Due dates and validation method |
| `AUDIT_EVIDENCE_REQUEST_LIST.md` | Traceable evidence requests |
| `screenshots/` | Rendered previews generated from the Markdown artifacts |

## Scope Boundary

Every person, role, system, decision, and screenshot in this repository is synthetic portfolio data. The images are rendered documentation previews, not exports from Entra, an IAM platform, or an audit application.
