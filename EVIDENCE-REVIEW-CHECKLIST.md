# Historical Evidence Review Checklist — Blockzag

> **Documentation aid only.** This checklist is for a potential retrospective review of the [original PDF](blockzag-wordpress-audit.pdf) and the [historical evidence addendum](HISTORICAL-EVIDENCE-ADDENDUM.md). It is **not** proof that any historical control, test, or mitigation happened. The site is reported as decommissioned; no active scanning or website access is requested.

## Evidence acceptance rules

For each claim, record the **event date**, **artifact creation date**, **source/custodian**, **scope**, and **reviewer**. Redact sensitive records before publication. Separate self-reported work from independently reproducible evidence. Do not publish secrets, access tokens, real user details, IP addresses requiring confidentiality, or client records.

| Claim to investigate | Potential historical artifact | Review question | Status |
| --- | --- | --- | --- |
| Four plugins removed (PDF names three) | Dated plugin inventory, versions and removal/change tickets | Which fourth plugin was removed, and when? | Count and inventory not independently verified |
| MFA, firewall and login protections | Redacted settings export / dated test record | Was the control enabled for the stated accounts and dates? | Not independently verified |
| Three-attempt login restriction attributed to `.htaccess` | Apache module/rule configuration or Wordfence settings and dated failed-login test | Which component actually enforced three failures, and was it tested? | Mechanism and enforcement not independently verified |
| HTTPS/TLS | Dated certificate and configuration checks | What hostname, time and TLS settings were assessed? | Not independently verified |
| WPScan / Security Ninja performed | Authorized scope and dated scanner outputs | Are tool versions, findings and limitations recorded? | Not independently verified |
| Restore test | Dated restore logs and acceptance criteria | Was recovery tested and data integrity checked? | Not independently verified |
| 15% performance improvement | Comparable before/after GTmetrix reports | Same test configuration, location and measurement conditions? | Unsupported by attached measurements |
| Critical header checks passed | Dated SecurityHeaders.com output | Which headers and criteria were included? | Not independently verified |
| Brute-force event mitigated in 48 hours | Redacted event logs and response ticket | Do timestamps support detection, response and resolution? | Not independently verified |

## Traceability template

For any future evidence that is **lawfully available for publication**, make a separate review record with: Claim ID; exact PDF page; reported event date; artifact name and SHA-256; collection date; origin/custodian; redaction notes; independent verification performed; limitations; reviewer; conclusion (**Observed**, **Reported**, **Inferred**, or **Not verified**).

Do not treat missing source records as evidence that a control was absent or ineffective. Preserve the original PDF as-is; document any corrections in versioned addenda.

## Portfolio interview explanation

"The report describes a historical website security effort. I separately documented where source evidence is missing, what would be necessary to validate each claim, and why a retrospective statement is not the same as an independently verified security assessment."
