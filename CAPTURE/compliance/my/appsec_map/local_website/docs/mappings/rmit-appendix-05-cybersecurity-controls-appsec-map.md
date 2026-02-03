# RMIT Appendix 5: Control Measures on Cybersecurity - AppSec Mapping

## Part A: Network Security (Controls 1-6)
**NOT AppSec.** Use network/infrastructure security:
- Firewall configuration
- IDS/IPS deployment
- DDoS protection services (Cloudflare, AWS Shield)
- VPN/network tunnels
- Network segmentation (SDN)

---

## Part B: Data Security

### Control B.1 - Data-at-Rest Encryption
**NOT AppSec.** Use:
- Database transparent encryption (TDE)
- Storage encryption
- OS-level encryption

Only AppSec if encryption is implemented in YOUR application code.

---

### Control B.2-4 - Data Loss Prevention
**NOT AppSec.** Use commercial DLP solutions (Symantec, Microsoft Purview).

---

### Control B.5 - Customer Information Breach Prevention
**Type:** S (Standard)

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| SAST | Data exposure scanning | Detect accidental exposure in code |
| Secret Detection | Credential scanning | Detect exposed credentials in code |

**Notes:** Only the code-level detection is AppSec. Operational breach monitoring is NOT AppSec.

---

## Part C: Security Operations Centre (SOC)
**NOT AppSec.** SOC is operational security:
- SIEM deployment
- Threat hunting
- Incident response
- Threat intelligence

AppSec tools feed findings to SOC, but SOC operations is NOT AppSec.

---

## Part D: VAPT

### Control D.1 - VAPT SOPs
Limited AppSec - only for application-layer pentesting procedures.

---

### Control D.2-3 - Vulnerability Assessment and Penetration Testing
**Type:** S (Standard)

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| DAST | Dynamic testing tools | Web/API vulnerability scanning |
| SCA | Composition analysis tools, Dependabot | Dependency vulnerability assessment |
| Application Pentest | Web/mobile/API pentesting | Application penetration testing |

**Notes:** Network vulnerability scanning and network pentesting are NOT AppSec.

---

### Control D.4 - Pre-Launch Testing
**Type:** S (Standard)

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| DevSecOps | Pre-production security gates | Mandatory testing before launch |
| Application Pentest | New application pentests | Test new applications |

---

### Control D.5-6 - Reporting and Compromise Assessment
Limited AppSec - only for application-level compromise detection.

---

## Part E: API Security
**Type:** S (Standard)
**This is the primary AppSec section of Appendix 5.**

### Control E.1(a) - Centralized API Inventory

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| SBOM | API inventory tools | Comprehensive API inventory |

---

### Control E.1(b) - API Availability
**Partial AppSec.**
- Application-level rate limiting = AppSec
- DDoS protection = NOT AppSec (use Cloudflare, AWS Shield)

---

### Control E.1(c) - Secure Coding Practices

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| SAST | API code analysis | Secure API implementation |
| SCA | Third-party library validation | Validate dependencies |
| Secure Coding Training | API security training | Developer training |

---

### Control E.1(d) - Encryption and Key Management

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| SAST | Encryption implementation review | Verify encryption in API code |
| Secret Detection | Key management review | Secure key handling in code |

---

### Control E.1(e-g) - Brute-Force, Auth, API Gateway

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| SAST | Auth code review | Secure auth implementation |
| DAST | Auth bypass testing | Test authorization |
| API Security Testing | OAuth/JWT testing | Validate token handling |

---

### Control E.1(h) - Periodic Security Assessments

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| DAST | API security scanning | Automated API testing |
| API Security Testing | API security testing tools, API security testing tools | Specialized API testing |
| Application Pentest | API penetration testing | Manual API testing |

---

### Control E.1(i-j) - Monitoring and Token Revocation

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| SAST | Token lifecycle review | Verify revocation implementation |
| Secret Detection | Exposed key detection | Detect compromised keys |

**Notes:** OWASP API Security Top 10 is the reference standard.
