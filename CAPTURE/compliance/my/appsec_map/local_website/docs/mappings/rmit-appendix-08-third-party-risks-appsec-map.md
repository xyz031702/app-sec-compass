# RMIT Appendix 8: IT and Cyber Risks Associated with Third Party Service Providers - AppSec Mapping

## Overview
Third-party risk management is primarily vendor management and governance. AppSec applies only to **software supply chain** aspects.

---

## Control 1 - Operational Performance and Capacity
**NOT AppSec.** Vendor operational assessment.

---

## Control 2 - Security Requirements

| Sub-control | AppSec? | Owner |
|-------------|---------|-------|
| 2(a) Security governance | NO | Vendor management |
| 2(b) IT asset management | NO | Vendor management |
| 2(c) Secure SDLC | **YES** | AppSec - assess vendor's secure development |
| 2(d) Physical security | NO | Vendor management |
| 2(e) Personnel security | NO | HR/Vendor management |
| 2(f) Access management | NO | Vendor management |
| 2(g) Incident management | NO | Vendor management |

### Control 2(c) - Secure SDLC

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| Maturity Assessment | BSIMM15, OWASP SAMM | Assess vendor's AppSec maturity |
| SCA | SBOM review | Review vendor dependencies |

---

## Control 3 - Cyber Supply Chain Risks

| Sub-control | AppSec? | Owner |
|-------------|---------|-------|
| 3(a) Personnel vetting | NO | HR |
| 3(b) Third-party/OSS vetting | **YES** | AppSec - software supply chain |
| 3(c) Sub-contractor management | **YES** | AppSec - Nth party dependencies |
| 3(d) Concentration/geopolitical | NO | Risk management |

### Control 3(b) - Third-Party/Open Source Software Vetting

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| SCA | Composition analysis tools | Scan third-party components |
| SBOM | CycloneDX, SPDX | Request vendor SBOM |
| SLSA | Supply chain verification | Verify software provenance |
| Supply Chain MAP | Maturity assessment | Assess vendor supply chain maturity |

### Control 3(c) - Sub-Contractor/Nth Party Risk

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| SBOM | Transitive dependency analysis | Track Nth party dependencies |
| Supply Chain MAP | Extended supply chain assessment | Assess sub-contractor risks |

---

## Appendix 9: Emerging Technologies

### Controls 1-2
**Partial AppSec.** Only relevant for:
- Security testing of AI/ML models you build
- Threat modeling for emerging tech applications

**NOT AppSec:**
- AI ethics/fairness (governance)
- Regulatory compliance
- Vendor AI risk assessment

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| Threat Modeling | Emerging tech threat modeling | Identify application risks |
| SAST/DAST | Security testing | Test YOUR emerging tech code |

---

## Summary

This appendix has **limited AppSec relevance**:
- Control 2(c): Vendor secure SDLC assessment
- Control 3(b): OSS/third-party software scanning
- Control 3(c): Transitive dependency analysis

Everything else is vendor management, not AppSec.
