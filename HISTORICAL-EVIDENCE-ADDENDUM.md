# Historical Evidence and Methodology Addendum

**Status: documentation integrity review (November 2026).**

This addendum qualifies the [original four-page PDF report](blockzag-wordpress-audit.pdf). It does **not** supersede the original report, independently verify its historical claims, or assert that the former website is operational today.

## Important timeline clarification

The PDF states that Blockzag.com was **decommissioned in 2024**, while also listing **"Project Completed — June 2025"**. Those dates can describe a retrospective report written after the website ceased operation, but the report does **not** establish exactly when each security-control change, test or observation occurred. Consequently:

- Treat June 2025 as the **reported document/project completion date**, not proof of live testing in June 2025.
- The underlying site's configuration and findings are historical and should **not** be interpreted as current.
- Exact control-implementation dates, system state, and contemporaneous records remain **unverified**.

## Claims requiring underlying evidence

| PDF statement | Evidence that would be needed | Current verification status |
|---|---|---|
| Four outdated plugins removed | Historical plugin inventory, version history, dated removal/change records | Not independently verified |
| 2FA, firewall, brute-force rules and SSL enforced | Dated configuration exports, screenshots, change records, test outputs | Not independently verified |
| WPScan / Security Ninja checks performed | Dated scope, scan output, tool versions, authorization records | Not independently verified |
| Staging restore test completed | Dated backup job, restore procedure, restoration logs and acceptance test | Not independently verified |
| **15% GTmetrix performance improvement** | Before/after performance measurements with comparable test conditions | **Unsupported by attached measurement data** |
| "Passed all critical checks" on SecurityHeaders.com | Dated scanner results, applicable criteria, and scope | Not independently verified |
| Brute-force attempt mitigated within 48 hours | Security event logs, triage ticket, control response evidence and timestamps | Not independently verified |

**Interpretation:** The PDF is a retrospective author account, not an independently attested audit. Absence of supporting files in this repository does not prove that work did not occur; it does mean readers cannot validate the claimed outcomes here.

## Technical distinctions and limitations

- **Changing the WordPress login URL is not a primary authentication control.** It may reduce automated noise, but strong MFA, least privilege, patching and rate limiting are more meaningful security measures.
- **Updating/removing plugins is only one aspect of vulnerability management.** A defensible review also considers core/theme versions, supported dependencies, security updates, and time-bounded exposure.
- **HTTPS configuration is not equivalent to comprehensive application security.** Certificate and transport checks do not establish the security of the entire platform.
- **Backups are not proven recoverable solely because a scheduled job exists.** Restoration requires validation of data integrity and operational recovery.
- **The report does not quantify security risk reduction.** Performance improvement and security effectiveness are distinct measures.

## Specific ambiguities in the original PDF

- **Plugin count (page 2):** The report states that four outdated plugins were removed, but explicitly names only three: Slider Revolution, Contact Form 7, and Insert Headers and Footers. The fourth plugin, exact versions, removal dates and related CVEs are **not identified** in the PDF. This is a traceability gap, not proof that the count is false.
- **Login-attempt limit (page 2):** The PDF says login attempts were limited to three via `.htaccess`, but it does not identify the Apache module, rate-limit rule, or WordPress plugin setting that implemented and enforced a three-*failed-login* threshold. An ordinary `.htaccess` rule does not by itself demonstrate application-aware login-failure counting. The mechanism and a dated negative test remain **unverified**. See [WordPress brute-force guidance](https://developer.wordpress.org/advanced-administration/security/brute-force/) and [Wordfence brute-force settings](https://www.wordfence.com/help/firewall/brute-force/).
- **How to resolve:** Where authorized historical records exist, identify the fourth plugin and versions, attach redacted plugin/change logs, and name the responsible login-protection control with a dated configuration and test result. Otherwise present both as reported and unverified. Do not silently change the original PDF.

## Recommended verification if historical records are available

1. Establish a timeline: website operation, security activities, decommissioning, and report-authoring dates.
2. Attach appropriately redacted historical artifacts and dates, with permission and no secrets or customer records.
3. Separate **Observed**, **Reported**, **Inferred**, and **Not verified** statements.
4. Clarify any unsupported figures or remove them from promotional summaries.
5. Preserve the original PDF as a record of what was written, with versioned corrections rather than silent revision.

**Portfolio objective:** Demonstrate willingness to scrutinize evidence quality, document uncertainty, and avoid overstating conclusions—core professional habits for GRC and IT audit roles.
