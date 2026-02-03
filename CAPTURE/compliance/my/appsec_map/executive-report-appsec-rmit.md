# Application Security Investment Case for RMIT Compliance

**Prepared for:** Board of Directors
**Prepared by:** Chief Information Security Officer
**Date:** February 2025
**Classification:** Internal Use Only

---

## Executive Summary

This report presents the investment case for Application Security capabilities to address Bank Negara Malaysia's Risk Management in Technology requirements issued November 2025. Application Security represents one layer within the institution's defense-in-depth model, specifically addressing vulnerabilities in software code, third-party components, and application programming interfaces that the institution develops or controls. Analysis indicates that approximately 35 percent of RMIT controls have direct Application Security relevance, with the remaining 65 percent addressed by network security, physical security, endpoint management, and operational procedures. Failure to invest in Application Security exposes the institution to regulatory penalties, reputational damage, and financial losses from application-layer breaches, which represented the root cause in eight of the ten largest data breach settlements between 2017 and 2024, with combined costs exceeding USD 5 billion.

---

## Section 1: Application Security Coverage of RMIT Controls

### Scope Definition

Application Security applies exclusively to controls where the institution writes, modifies, or controls application source code. It does not apply to commercial off-the-shelf products, network infrastructure, physical security, or endpoint devices managed by platform teams.

### Coverage Analysis

| RMIT Section | Total Controls | AppSec Applicable | Percentage |
|--------------|----------------|-------------------|------------|
| Part A Overview | 7 | 5 | 71 |
| Chapter 8 Governance | 7 | 4 | 57 |
| Chapter 9 Technology Risk Management | 5 | 5 | 100 |
| Chapter 10 Technology Operations | 3 | 3 | 100 |
| Chapter 11 Cybersecurity Management | 9 | 6 | 67 |
| Chapter 12 Digital Services | 9 | 5 | 56 |
| Chapter 13 Technology Audits | 4 | 4 | 100 |
| Chapter 14-15 External Assurance and Training | 5 | 2 | 40 |
| Part C Regulatory Process | 8 | 6 | 75 |
| Appendix 1 Storage and Transportation | 5 | 0 | 0 |
| Appendix 2 Self-Service Terminals | 22 | 0 | 0 |
| Appendix 3 Digital Services Controls | 9 | 9 | 100 |
| Appendix 4 Mobile Applications | 9 | 9 | 100 |
| Appendix 5 Cybersecurity Controls | 25 | 8 | 32 |
| Appendix 6 Simplified Notification | 3 | 2 | 67 |
| Appendix 7 Risk Assessment Report | 8 | 6 | 75 |
| Appendix 8 Third Party Risks | 7 | 3 | 43 |
| Appendix 10 Cloud Services | 12 | 5 | 42 |
| Appendix 11 Fraud Detection | 8 | 1 | 13 |

### Summary by Security Layer

| Security Layer | RMIT Controls Addressed | Primary Tools and Solutions |
|----------------|------------------------|----------------------------|
| Application Security | 35 percent | SAST, DAST, SCA, SBOM, API Testing |
| Network Security | 20 percent | Firewall, IDS/IPS, DDoS Protection |
| Endpoint and Device | 15 percent | EDR, MDM, Device Hardening |
| Physical Security | 10 percent | Access Control, CCTV, Facility Security |
| Operational Security | 20 percent | SOC, Incident Response, Fraud Operations |

### Controls Outside Application Security Scope

The following RMIT sections require investment in solutions other than Application Security:

| RMIT Section | Appropriate Solution | Rationale |
|--------------|---------------------|-----------|
| Appendix 1 | Hardware encrypted devices, DLP | Physical media handling |
| Appendix 2 | Endpoint management, device hardening | ATM and kiosk vendor software |
| Appendix 5 Part A | Firewall, IDS/IPS, DDoS services | Network infrastructure |
| Appendix 5 Part B-C | Commercial DLP, SIEM | Data loss prevention, SOC operations |
| Appendix 11 | Commercial fraud platforms | Fraud analytics and detection |
| Chapter 14.1-14.2 | Infrastructure auditors | Data center and network assessment |

---

## Section 2: Consequences of Inadequate Investment

### Regulatory Consequences

Under the Financial Services Act 2013 and Islamic Financial Services Act 2013, Bank Negara Malaysia may impose the following for non-compliance with RMIT requirements marked as Standards:

| Enforcement Action | Description |
|-------------------|-------------|
| Monetary Penalty | Up to RM25 million for institutions, RM3 million for individuals |
| License Conditions | Additional operating restrictions or capital requirements |
| Independent Review | Mandatory external assessment at institution expense |
| Remediation Orders | Required corrective action plans with defined timelines |
| Public Disclosure | Enforcement actions may be published |

