# RMIT Appendix 1: Storage and Transportation of Sensitive Data in Removable Media - AppSec Mapping

## Overview
This appendix covers physical media handling. **NOT AppSec.**

---

## Controls 1-5

| Control | Topic | AppSec? | Better Approach |
|---------|-------|---------|-----------------|
| 1 | Encryption on removable media | NO | Hardware-encrypted USB drives, OS encryption |
| 2 | Access control to media | NO | Physical access controls |
| 3 | Prohibit unauthorized copying | NO | DLP endpoint agents, device control |
| 4 | Transportation controls | NO | Physical security procedures |
| 5 | Third-party compliance | NO | Vendor management process |

---

## AppSec Mapping

**None.** This entire appendix is out of AppSec scope.

ROI Decision: FIs don't write code to encrypt USB drives - they use hardware-encrypted devices or OS-level encryption (BitLocker). Device control is handled by endpoint management (MDM/DLP), not AppSec.
