# RMIT Chapter 13: Technology Audits - AppSec Mapping

## Control 13.1
**Type:** S (Standard)
**Requirement:** Scope, frequency, and intensity of technology audits must be commensurate with complexity, sophistication, and criticality of technology systems.

### AppSec Mapping

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| SAST | Audit-ready scan reports | Evidence for audits |
| DAST | Historical vulnerability reports | Audit trail |
| SCA | Dependency audit reports | Third-party component audit |
| Maturity Assessment | BSIMM15 | Independent program assessment |

**Notes:** AppSec tools provide audit evidence with timestamps and remediation tracking.

---

## Control 13.2
**Type:** S (Standard)
**Requirement:** Annual review of technology audit plan covering: critical technology services, third-party service providers, external system interfaces, delayed/terminated projects, post-implementation reviews.

### AppSec Mapping

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| SCA | Third-party component inventory | Audit third-party dependencies |
| SBOM | Supply chain documentation | Audit external interfaces |
| SAST/DAST | Post-deployment scans | Post-implementation security review |
| DevSecOps | Security gate results | Audit project security compliance |

---

## Control 13.3
**Type:** S (Standard)
**Requirement:** Internal audit function must have dedicated, certified technology audit resources conversant with the institution's technology systems and delivery channels.

### AppSec Mapping

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| Secure Coding Training | Tool training for auditors | Audit team AppSec competency |
| Maturity Assessment | BSIMM15, OWASP SAMM | Framework knowledge |

**Notes:** Auditors need training on AppSec tools and concepts. **Relevant certifications:** CSSLP, CASE.

---

## Control 13.4
**Type:** G (Guideline)
**Requirement:** Technology audit resources may advise on compliance during planning/development phases, but must consider independence for post-implementation reviews.

### AppSec Mapping

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| Threat Modeling | Design review participation | Audit input during planning |
| DevSecOps | Security gate reviews | Audit advisory during development |

**Notes:** Separate advisory and assurance roles.
