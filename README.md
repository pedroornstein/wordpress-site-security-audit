# WordPress Security Review · Blockzag

**Pedro Ornstein** · Historical security reporting and evidence review

This portfolio project documents reported hardening work on a WordPress site I previously owned and managed. It covers plugin maintenance, privileged authentication, transport security, backups, and recovery.

> The report says the site was decommissioned in 2024 and lists June 2025 as the project completion date. Individual testing and implementation dates remain unverified. The PDF records the author's retrospective account.

## Review the work

| Artifact | What it shows |
| --- | --- |
| [Historical evidence and methodology addendum](HISTORICAL-EVIDENCE-ADDENDUM.md) | Start here for the timeline, technical qualifications, and verification limits. |
| [Original security report (PDF)](blockzag-wordpress-audit.pdf) | The original four-page report, including the reported changes and results. |
| [Evidence review checklist](EVIDENCE-REVIEW-CHECKLIST.md) | The source records and review questions needed to substantiate each historical claim. |

## Examples of evidence judgment

| Reported claim | What a reviewer can establish from this repository |
| --- | --- |
| Four plugins were removed | Page 2 names three. The full inventory and removal dates would require dated change records. |
| A staging restore test was documented | The report describes a restore test. A dated restore log and acceptance criteria would support a recoverability conclusion. |
| Performance improved by 15% | The PDF reports the figure. Verification would require comparable before-and-after measurements. |

The repository documents historical claims and their evidence limits. Its materials provide no current security assessment or authorization for testing.

## Automated document integrity check

Run `python scripts/validate_docs.py` with Python 3.10+ from the repository root. The [documentation workflow](.github/workflows/docs-quality.yml) checks local Markdown links and compares the PDF against its recorded SHA-256 baseline. These checks detect document changes and broken links. Historical claims require the evidence described in the addendum.

## Related work

[RouteShield GRC case study](https://github.com/pedroornstein/grc-cybersecurity-portfolio) · Simulated enterprise risk, vendor due diligence, remediation planning, and a reproducible control test.
