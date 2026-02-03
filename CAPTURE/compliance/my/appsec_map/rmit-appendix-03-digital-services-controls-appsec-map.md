# RMIT Appendix 3: Control Measures for Digital Services - AppSec Mapping

## Control 1 - Digital Services Security Controls
**Type:** S (Standard)

### Control 1(a) - Robust Registration/Enrollment Authentication

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| SAST | Authentication flow analysis | Secure registration code |
| DAST | Registration process testing | Test enrollment security |

---

### Control 1(b) - Secure Channels (TLS)

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| DAST | SSL/TLS testing (testssl.sh) | Verify TLS configuration in app |

**Notes:** TLS 1.2 minimum, TLS 1.3 preferred. Application-level TLS config is AppSec.

---

### Control 1(c-d) - Encrypt Confidential Information, Mutual Authentication

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| SAST | Encryption usage analysis | Verify encryption in code |
| DAST | mTLS validation testing | Verify mutual authentication |

---

### Control 1(e) - Secure Session Handling

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| SAST | Session management analysis | Identify session vulnerabilities |
| DAST | Session testing (OWASP ZAP) | Test session security |
| IAST | Runtime session monitoring | Detect session issues |

**Notes:** OWASP Session Management Cheat Sheet.

---

### Control 1(f) - Log Retention (3 years)

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| SAST | Logging implementation review | Verify adequate logging in code |

---

### Control 1(g-j) - Image Verification, Brute-force, Limits, Cooling-off

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| SAST | Business logic review | Verify limit and cooling-off logic |
| DAST | Brute-force testing, bypass testing | Test lockout mechanisms |
| API Security Testing | Rate limiting validation | Anti-brute-force testing |

---

## Control 2 - Identity Proofing Technology
**Type:** S (Standard)
**Requirement:** Must be (a) secure against malware/phishing, (b) accurate with minimal false acceptance, (c) compliant with international standards.

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| SAST | Authentication code analysis | Secure implementation |
| DAST | Biometric bypass testing | Test biometric security |
| Mobile App Shielding | Runtime protection | Protect against device threats |

**Notes:** FIDO2, WebAuthn for passwordless auth. ISO/IEC 30107 for biometrics.

---

## Control 3 - Mobile Device and Customer Details Security
**Type:** S (Standard)

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| SAST | Device binding logic review | Secure binding implementation |
| DAST | Device binding bypass testing | Test binding security |
| Mobile DAST | Device fingerprinting validation | Verify device identification |

---

## Control 4-6 - MFA for Financial Transactions
**Type:** S (Standard)

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| SAST | MFA implementation review | Verify MFA in code |
| DAST | MFA bypass testing | Test MFA enforcement |
| API Security Testing | Transaction signing validation | Verify transaction binding |

**Notes:** PSD2 dynamic linking - auth code bound to specific amount and payee.

---

## Control 7 - OTP Requirements
**Type:** S (Standard)

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| SAST | OTP implementation review | Verify TOTP/HOTP implementation |
| DAST | OTP replay testing | Test time-bound enforcement |

**Notes:** RFC 6238 (TOTP), RFC 4226 (HOTP).

---

## Control 8 - Non-MFA Transactions (Below RM10,000)
**Type:** S (Standard)

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| SAST | Limit logic review | Verify limit implementation |

---

## Control 9 - Cryptographic Key-Based Authentication (Passwordless)
**Type:** S (Standard)

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| SAST | FIDO2/WebAuthn implementation review | Verify secure implementation |
| DAST | Passwordless authentication testing | Test implementation security |
| Secret Detection | Private key handling review | Secure key storage |

**Notes:** FIDO2/WebAuthn is the leading passwordless standard.