### Financial Impact of Application-Layer Breaches

The following table presents confirmed financial impacts from breaches where application security failures were the root cause:

| Incident | Year | Root Cause | Confirmed Financial Impact |
|----------|------|------------|---------------------------|
| Change Healthcare | 2024 | Ransomware via unpatched systems | USD 2.5 billion total costs |
| Meta Texas Biometric | 2024 | Unauthorized data processing | USD 1.4 billion settlement |
| Equifax | 2017 | Unpatched Apache Struts vulnerability | USD 700 million settlement |
| T-Mobile | 2021 | API vulnerability exploitation | USD 500 million total costs |
| LinkedIn GDPR | 2024 | Processing without consent | USD 335 million fine |
| Capital One | 2019 | Server-side request forgery | USD 270 million total costs |

### Supply Chain Attack Escalation in 2025

The software supply chain has emerged as a primary attack vector in 2025, with incidents demonstrating increased sophistication:

| Incident | Date | Attack Method | Impact |
|----------|------|---------------|--------|
| Shai-Hulud npm Worm | September 2025 | Compromised npm packages with self-replicating malware | 18 packages, USD 50 million cryptocurrency theft |
| Shai-Hulud 2.0 | November 2025 | Self-replicating worm via package manager scripts | 796 packages, credential theft across 132 million downloads |
| Salesloft and Drift | August 2025 | SaaS application compromise propagating to customers | 700 organizations including Google and Allianz |
| SharePoint Zero-Day | July 2025 | Chained vulnerabilities exploited by state actor | 400 organizations including US nuclear agency |

### Cost Statistics

| Metric | 2024 Value | Source |
|--------|------------|--------|
| Average breach cost globally | USD 4.88 million | IBM Cost of a Data Breach Report |
| Healthcare sector average | USD 10.93 million | IBM Cost of a Data Breach Report |
| Financial services average | USD 5.97 million | IBM Cost of a Data Breach Report |
| Americans impacted by breaches | 1 billion | Identity Theft Resource Center |

### Scenario Analysis

| Scenario | Probability | Description | Estimated Impact |
|----------|-------------|-------------|------------------|
| Optimistic | 20 percent | Minor audit findings, no exploitation | Remediation costs only |
| Expected | 60 percent | Vulnerability exploited, contained breach | USD 5 to 15 million |
| Adverse | 20 percent | Supply chain compromise, systemic breach | USD 50 to 200 million |

---

## Section 3: Maturity Measurement Framework

### Recommended Assessment Frameworks

| Framework | Publisher | Purpose | Recommended Use |
|-----------|-----------|---------|-----------------|
| BSIMM15 | Black Duck | Application security program maturity | Annual benchmarking against financial sector peers |
| Supply Chain MAP | Black Duck | Software supply chain maturity | Quarterly assessment of third-party risk |
| SLSA | OpenSSF | Build integrity verification | Technical compliance for CI/CD pipelines |
| OWASP SAMM | OWASP | Software assurance maturity | Self-assessment and roadmap development |

### BSIMM15 Maturity Levels

| Level | Description | Characteristics |
|-------|-------------|-----------------|
| Level 1 | Emerging | Ad-hoc activities, reactive security testing |
| Level 2 | Maturing | Defined processes, consistent execution across teams |
| Level 3 | Optimizing | Metrics-driven decisions, continuous improvement |

### Key Performance Indicators

| Category | Metric | Target | Measurement Frequency |
|----------|--------|--------|----------------------|
| Risk Reduction | Mean time to remediate critical vulnerabilities | Under 7 days | Weekly |
| Risk Reduction | Vulnerability escape rate to production | Under 5 percent | Monthly |
| Risk Reduction | Security debt backlog | Declining trend | Monthly |
| Maturity | BSIMM level | Level 2 minimum | Annual |
| Maturity | SLSA level for critical builds | Level 2 minimum | Quarterly |
| Velocity | Security gate pass rate | Above 85 percent | Weekly |
| Velocity | Mean time to approve security exceptions | Under 2 days | Weekly |
| Coverage | Third-party components with SBOM | 100 percent | Quarterly |
| Coverage | Applications with security testing | 100 percent | Quarterly |

---

## Section 4: Gap Assessment

### Current State Assessment

The following assessment assumes baseline capabilities. Actual ratings should be validated through formal assessment.

