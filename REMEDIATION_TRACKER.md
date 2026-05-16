# Remediation Tracker - Access Review

Date created: 2026-05-15  
Objective: Track required access reductions/removals and evidence of completion.

| Task ID | User ID | Required Change | Priority | Owner | Due Date | Validation Method | Evidence to Attach | Status |
|---|---|---|---|---|---|---|---|---|
| RT-001 | U-002 | Remove `ERP_GL_Admin` | High | IAM Support | 2026-05-19 | Permission export before/after + reviewer check | Change ticket ID, screenshot, updated access table | Open |
| RT-002 | U-005 | Modify `CRM_Admin` to standard CRM role | Medium | IAM Support | 2026-05-19 | Role membership verification in CRM admin panel | Role change screenshot + reviewer note | Open |
| RT-003 | U-008 | Remove `SharedDrive_All` and apply scoped access | High | IT Support | 2026-05-19 | Shared drive ACL check before/after | ACL screenshot + access request reference | Open |
| RT-004 | U-011 | Remove `Payroll_Admin` | High | IAM Support | 2026-05-19 | Payroll role assignment check after removal | Role removal screenshot + approval note | Open |
| RT-005 | U-012 | Modify `Ticketing_Supervisor` to `Ticketing_Agent` | Medium | IT Support | 2026-05-19 | Ticketing role audit report | Role update screenshot + verification note | Open |

## Completion Criteria

- Access is reduced or removed as defined above.
- Before/after evidence is captured and sanitized.
- Exception entries in `EXCEPTION_LOG.md` are updated to `Closed`.
- Access review table is updated to reflect final state.

