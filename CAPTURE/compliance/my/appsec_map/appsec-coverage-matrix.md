# RMIT Compliance to AppSec Coverage Matrix

## Overview
This matrix maps BNM Risk Management in Technology (RMIT) November 2025 requirements to Application Security tools/practices.

**Scope:** Only controls where FIs write/control application code. Commercial solutions and infrastructure controls are excluded.

---

## ROI Decision Framework

Before mapping a control to AppSec, apply this test:

1. **"Do we write/control this code?"** → No = Not AppSec
2. **"Is there a commercial product for this?"** → Yes = Probably not AppSec
3. **"Would a platform team handle this?"** → Yes = Infrastructure, not AppSec
4. **"Is this about OUR application vulnerabilities?"** → Yes = AppSec

---

## AppSec Category Legend

| Abbr | Category | Example Tools |
|------|----------|---------------|
| SAST | Static Application Security Testing | SonarQube, Checkmarx, Fortify |
| DAST | Dynamic Application Security Testing | OWASP ZAP, Burp Suite |
| IAST | Interactive Application Security Testing | Contrast Security |
| SCA | Software Composition Analysis | Snyk, Black Duck |
| SBOM | Software Bill of Materials | CycloneDX, SPDX |
| DevSecOps | CI/CD Security Integration | GitLab Security, GitHub Advanced Security |
| SLSA | Supply-chain Levels for Software Artifacts | Sigstore, in-toto |
| Container | Container Image Security | Trivy, Grype |
| API | API Security Testing | Salt Security, 42Crunch |
| Secret | Secret Detection | GitLeaks, TruffleHog |
| IaC | Infrastructure-as-Code Security | Checkov, tfsec |
| Mobile | Mobile App Security Testing | NowSecure, MobSF |
| Shielding | Mobile App Shielding | Promon, Guardsquare |
| Pentest | Application Penetration Testing | Bug bounty, CREST firms |
| Threat | Threat Modeling | STRIDE, PASTA |
| Training | Secure Coding Training | Secure Code Warrior, WebGoat |
| Maturity | AppSec Maturity Assessment | BSIMM15, OWASP SAMM |

---

## Coverage Matrix

### Legend
- ● = AppSec applies (we write/control this code)
- — = NOT AppSec (commercial product, infrastructure, or operational)

| RMIT Section | SAST | DAST | SCA | SBOM | DevSecOps | Container | API | Secret | Mobile | Pentest | Threat | Training | Maturity |
|--------------|------|------|-----|------|-----------|-----------|-----|--------|--------|---------|--------|----------|----------|
| **Part A: Overview** |
| 1.1-1.4 | ● | ● | ● | ● | ● | | | | | | ● | ● | ● |
| **Ch 8: Governance** |
| 8.1-8.7 | ● | ● | ● | ● | ● | | | | | | | | ● |
| **Ch 9: Tech Risk Mgmt** |
| 9.1-9.5 | ● | ● | ● | ● | ● | ● | | | | | ● | | ● |
| **Ch 10: Tech Ops Mgmt** |
| 10.1-10.3 | ● | ● | ● | | ● | ● | | ● | | | ● | | |
| **Ch 11: Cybersecurity** |
| 11.1-11.3 | ● | ● | ● | ● | ● | | | ● | | | ● | | |
| 11.4-11.9 | ● | ● | ● | | | | | ● | | ● | | | |
| **Ch 12: Digital Services** |
| 12.1-12.3 | ● | ● | | | ● | | ● | ● | ● | | | | |
| 12.4-12.9 | — | — | — | — | — | — | ● | ● | — | — | — | — | — |
| **Ch 13: Tech Audits** |
| 13.1-13.4 | ● | ● | ● | ● | ● | | | | | | ● | ● | ● |
| **Ch 14-15** |
| 14.1-14.2 | — | — | — | — | — | — | — | — | — | — | — | — | — |
| 15.1-15.2 | | | | | | | | | | | | ● | |
| **Part C: Regulatory** |
| 16.1-16.7 | ● | ● | ● | ● | ● | | | | | ● | ● | | |
| 17.1-17.5 | ● | ● | ● | | ● | ● | | ● | | | ● | | |
| 18.1-18.2 | ● | ● | ● | | ● | | | | | | | | ● |
| **Appendix 1** | — | — | — | — | — | — | — | — | — | — | — | — | — |
| **Appendix 2** | — | — | — | — | — | — | — | — | — | — | — | — | — |
| **Appendix 3** |
| Controls 1-9 | ● | ● | | | ● | | ● | ● | | ● | | | |
| **Appendix 4** |
| Controls 1-3 | ● | ● | ● | | ● | | | | ● | ● | ● | | ● |
| **Appendix 5** |
| Part A-C | — | — | — | — | — | — | — | — | — | — | — | — | — |
| Part D (App pentest only) | | ● | ● | | ● | | | | | ● | | | |
| Part E (API) | ● | ● | ● | ● | ● | | ● | ● | | ● | | ● | |
| **Appendix 6** | ● | ● | | | | | ● | | | | ● | | |
| **Appendix 7** | ● | ● | | | ● | | ● | | ● | ● | | | ● |
| **Appendix 8** |
| 2(c), 3(b-c) only | | | ● | ● | | | | | | | | | ● |
| **Appendix 10** |
| App workloads only | ● | ● | ● | | ● | ● | | ● | | ● | | | |
| **Appendix 11** | ● | ● | — | — | — | — | — | — | — | — | — | — | — |

