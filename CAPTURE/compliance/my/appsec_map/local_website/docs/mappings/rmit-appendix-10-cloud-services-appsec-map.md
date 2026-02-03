# RMIT Appendix 10: Key Risks and Control Measures for Cloud Services - AppSec Mapping

## Overview
Cloud security has a **shared responsibility model**. Most cloud governance controls are NOT AppSec - they're vendor management and infrastructure configuration.

**AppSec applies when:** You deploy YOUR application code/containers to the cloud.

---

## Part A: Cloud Governance

### Controls A.1-5 - Cloud Risk Management, Policy, Due Diligence, Certifications, Contracts
**NOT AppSec.** These are vendor management and governance:
- Cloud vendor assessment
- Contract negotiation
- SOC 2/ISO 27001 certification review
- Cloud usage policies

---

## Part B: Cloud Design and Control

### Cloud Infrastructure Security
**NOT AppSec.** Use cloud-native/CSPM tools:
- CSPM (Prisma Cloud, Wiz) - for cloud configuration
- Cloud IAM - for identity management
- Network security groups - for network controls
- Cloud DDoS protection - for availability

---

### Application Workload Security (AppSec Relevant)

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| Container Security | Container scanning tools | Scan YOUR container images |
| SAST | Cloud application code scanning | Scan YOUR application code |
| DAST | Cloud application testing | Test YOUR running applications |
| IaC Security | IaC scanning tools | Scan YOUR Terraform/CloudFormation |
| Secret Detection | Secret scanning tools | Detect secrets in YOUR code |

**ROI Decision:** Only scan code/containers YOU build. Cloud provider manages their infrastructure.

---

### DevSecOps for Cloud

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| DevSecOps | CI/CD security gates | Automate security in YOUR pipeline |
| SLSA | Build integrity | Secure YOUR build pipeline |
| SCA | Dependency scanning | Scan YOUR dependencies |

---

### Application Penetration Testing

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| Application Pentest | Cloud application pentesting | Test YOUR applications |

**Notes:** Cloud infrastructure pentesting requires CSP approval and is NOT AppSec.

---

## Summary

| Cloud Control Area | AppSec? | Owner |
|--------------------|---------|-------|
| Cloud vendor selection | NO | Procurement/Risk |
| Cloud IAM configuration | NO | Cloud/Platform team |
| Network security groups | NO | Cloud/Platform team |
| CSPM/misconfiguration | NO | Cloud/Platform team |
| YOUR application code | YES | AppSec team |
| YOUR container images | YES | AppSec team |
| YOUR IaC code | YES | AppSec team |
| YOUR CI/CD pipeline | YES | AppSec team |
