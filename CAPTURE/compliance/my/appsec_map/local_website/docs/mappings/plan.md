# RMIT Compliance to AppSec Mapping Plan

## Objective
For each RMIT compliance document (chapter/appendix), create a mapping file that correlates each control/requirement with applicable AppSec tools and practices.

---

## 1. Output Structure
For each source file `rmit-xxx.txt`, create `rmit-xxx-appsec-map.md`:

```markdown
# RMIT [Chapter/Appendix] - AppSec Mapping

## Control [X.X]
**Type:** S (Standard) / G (Guideline)
**Requirement:** [Full text or summary]

### AppSec Mapping

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| SAST     | ...          | ...                          |
| SCA      | ...          | ...                          |

**Notes:** [Any observations, gaps, or implementation considerations]

---
```

---

## 2. AppSec Categories Reference

| Category | Description |
|----------|-------------|
| SAST | Static Application Security Testing |
| DAST | Dynamic Application Security Testing |
| IAST | Interactive Application Security Testing |
| SCA | Software Composition Analysis |
| SBOM | Software Bill of Materials |
| DevSecOps | CI/CD security integration |
| SLSA | Supply-chain Levels for Software Artifacts |
| DORA | DevOps Research & Assessment metrics |
| Container Security | Image scanning, runtime protection |
| API Security | API gateway, auth, rate limiting |
| Secret Management | Vault, credential scanning |
| IaC Security | Infrastructure-as-Code scanning |
| Penetration Testing | Red team, bug bounty |
| Threat Modeling | STRIDE, PASTA, etc. |
| Security Training | Secure coding awareness |
| Monitoring/SIEM | Runtime detection, logging |

---

## 3. Files to Process (20 total)
Process in order, one by one:

1. rmit-header-toc.txt
2. rmit-part-a-overview.txt
3. rmit-ch08-governance.txt
4. rmit-ch09-technology-risk-management.txt
5. rmit-ch10-technology-operations-management.txt
6. rmit-ch11-cybersecurity-management.txt
7. rmit-ch12-digital-services.txt
8. rmit-ch13-technology-audits.txt
9. rmit-ch14-external-party-assurance.txt
10. rmit-part-c-regulatory-process.txt
11. rmit-appendix-01-storage-transportation.txt
12. rmit-appendix-02-sst-controls.txt
13. rmit-appendix-03-digital-services-controls.txt
14. rmit-appendix-04-mobile-applications.txt
15. rmit-appendix-05-cybersecurity-controls.txt
16. rmit-appendix-06-simplified-notification.txt
17. rmit-appendix-07-risk-assessment-report.txt
18. rmit-appendix-08-third-party-risks.txt
19. rmit-appendix-10-cloud-services.txt
20. rmit-appendix-11-fraud-detection.txt

---

## 4. Final Deliverable (Separate Task)
After all mappings complete:
- 1 summary matrix (`appsec-coverage-matrix.md`) consolidating all mappings
- Ranking/prioritization analysis