---

## Sections FULLY Out of AppSec Scope

| Section | Reason | Better Approach |
|---------|--------|-----------------|
| Appendix 1 | Physical media handling | Hardware encryption, DLP |
| Appendix 2 | SST/ATM device security | Device hardening, endpoint management |
| Appendix 5 Part A | Network security | Firewall, IDS/IPS |
| Appendix 5 Part B | DLP policies | Commercial DLP |
| Appendix 5 Part C | SOC operations | SIEM, operational security |
| Appendix 11 (most) | Fraud detection | Commercial fraud platforms |
| Ch 14.1-14.2 | Data center/network assessment | Infrastructure auditors |
| Ch 12.4-12.7 | Fraud operations, customer awareness | Fraud team, marketing |

---

## Summary: What IS AppSec in RMIT

### High AppSec Relevance
| RMIT Section | Why AppSec? |
|--------------|-------------|
| Ch 10.2 | Security throughout SDLC |
| Ch 12.1-12.3 | Digital services application code |
| Appendix 3 | Authentication, session, MFA code |
| Appendix 4 | Mobile application security |
| Appendix 5 Part E | API security |
| Appendix 7 Part D | Application penetration testing |

### Medium AppSec Relevance
| RMIT Section | Why AppSec? |
|--------------|-------------|
| Ch 9.2 | TRMF includes AppSec elements |
| Ch 11.3 | CRF application security aspects |
| Appendix 8.2(c), 3(b-c) | Software supply chain |
| Appendix 10 | Cloud application workloads |

### Governance/Process (Supporting)
| RMIT Section | AppSec Role |
|--------------|-------------|
| Ch 8 | AppSec metrics for board |
| Ch 13 | AppSec audit evidence |
| Ch 15.1-15.2 | Secure coding training |
| Part C (16-18) | AppSec for regulatory submissions |

---

## Tool Recommendations by Priority

| Priority | Category | RMIT Coverage | ROI |
|----------|----------|---------------|-----|
| 1 | **SAST** | Ch10, Ch12, App3-4, App5.E | High - YOUR code |
| 2 | **DAST** | Ch10, Ch12, App3-4, App5.D-E | High - YOUR apps |
| 3 | **SCA** | Ch9-10, App4, App5, App8 | High - YOUR dependencies |
| 4 | **DevSecOps** | All chapters | High - YOUR pipeline |
| 5 | **Application Pentest** | Ch11, App3-5, App7 | Medium - validation |
| 6 | **Mobile (SAST/DAST)** | Ch12, App4, App7 | Medium - if mobile apps |
| 7 | **API Security** | App3, App5.E, App7 | Medium - if APIs |
| 8 | **Container** | Ch9-10, Ch17, App10 | Medium - if containers |
| 9 | **SBOM** | Ch9, App5.E, App8 | Medium - inventory |
| 10 | **Maturity (BSIMM15)** | Ch8, Ch13, App4, App7 | Low - benchmarking |

---

## NOT AppSec - Use These Instead

| Control Area | Commercial/Platform Solution |
|--------------|------------------------------|
| SST/ATM security | Device hardening + endpoint management |
| Endpoint protection | EDR (CrowdStrike, SentinelOne) |
| Antivirus | Commercial AV |
| Full disk encryption | BitLocker, LUKS |
| Network security | Firewall, IDS/IPS, SDN |
| DDoS protection | Cloudflare, AWS Shield |
| DLP | Symantec, Microsoft Purview |
| SOC/SIEM | Splunk, QRadar, Sentinel |
| Fraud detection | FICO, SAS, Featurespace |
| Device fingerprinting | ThreatMetrix, iovation |
| General awareness | KnowBe4, Proofpoint |

---

*Generated: 2025-02-03*
*Source: BNM RMIT November 2025*
*Review criteria: appsec_map/review.md (with ROI section)*
