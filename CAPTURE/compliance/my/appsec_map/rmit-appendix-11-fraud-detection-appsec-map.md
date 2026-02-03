# RMIT Appendix 11: Fraud Detection Standards - AppSec Mapping

## Overview
Fraud detection is **NOT AppSec**. It's operational analytics handled by:
- Commercial fraud platforms (FICO, SAS, Featurespace)
- Fraud operations teams
- Risk analytics teams

**ROI Decision:** FIs don't build custom fraud detection code - they buy commercial solutions.

---

## Controls 1-8 Analysis

| Control | Topic | AppSec? | Better Approach |
|---------|-------|---------|-----------------|
| 1 | Customer risk profiles | NO | Fraud analytics platform |
| 2(a-b) | Transaction monitoring | NO | Fraud analytics platform |
| 2(c) | Device fingerprinting | NO | Commercial device ID (ThreatMetrix, iovation) |
| 2(d) | AI account takeover | NO | Commercial fraud AI |
| 2(e) | Vulnerable customer scoring | NO | Fraud rules engine |
| 2(f) | Biometric credential change | NO | Commercial biometric SDK |
| 3 | Session hijacking detection | **PARTIAL** | Session security in YOUR app code |
| 4 | Access restriction process | NO | Fraud operations |
| 5 | Suspicious transaction investigation | NO | Fraud operations |
| 6 | Contact center resources | NO | Operations staffing |
| 7 | Fraud rule updates | NO | Fraud analytics platform |
| 8 | Fraud management playbook | NO | Fraud operations |

---

## AppSec Mapping

### Control 3 - Session Hijacking Detection (Partial)
Only AppSec if you implement session security in YOUR application code:

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| SAST | Session management review | Secure session handling code |
| DAST | Session hijacking testing | Validate session security |

**Notes:** Commercial fraud platforms typically handle session anomaly detection. Only map to AppSec if implementing custom session security.

---

## Summary

**This appendix has minimal AppSec relevance.** Only Control 3 (session security) applies, and only if implementing custom code.

Use commercial solutions:
- Device fingerprinting: ThreatMetrix, iovation
- Fraud detection: FICO, SAS, Featurespace
- Behavioral biometrics: BioCatch, BehavioSec
- Session security: Commercial fraud platform features
