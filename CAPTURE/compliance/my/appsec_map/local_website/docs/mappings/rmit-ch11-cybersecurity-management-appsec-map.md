# RMIT Chapter 11: Cybersecurity Management - AppSec Mapping

## Control 11.1
**Type:** S (Standard)
**Requirement:** Enterprise-wide focus on effective cyber risk management.

### AppSec Mapping

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| Security Champions | Champion program | Embed security in dev teams |

**Notes:** Organizational control - Security Champions bridge business and technology.

---

## Control 11.2
**Type:** S (Standard)
**Requirement:** Develop CRF with IPDRR (Identify, Protect, Detect, Respond, Recover).

### AppSec Mapping

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| SBOM | CycloneDX, SPDX | **Identify** - application asset inventory |
| SAST | Static analysis tools | **Protect** - secure code |
| SCA | Composition analysis tools | **Protect** - secure dependencies |
| DAST | Dynamic testing tools | **Detect** - find runtime vulnerabilities |

**Notes:** AppSec covers Identify, Protect, Detect phases only. Respond/Recover is operational.

---

## Control 11.3
**Type:** S (Standard)
**Requirement:** CRF elements including asset classification, threat identification, defense-in-depth, continuous monitoring.

### AppSec Mapping

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| Threat Modeling | STRIDE, PASTA | (a) Application risk context |
| SBOM | CycloneDX, Dependency-Track | (b)(h) Asset inventory |
| SAST | Static analysis tools | (c) Code vulnerability identification |
| DAST | Dynamic testing tools | (c) Runtime vulnerability detection |
| SCA | Composition analysis tools | (c) Third-party vulnerabilities |
| DevSecOps | Continuous scanning | (e)(g) Continuous monitoring |

**Notes:** Zero-trust, micro-segmentation, network defense are NOT AppSec - those are network/infrastructure.

---

## Control 11.4
**Type:** S (Standard)
**Requirement:** NCII compliance.

### AppSec Mapping
**None.** Regulatory compliance control.

---

## Control 11.5
**Type:** S (Standard)
**Requirement:** Adopt Appendix 5 controls.

### AppSec Mapping
*Only Part E (API Security) and Part D (VAPT for applications) are AppSec. See appendix-05 mapping.*

---

## Control 11.6
**Type:** S (Standard)
**Requirement:** Red Team simulation every 3 years.

### AppSec Mapping

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| Application Pentest | Web/mobile/API penetration testing | Application-layer red team |

**Notes:** Full red team includes network/infrastructure. Only application pentesting is AppSec.

---

## Control 11.7
**Type:** G (Guideline)
**Requirement:** May implement bug bounty programs.

### AppSec Mapping

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| Bug Bounty | HackerOne, Bugcrowd | Crowdsourced application testing |

---

## Control 11.8
**Type:** S (Standard)
**Requirement:** Mitigations for cyber-attack lifecycle (kill chain).

### AppSec Mapping

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| SAST | Code security | **Exploitation** - prevent exploitable code |
| SCA | Vulnerability management | **Exploitation** - patch dependencies |
| Secret Detection | Secret scanning tools | **Exfiltration** - prevent credential exposure |

**Notes:** Most kill chain phases (recon, delivery, C2) are network/endpoint security, NOT AppSec.

---

## Control 11.9
**Type:** S (Standard)
**Requirement:** Continuous monitoring and SOC.

### AppSec Mapping

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| DevSecOps | Continuous scanning | Automated vulnerability detection |

**Notes:** SOC operations is NOT AppSec. AppSec tools feed findings to SOC, but SOC itself is operational security.
