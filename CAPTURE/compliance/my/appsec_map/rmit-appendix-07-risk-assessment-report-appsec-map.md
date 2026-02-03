# RMIT Appendix 7: Risk Assessment Report and External Party Assurance - AppSec Mapping

## Part A-B: Report Templates and Confirmation Format
**Type:** S (Standard)

### AppSec Mapping

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| Threat Modeling | Application risk assessment | Document application risks |
| SAST/DAST | Security test reports | Evidence for assessment |
| Application Pentest | Pentest reports | Quality assurance evidence |

---

## Part C: External Assurance Requirements
**Type:** S (Standard)

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| Application Pentest | Independent application pentest | External security assurance |
| Maturity Assessment | BSIMM15 | Independent maturity assessment |

---

## Part D: Minimum Controls for ESP Assessment

### Control D.1 - Security Requirements Assessment
**Partial AppSec.** Only access control code review is AppSec.

| Sub-control | AppSec? | Better Approach |
|-------------|---------|-----------------|
| (a) Access control | YES (if in code) | SAST for auth code |
| (b) Physical security | NO | Physical security assessment |
| (c) Operations security | NO | Operations review |
| (d) Communication security | NO | Network security assessment |
| (e) Incident management | NO | Incident response assessment |
| (f) BCM | NO | BCM assessment |

---

### Control D.2(a) - Authentication and Session Security

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| SAST | Session management review | Secure session code |
| DAST | Session hijacking tests | Test session security |
| IAST | Runtime session monitoring | Detect session issues |
| Application Pentest | Auth testing | Validate authentication |

---

### Control D.2(b) - Transaction Authentication

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| SAST | Transaction signing review | Non-repudiation code |
| DAST | Channel security testing | Test secure delivery |
| API Security Testing | Transaction binding | Validate transaction integrity |

---

### Control D.2(c) - Segregation of Duties

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| SAST | Access control logic review | Verify segregation in code |
| DAST | Authorization bypass testing | Test access controls |

---

### Control D.2(d) - Data Integrity
**Partial AppSec.**

| Sub-control | AppSec? | Better Approach |
|-------------|---------|-----------------|
| (i) E2E encryption | YES (if in code) | SAST encryption review |
| (ii-iii) Network security | NO | Network assessment |
| (iv) Pentest | YES | Application pentest |
| (v) Audit trail | YES (if in code) | SAST logging review |
| (vi-viii) Confidentiality, auth | YES | SAST/DAST |

---

### Control D.2(e) - Mobile Device Security

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| Mobile SAST | Secure code analysis | (i-ii) Mobile code security |
| Mobile DAST | Mobile penetration testing | (iii) Mobile app testing |
| Mobile App Shielding | Runtime protection | (ii) Compromised device detection |
| Mobile SAST | Data storage analysis | (v) No sensitive local storage |
| Mobile SAST | OTP implementation review | (x-xi) Transaction code security |

**Notes:** Use OWASP MSTG for testing guidance.
