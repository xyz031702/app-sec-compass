# RMIT Appendix 4: Control Measures for Mobile Applications and Devices - AppSec Mapping

## Control 1 - Mobile Application Risk Assessment
**Type:** S (Standard)
**Requirement:** Continuously assess and perform risk assessment for mobile application threats.

### AppSec Mapping

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| Threat Modeling | Mobile threat modeling (STRIDE) | Identify mobile-specific threats |
| Mobile SAST | Checkmarx, Fortify Mobile | Continuous code analysis |
| Mobile DAST | NowSecure, MobSF | Runtime vulnerability testing |
| SCA | Mobile dependency scanning | Third-party library risks |
| Maturity Assessment | OWASP SAMM (mobile) | Assess mobile AppSec maturity |

**Notes:** Use OWASP MASVS and MSTG for mobile security testing.

---

## Control 2 - Mobile Application Security
**Type:** S (Standard)

### Control 2(a) - Secure Tamper-Proof Environment

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| Mobile App Shielding | Promon, Guardsquare DexGuard | Runtime protection |
| Mobile SAST | Root/jailbreak detection analysis | Verify detection code |
| Mobile DAST | Tamper resistance testing | Test anti-tampering |
| RASP | Runtime self-protection | Detect compromised environment |

---

### Control 2(b) - No Local Storage of Authentication Credentials

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| Mobile SAST | Data storage analysis | Detect credential storage |
| Mobile DAST | Data extraction testing | Verify no credentials stored |

**Notes:** OWASP MASVS MSTG-STORAGE requirements.

---

### Control 2(c) - Robust Activation Authentication

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| Mobile SAST | Activation flow analysis | Secure activation code |
| Mobile DAST | Activation bypass testing | Test activation security |

---

### Control 2(d) - Secure Provisioning/Deprovisioning

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| Mobile SAST | Provisioning code review | Secure provisioning logic |
| Mobile DAST | Deprovisioning testing | Verify complete data removal |

---

### Control 2(e-f) - Reputable Distribution Platforms, Platform Access Controls

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| SLSA | Build provenance | Verify app authenticity |
| Secret Detection | App signing key review | Protect signing keys |
| DevSecOps | Secure release pipeline | Prevent unauthorized uploads |

---

### Control 2(g) - Fake Application Monitoring

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| DevSecOps | App store monitoring | Detect impersonation |

**Notes:** Brand protection services to detect fake apps.

---

## Control 3 - Agent/Intermediary Mobile Devices
**Type:** S (Standard)

### Control 3(a-b) - Device Hardening, Remote Wipe
**NOT AppSec** - Device management (MDM) is infrastructure.

---

### Control 3(c) - Card Payment Industry Standards

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| Mobile SAST | PCI compliance scanning | Payment security in code |

**Notes:** PCI DSS for card payment security.

---

### Control 3(d) - Data Masking on Display

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| Mobile SAST | Data masking implementation review | Verify masking in code |
| Mobile DAST | Screen capture testing | Test masking effectiveness |

---

### Control 3(e) - 30-Day Customer Information Retention Limit

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| Mobile SAST | Data retention logic review | Verify purge implementation |
