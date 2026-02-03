# RMIT Chapter 8: Governance - AppSec Mapping

## Control 8.1
**Type:** S (Standard)
**Requirement:** Board must establish and approve technology risk appetite, including risk tolerances, risk owners, key risk indicators, resource deployment, and regular reviews.

### AppSec Mapping

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| Maturity Assessment | BSIMM15 metrics | Track AppSec KRIs against tolerance |
| DevSecOps | Security metrics dashboards | Report vulnerability trends |

**Notes:** Governance control - AppSec tools provide data for board-level risk reporting.

---

## Control 8.2
**Type:** S (Standard)
**Requirement:** Board must approve IT/cybersecurity strategic plans (3+ years), oversee TRMF and CRF implementation, ensure robust risk assessments for critical IT systems, review policies every 3 years.

### AppSec Mapping

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| SAST/DAST | Continuous scanning | Demonstrate ongoing risk assessment |
| SCA | Dependency scanning | Track third-party component risks |
| Maturity Assessment | BSIMM15, OWASP SAMM | Strategic AppSec program assessment |

**Notes:** Strategic planning control - maturity assessments inform strategic roadmaps.

---

## Control 8.3-8.4
**Type:** S (Standard)
**Requirement:** Board-level committee with technology experience; regular updates on technology risk and cyber threats; board cybersecurity training.

### AppSec Mapping

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| DevSecOps | Executive security dashboards | Board-friendly AppSec reporting |

**Notes:** Governance structure control - limited direct AppSec tooling.

---

## Control 8.5
**Type:** S (Standard)
**Requirement:** Board Audit Committee (BAC) must ensure effective internal technology audit function and timely closure of corrective actions.

### AppSec Mapping

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| SAST/DAST | Audit trail of scan results | Evidence for audits |
| DevSecOps | Defect tracking (Jira) | Track corrective action closure |

**Notes:** Audit-focused control - AppSec tools provide audit evidence.

---

## Control 8.6-8.7
**Type:** S (Standard)
**Requirement:** Senior management day-to-day risk management; cross-functional committee for technology oversight.

### AppSec Mapping

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| SCA | Vulnerability age tracking | Report on patch deployment |
| SBOM | Component inventory | Track technology obsolescence |
| DevSecOps | Security posture dashboards | Cross-functional visibility |

**Notes:** Operational management control - AppSec dashboards support committee reporting.
