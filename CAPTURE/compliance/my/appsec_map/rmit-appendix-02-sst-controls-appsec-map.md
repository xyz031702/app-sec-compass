# RMIT Appendix 2: Control Measures on Self-service Terminals (SSTs) - AppSec Mapping

## Overview
SST/ATM controls are **NOT AppSec**. These are addressed by:
- Device hardening (CIS Benchmarks)
- Application whitelisting (endpoint management)
- Commercial AV/EDR solutions
- Physical security systems

**ROI Decision:** FIs don't write ATM application code - they use vendor software. Platform/endpoint teams handle these controls, not AppSec teams.

---

## Cash SST Controls 1-14

| Control | Topic | AppSec? | Better Approach |
|---------|-------|---------|-----------------|
| 1 | Full hard disk encryption | NO | OS-level encryption (BitLocker) |
| 2 | Card retention/blocking | NO | ATM switching system (vendor) |
| 3 | Antivirus | NO | Commercial AV/EDR |
| 4 | Centralized monitoring | NO | Endpoint management platform |
| 5-7 | Physical locks, alarms | NO | Physical security |
| 8 | Component pairing | NO | Hardware security (HSM) |
| 9 | BIOS lock-down | NO | Hardware vendor tools |
| 10 | OS/App hardening | NO | CIS Benchmarks, vendor hardening |
| 11 | System parameters | NO | Endpoint configuration |
| 12 | Application whitelisting | NO | Endpoint management (Carbon Black, McAfee) |
| 13 | Gold disk controls | NO | Image management, endpoint tools |
| 14 | CCTV | NO | Physical security |

---

## Non-Cash SST Controls 1-8

| Control | Topic | AppSec? | Better Approach |
|---------|-------|---------|-----------------|
| 1-8 | Kiosk hardening | NO | OS hardening (CIS Benchmarks) + kiosk mode |

---

## AppSec Mapping

**None.** This entire appendix is out of AppSec scope.

The only scenario where AppSec applies to SST/ATM:
- If the FI develops custom ATM application software (rare)
- Then SAST/DAST would apply to that custom code

For standard vendor ATM software, use:
- Device hardening standards
- Endpoint management platforms
- Vendor security updates
