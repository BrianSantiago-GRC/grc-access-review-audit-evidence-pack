# Access Review Table (Sample Data)

| User ID | Department | Role | Access Granted | Access Needed? (Y/N) | Reviewer Decision (Keep/Modify/Remove) | Evidence Ref | Notes |
|---|---|---|---|---|---|---|---|
| U-001 | Finance | AP Specialist | ERP_AP_ReadWrite | Y | Keep | EV-001 | Access aligns to current role |
| U-002 | Finance | Contractor | ERP_GL_Admin | N | Remove | EV-002 | Excessive access for temporary role |
| U-003 | HR | HR Coordinator | HRIS_ReadWrite | Y | Keep | EV-003 | Required for onboarding tasks |
| U-004 | IT | Help Desk | M365_User_Admin | Y | Keep | EV-004 | Needed for account support |
| U-005 | Sales | Sales Rep | CRM_Admin | N | Modify | EV-005 | Downgrade to standard user |
| U-006 | Operations | Ops Analyst | BI_ReadOnly | Y | Keep | EV-006 | Appropriate least-privilege access |
| U-007 | Legal | Paralegal | DMS_ReadWrite | Y | Keep | EV-007 | Role-based requirement |
| U-008 | Marketing | Intern | SharedDrive_All | N | Remove | EV-008 | Over-permissioned intern account |
| U-009 | IT | SysAdmin | Server_LocalAdmin | Y | Keep | EV-009 | Admin privilege justified |
| U-010 | Compliance | Analyst | GRC_Tool_Editor | Y | Keep | EV-010 | Required for control updates |
| U-011 | Finance | Analyst | Payroll_Admin | N | Remove | EV-011 | Access not required by function |
| U-012 | Customer Support | Agent | Ticketing_Supervisor | N | Modify | EV-012 | Reduce to agent permissions |
| U-013 | IT | IAM Support | Entra_RoleMgmt_Read | Y | Keep | EV-013 | Needed for review workflows |
| U-014 | Procurement | Buyer | ERP_PO_ReadWrite | Y | Keep | EV-014 | Role-aligned access |
| U-015 | Executive | EA | Calendar_Delegate_All | Y | Keep | EV-015 | Approved business need |
