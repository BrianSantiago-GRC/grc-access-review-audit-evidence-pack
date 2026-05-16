# Findings - GRC Access Review and Audit Evidence Pack

Date: 2026-05-15  
Reviewer role context: Junior cybersecurity/GRC portfolio simulation (sanitized sample data)

## Scope Reviewed

- Total accounts reviewed: 15
- Keep decisions: 10
- Modify decisions: 2
- Remove decisions: 3

## Key Findings

1. **Excessive access exists in non-admin roles.**  
   Contractor and intern accounts had broad permissions not aligned to role requirements.

2. **Least-privilege gaps were identified and reduced.**  
   Two accounts required permission downgrades instead of full removal (CRM admin and ticketing supervisor roles).

3. **Administrative access is mostly justified with role context.**  
   Admin-level permissions were retained only where there was a documented business need.

4. **Evidence traceability was maintained for each decision.**  
   Each user decision maps to an evidence reference (`EV-001` through `EV-015`) for audit-readiness.

## Risk Summary

- Primary risk observed: Over-permissioned access in temporary or non-privileged roles.
- Operational impact if not remediated: Increased unauthorized access risk, control failure during audits, and delayed incident response.
- Current remediation posture: Immediate reduction/removal actions logged in `REMEDIATION_TRACKER.md`.

## Recommendations

- Enforce role-based access review every 30-90 days for sensitive systems.
- Require documented business justification for admin-level privileges.
- Time-box temporary and contractor access with automatic expiry where possible.
- Track all access changes with ticket/evidence references and reviewer notes.

## Control Mapping (Portfolio-Level)

- **NIST CSF PR.AC-1 / PR.AC-4:** Identities and permissions are managed and reviewed.
- **NIST CSF DE.CM-1:** Access and activity evidence supports monitoring and review.
- **HIPAA 164.308(a)(4) - Information Access Management:** Access authorization and role appropriateness reviewed.

