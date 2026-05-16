# Exception Log - Access Review

Date: 2026-05-15  
Purpose: Track non-standard or non-compliant access outcomes identified during review.

| Exception ID | User ID | Department | Access Issue | Decision | Business Risk | Required Action | Target Date | Evidence Ref | Status |
|---|---|---|---|---|---|---|---|---|---|
| EX-001 | U-002 | Finance (Contractor) | Contractor had `ERP_GL_Admin` access | Remove | Unauthorized financial data/admin exposure | Remove admin access and validate contractor scope | 2026-05-19 | EV-002 | Open |
| EX-002 | U-005 | Sales | Sales role had `CRM_Admin` instead of standard access | Modify | Unnecessary privilege elevation in customer data platform | Downgrade to standard CRM role | 2026-05-19 | EV-005 | Open |
| EX-003 | U-008 | Marketing (Intern) | Intern had broad `SharedDrive_All` access | Remove | Excessive access to cross-functional sensitive files | Remove broad access and regrant least privilege | 2026-05-19 | EV-008 | Open |
| EX-004 | U-011 | Finance | Analyst had `Payroll_Admin` access | Remove | Payroll confidentiality/integrity risk | Remove payroll admin and verify no dependency | 2026-05-19 | EV-011 | Open |
| EX-005 | U-012 | Customer Support | Agent had `Ticketing_Supervisor` access | Modify | Access beyond role need, potential case control misuse | Downgrade to agent-level permissions | 2026-05-19 | EV-012 | Open |

## Reviewer Notes

- All exceptions are tied to access reduction or removal to align with least-privilege.
- No exception in this log should be closed without evidence of implemented permission changes.

