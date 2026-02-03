# RMIT Appendix 6: Criteria for Simplified Notification - AppSec Mapping

## Overview
This appendix defines criteria for simplified notification. Limited direct AppSec relevance.

## Control 1 - Simplified Notification Criteria
**Type:** G (Guideline)
**Requirement:** Simplified notification applies when enhancement does NOT result in: (a) new technology introduction, (b) material architecture changes, (c) transmission of confidential/sensitive data.

### AppSec Mapping

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| Threat Modeling | Change impact assessment | Determine if changes are material |
| SAST/DAST | Delta security analysis | Assess security impact of changes |

**Notes:** Assessment to determine notification type.

---

## Control 2-3 - Service Expansion and Regulated Entity Integration
**Type:** G (Guideline)

### AppSec Mapping

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| API Security Testing | Integration security testing | Secure integration implementation |
| DAST | API endpoint testing | Test integration security |

**Notes:** Simplified process - still requires secure implementation.