| RMIT Control Area | SAST | DAST | SCA | SBOM | DevSecOps | API Security | Mobile | Pentest |
|-------------------|------|------|-----|------|-----------|--------------|--------|---------|
| Chapter 10 SDLC | Gap | Gap | Gap | Gap | Gap | N/A | N/A | Gap |
| Chapter 12 Digital | Gap | Gap | N/A | N/A | Gap | Gap | Gap | Gap |
| Appendix 3 Auth/Session | Gap | Gap | N/A | N/A | Gap | Gap | N/A | Gap |
| Appendix 4 Mobile | Gap | Gap | Gap | N/A | Gap | N/A | Gap | Gap |
| Appendix 5 Part E API | Gap | Gap | Gap | Gap | Gap | Gap | N/A | Gap |
| Appendix 8 Supply Chain | N/A | N/A | Gap | Gap | N/A | N/A | N/A | N/A |
| Appendix 10 Cloud | Gap | Gap | Gap | N/A | Gap | N/A | N/A | Gap |

Legend: Gap indicates capability not currently deployed or not meeting RMIT requirements. N/A indicates control area not applicable.

### Investment Priority Matrix

| Priority | Capability | RMIT Coverage | Implementation Rationale |
|----------|------------|---------------|-------------------------|
| 1 | Static Application Security Testing | Chapters 10, 12, Appendices 3-5, 7, 10 | Foundation for secure development |
| 2 | Dynamic Application Security Testing | Chapters 10, 12, Appendices 3-5, 7, 10 | Runtime vulnerability detection |
| 3 | Software Composition Analysis | Chapters 9-10, Appendices 4-5, 8, 10 | Supply chain risk mitigation |
| 4 | DevSecOps Integration | All chapters | Automation and scalability |
| 5 | Application Penetration Testing | Chapters 11, 13, Appendices 3-5, 7 | Independent validation |
| 6 | Software Bill of Materials | Chapters 9, 11, Appendices 5, 8 | Asset visibility and tracking |
| 7 | API Security Testing | Appendices 3, 5, 7 | Digital services protection |
| 8 | Mobile Application Testing | Chapter 12, Appendices 4, 7 | Mobile channel security |

---

## Section 5: Recommendations

### Immediate Actions (0 to 90 days)

1. Conduct formal gap analysis against RMIT requirements as mandated in Section 18.1
2. Engage BSIMM15 assessment to establish baseline maturity
3. Initiate procurement for SAST, DAST, and SCA capabilities
4. Establish software bill of materials generation for critical applications

### Short-Term Actions (90 to 180 days)

1. Deploy security testing tools into development pipelines
2. Implement security gates for production releases
3. Establish vulnerability management process with defined SLAs
4. Conduct initial penetration testing of digital services

### Medium-Term Actions (180 to 365 days)

1. Achieve BSIMM Level 2 maturity across core practices
2. Implement SLSA Level 2 for critical application builds
3. Establish security champions program across development teams
4. Complete supply chain risk assessment using Supply Chain MAP

### Investment Estimate

| Capability | Implementation Cost | Annual Operating Cost | Notes |
|------------|--------------------|-----------------------|-------|
| SAST Platform | USD 200,000 to 400,000 | USD 100,000 to 200,000 | Enterprise license |
| DAST Platform | USD 100,000 to 200,000 | USD 50,000 to 100,000 | Enterprise license |
| SCA Platform | USD 150,000 to 300,000 | USD 75,000 to 150,000 | Enterprise license |
| DevSecOps Integration | USD 100,000 to 200,000 | USD 50,000 to 100,000 | Professional services |
| Penetration Testing | N/A | USD 200,000 to 400,000 | Annual program |
| BSIMM Assessment | N/A | USD 50,000 to 100,000 | Annual assessment |
| Training Program | USD 50,000 to 100,000 | USD 25,000 to 50,000 | Secure coding training |
| Total Year 1 | USD 600,000 to 1,200,000 | USD 550,000 to 1,100,000 | |

---

## Appendix A: Reference Materials

### Regulatory Sources
- Bank Negara Malaysia, Risk Management in Technology, Issued 28 November 2025
- Financial Services Act 2013, Sections 47, 143
- Islamic Financial Services Act 2013, Sections 57, 155

### Industry Standards
- OWASP Top 10 Web Application Security Risks
- OWASP API Security Top 10
- OWASP Mobile Application Security Verification Standard
- NIST Cybersecurity Framework
- ISO 27001 Information Security Management

### Maturity Frameworks
- Black Duck BSIMM15, Building Security In Maturity Model Version 15
- Black Duck Software Supply Chain Maturity Assessment Program
- OpenSSF SLSA, Supply-chain Levels for Software Artifacts
- OWASP SAMM, Software Assurance Maturity Model

### Breach Cost Data
- IBM Security, Cost of a Data Breach Report 2024
- Identity Theft Resource Center, 2024 Data Breach Report
- Ponemon Institute, Application Security Research

---

**Document Control**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | February 2025 | CISO | Initial release |

---

*This document contains confidential information intended for Board review. Distribution outside the institution requires prior authorization.*
