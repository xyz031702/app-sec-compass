# RMIT Part A Overview - AppSec Mapping

## Control 1.1
**Type:** S (Standard)
**Requirement:** Financial institutions must invest in expertise and risk controls to prevent operational disruptions, achieve highest security against digital crimes, maintain oversight over third parties, build cyber resilience, and practice ethical technology use.

### AppSec Mapping

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| SAST | Static analysis tools, Static analysis tools | Identify code vulnerabilities |
| DAST | Dynamic testing tools | Test running applications |
| SCA | Composition analysis tools, Dependabot | Manage third-party library risks |
| SBOM | CycloneDX, SPDX | Track software components |
| DevSecOps | CI/CD security gates | Automate security controls |
| Secure Coding Training | Secure Code Warrior, OWASP WebGoat | Build internal expertise |
| Maturity Assessment | BSIMM15, OWASP SAMM | Assess AppSec program maturity |

**Notes:** High-level requirement; specific tools depend on detailed controls in Part B.

---

## Control 1.2
**Type:** S (Standard)
**Requirement:** Policy sets minimum requirements for technology risk management including cyber risk. Controls must be proportionate to size, complexity, and technology exposure.

### AppSec Mapping

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| Threat Modeling | STRIDE, PASTA | Risk-based security assessment |
| DevSecOps | Risk-based pipeline gates | Proportionate controls based on risk |
| Maturity Assessment | BSIMM15 | Benchmark against industry peers |

**Notes:** Emphasizes proportionality - smaller institutions may use lighter tooling.

---

## Control 1.3-1.4
**Type:** S (Standard)
**Requirement:** Enforcement actions for non-compliance; Bank may require external review and remediation.

### AppSec Mapping

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| Maturity Assessment | BSIMM15, OWASP SAMM | Independent maturity assessment |
| DevSecOps | Remediation tracking | Manage remediation plans |

**Notes:** Governance controls - AppSec assessments support compliance evidence.

---

## Controls 2.1 - 7.1 (Applicability, Legal, Definitions)
**Type:** S (Standard)

### AppSec Mapping

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| SBOM | Asset inventory | Track "critical systems" and components |

**Notes:** Mostly administrative controls. SBOM helps with system classification defined in 5.2.
