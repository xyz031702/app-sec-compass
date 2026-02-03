# RMIT Chapter 10: Technology Operations Management - AppSec Mapping

## Control 10.1
**Type:** S (Standard)
**Requirement:** Establish appropriate governance for technology projects with risk assessments throughout the project lifecycle.

### AppSec Mapping

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| Threat Modeling | STRIDE, PASTA | Project security risk assessment |
| DevSecOps | Shift-left security | Security in SDLC from start |

---

## Control 10.2
**Type:** S (Standard)
**Requirement:** Risk assessments for: (a) resources, (b) system complexity, (c) security controls throughout lifecycle, (d) user requirements, (e) testing strategies, (f) deployment strategies, (g) disaster recovery.

### AppSec Mapping

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| SAST | Static analysis tools | (c)(e) Security in development, code testing |
| DAST | Dynamic testing tools | (c)(e) Runtime testing |
| IAST | Interactive testing tools | (c)(e) Combined testing |
| SCA | Composition analysis tools | (b)(c) Third-party component risks |
| Secret Detection | Secret scanning tools | (c) Prevent credential exposure |
| DevSecOps | CI/CD security gates | (c) Security throughout lifecycle |
| Container Security | Container scanning tools | (c)(f) Secure container deployment |
| IaC Security | IaC scanning tools | (c) Infrastructure security code |

**ROI Notes:**
- (a) Resource adequacy - NOT AppSec (project management)
- (d) User requirements - NOT AppSec (business analysis)
- (f) Fallback strategies - NOT AppSec (operations)
- (g) Disaster recovery - NOT AppSec (infrastructure/BCM)

---

## Control 10.3
**Type:** S (Standard)
**Requirement:** Board and senior management receive timely reports on risk management.

### AppSec Mapping

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| DevSecOps | Security metrics dashboards | Project security status reporting |

**Notes:** Executive reporting is governance. AppSec provides the data.
