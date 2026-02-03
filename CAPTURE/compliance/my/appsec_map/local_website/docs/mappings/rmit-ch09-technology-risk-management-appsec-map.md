# RMIT Chapter 9: Technology Risk Management - AppSec Mapping

## Control 9.1
**Type:** S (Standard)
**Requirement:** TRMF must be an integral part of the enterprise risk management framework (ERM).

### AppSec Mapping

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| Maturity Assessment | BSIMM15 | Integrate AppSec into ERM |
| DevSecOps | GRC platform integration | Feed AppSec findings into ERM |

---

## Control 9.2
**Type:** S (Standard)
**Requirement:** TRMF must include: (a) clear technology risk definition, (b) responsibilities across levels, (c) identification of technology risks including emerging tech, (d) risk classification of information assets, (e) risk measurement approaches, (f) risk controls, (g) continuous monitoring, (h) effective information system for risk profile, (i) key resources and third-party dependencies, (j) scenario analysis, (k) incident management policies.

### AppSec Mapping

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| SBOM | CycloneDX, SPDX, Dependency-Track | (d)(i) Asset classification, track dependencies |
| SCA | Composition analysis tools | (c)(f) Identify third-party component risks |
| SAST | Static analysis tools | (e)(f) Risk measurement via severity scoring |
| DAST | Dynamic testing tools | (f)(g) Risk controls validation, continuous testing |
| Threat Modeling | STRIDE, PASTA | (c)(j) Emerging tech risk, scenario analysis |
| DevSecOps | Pipeline security gates | (f)(g) Automated controls, continuous monitoring |
| Container Security | Container scanning tools | (d) Container/image classification |

**Notes:** Core TRMF control - multiple AppSec tools map to specific sub-requirements.

---

## Control 9.3
**Type:** S (Standard)
**Requirement:** Establish independent enterprise-wide technology risk management function responsible for implementing TRMF/CRF, advising on critical projects, and providing independent views on third-party assessments.

### AppSec Mapping

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| SCA | Third-party risk scoring | Independent assessment of vendor components |
| Maturity Assessment | BSIMM15, Supply Chain MAP | Third-party security assessments |
| DevSecOps | Centralized security platform | Enterprise-wide visibility |

---

## Control 9.4-9.5
**Type:** S (Standard)
**Requirement:** Designate CISO with sufficient authority, independence, and resources. CISO must have technical skills, be appropriately certified, and advise on technology risk.

### AppSec Mapping

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| DevSecOps | CISO dashboard | Holistic AppSec visibility |
| Maturity Assessment | BSIMM15 | Program assessment for CISO reporting |

**Notes:** Role-based control - CISO requires visibility across all AppSec tools.
