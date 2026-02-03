# RMIT Chapter 12: Digital Services - AppSec Mapping

## Control 12.1
**Type:** S (Standard)
**Requirement:** Robust security controls for digital services.

### AppSec Mapping

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| SAST | Static analysis tools | Secure code for digital services |
| DAST | Dynamic testing tools | Test running applications |
| IAST | Interactive testing tools | Runtime testing |
| API Security Testing | API security testing tools, API security testing tools | Test authentication/authorization |
| Secret Detection | Secret scanning tools | Prevent credential exposure |

**ROI Notes:** Physical controls = NOT AppSec. Refer to Appendices 2, 3, 4.

---

## Control 12.2
**Type:** S (Standard)
**Requirement:** Document alternative controls if not yet implemented.

### AppSec Mapping

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| Threat Modeling | Risk acceptance process | Document alternatives |

---

## Control 12.3
**Type:** S (Standard)
**Requirement:** Enhance CRF for digital fraud including mobile app security.

### AppSec Mapping

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| Mobile SAST | Static analysis tools Mobile | (b) Secure mobile app code |
| Mobile DAST | Mobile security testing tools | (b)(c) Test mobile app security |
| Mobile App Shielding | App shielding tools | (b) Runtime protection |

**ROI Notes:**
- (a) Customer device threats - NOT AppSec (endpoint security)
- (d-g) Incident handling, management review - NOT AppSec (operations)

---

## Control 12.4
**Type:** S (Standard)
**Requirement:** Fraud detection capabilities.

### AppSec Mapping
**NOT AppSec.** Fraud detection is operational analytics. Use commercial fraud platforms (FICO, SAS).

---

## Control 12.5-12.7
**Type:** S (Standard)
**Requirement:** Secure communication, customer awareness.

### AppSec Mapping
**NOT AppSec.** Customer communication and awareness programs are operational.

---

## Control 12.8
**Type:** S (Standard)
**Requirement:** Self-service kill switch for account suspension.

### AppSec Mapping

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| SAST/DAST | Test kill switch code | Security testing of feature |
| API Security Testing | Test account APIs | Secure API implementation |

---

## Control 12.9
**Type:** S (Standard)
**Requirement:** Heightened monitoring after incidents, credential revocation.

### AppSec Mapping

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| Secret Detection | Credential management | (c) Secure credential revocation code |

**ROI Notes:** (a) Account monitoring, (b) customer notification - NOT AppSec (operations).
