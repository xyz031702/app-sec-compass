# Summary Report Generation Plan

## Context Files
1. `plan.md` - Mapping methodology for compliance controls to AppSec tools/process
2. `review.md` - Guidelines to identify what IS and IS NOT AppSec (with ROI criteria)
3. `*-appsec-map.md` - Individual mapping results per RMIT chapter/appendix
4. `appsec-coverage-matrix.md` - Consolidated coverage matrix

---

## Report Objective

As a CISO reporting to the Board, produce an investment case for the AppSec layer of compliance controls (onion model: AppSec is one layer among network, physical, endpoint, etc.).

---

## Report Sections to Generate

### Section 1: AppSec Coverage
**Question:** What is the coverage of AppSec for RMIT compliance controls?

**Content to include:**
- % of controls where AppSec applies vs. other layers
- Visual breakdown (table or diagram)
- Clear distinction: what AppSec covers vs. infrastructure/physical/endpoint

---

### Section 2: Consequences of Not Investing
**Question:** What happens if we don't invest in AppSec?

**Content to include:**

| Scenario | Description |
|----------|-------------|
| Best case | Minor audit findings, no exploits |
| Expected case | Vulnerability exploited, contained breach |
| Worst case | Supply chain compromise, systemic breach |

**Real-world examples to reference (2025):**

| Incident | Date | Root Cause | Impact | AppSec Prevention |
|----------|------|------------|--------|-------------------|
| **Shai-Hulud npm Worm** | Sep 2025 | Phishing → npm account compromise → malicious packages | 18 packages, 2.6B weekly downloads, $50M crypto stolen | SCA + SBOM + version pinning |
| **Shai-Hulud 2.0 "The Second Coming"** | Nov 2025 | Self-replicating worm via preinstall scripts | 796 packages, 132M downloads, credential theft + destructive wipes | SCA + DevSecOps gates + SBOM |
| **Salesloft/Drift Supply Chain** | Aug 2025 | Compromised SaaS app → Salesforce environments | 700+ orgs (Google, Allianz), "SolarWinds moment for SaaS" | SCA + third-party risk assessment |
| **SharePoint ToolShell Zero-Day** | Jul 2025 | Chained CVEs (CVE-2025-53770/53771) | 400+ orgs including NNSA, Chinese APT | DAST + patch management |
| **Blue Shield California** | 2025 | Google Analytics misconfiguration | 4.7M customer records exposed | DAST + config scanning |
| **NYU Data Breach** | 2025 | Web application vulnerability | 3M+ applicant records | SAST + DAST |
| **xz Utils Backdoor** | 2024 | Malicious maintainer commit over 2 years | Near-miss on Linux infrastructure | SCA + code review + SBOM |
| **Polyfill.io** | 2024 | Domain takeover → malicious JS injection | 100K+ websites compromised | SCA + SBOM + dependency monitoring |

**Key 2025 Trends:**
- npm supply chain attacks becoming weaponized (self-replicating worms)
- SaaS-to-SaaS compromise chains ("SolarWinds for SaaS")
- Preinstall/postinstall script abuse in package managers
- Credential exfiltration to public GitHub repos to evade detection

**Historical breaches with confirmed major costs (2017-2024):**

| Incident | Year | Root Cause | Financial Impact | AppSec Prevention |
|----------|------|------------|------------------|-------------------|
| **Change Healthcare** | 2024 | Ransomware via unpatched systems | **$2.5B+ total costs**, $22M ransom paid, 190M records | SCA + DAST + patch mgmt |
| **AT&T/Snowflake** | 2024 | Stolen credentials, no MFA on cloud | 110M customers, part of 500M Snowflake MDL | Secret management + API security |
| **Ticketmaster/Snowflake** | 2024 | Cloud credential theft | 560M customers exposed | Secret management + SCA |
| **Meta (Texas Biometric)** | 2024 | Unauthorized biometric data capture | **$1.4B settlement** (largest US privacy settlement) | Privacy by design |
| **LinkedIn GDPR** | 2024 | Processing without consent | **€310M ($335M) fine** | Compliance scanning |
| **T-Mobile** | 2021 | API vulnerability exploited | **$500M** ($350M settlement + $150M security investment), 76M records | API security + DAST |
| **Capital One** | 2019 | SSRF vulnerability in WAF config | **$270M** ($80M OCC fine + $190M settlement), 100M records | SAST + DAST |
| **Equifax** | 2017 | Unpatched Apache Struts (CVE-2017-5638) | **$700M+ settlement**, 147M records | SCA + patch management |

**Key cost statistics:**
- Average breach cost 2024: **$4.88M** (IBM Report, 10% YoY increase)
- Healthcare sector average: **$10.93M** per breach
- Financial services average: **$5.97M** per breach
- 2024 saw **1 billion+ Americans** impacted by breaches (490% increase over 2023)

**Sources:**
- [CISA: npm Supply Chain Compromise](https://www.cisa.gov/news-events/alerts/2025/09/23/widespread-supply-chain-compromise-impacting-npm-ecosystem)
- [Palo Alto Unit42: Shai-Hulud Analysis](https://unit42.paloaltonetworks.com/npm-supply-chain-attack/)
- [Check Point: Shai-Hulud 2.0](https://blog.checkpoint.com/research/shai-hulud-2-0-inside-the-second-coming-the-most-aggressive-npm-supply-chain-attack-of-2025/)
- [Infosecurity: Top 10 Cyber-Attacks 2025](https://www.infosecurity-magazine.com/news-features/top-10-cyberattacks-of-2025/)
- [CSO: Biggest Data Breach Fines](https://www.csoonline.com/article/567531/the-biggest-data-breach-fines-penalties-and-settlements-so-far.html)
- [Krebs on Security: Change Healthcare](https://krebsonsecurity.com/2024/10/change-healthcare-breach-hits-100m-americans/)
- [FTC: Equifax Settlement](https://www.ftc.gov/enforcement/refunds/equifax-data-breach-settlement)

**Include:** BNM enforcement consequences (penalties, license risk)

---

### Section 3: Maturity & Risk Metrics
**Question:** How do we measure implementation maturity?

**Frameworks to use:**

| Framework | Type | Use For |
|-----------|------|---------|
| BSIMM15 | Commercial | AppSec program maturity benchmarking |
| Supply Chain MAP | Commercial | Software supply chain maturity |
| DORA | Industry standard | DevSecOps velocity metrics |
| OWASP SAMM | Open source | Alternative maturity model |
| SLSA | Open source | Build integrity levels |

**Metric categories:**
1. **Business risk metrics** - MTTR, escape rate, security debt, third-party risk
2. **Technical maturity** - BSIMM levels (1-3), SLSA levels (1-4)
3. **DevSecOps velocity** - Deployment frequency, lead time, security gate pass rate

---

### Section 4: Gap Assessment Heatmap
**Question:** How do we measure current gaps?

**Design a heatmap with:**
- Rows: RMIT control areas (Ch10, Ch11, Ch12, App3, App4, App5, etc.)
- Columns: AppSec tool categories (SAST, DAST, SCA, SBOM, DevSecOps, API, Mobile, Pentest)
- Cells: Maturity rating (🔴 Critical | 🟠 Needs Work | 🟡 Acceptable | 🟢 Mature)

**Include:**
- Priority quadrant (High ROI + High Coverage = Priority 1)
- Current state vs. target state

---

## Output Format

Generate as markdown with:
- Executive summary (1 paragraph)
- Tables for data
- Simple ASCII diagrams where helpful
- Clear section headers
- Actionable recommendations

---

## Notes

- Focus on ROI - not everything needs AppSec (per review.md guidelines)
- Reference real breach examples with costs where available
- Use BSIMM15 and Supply Chain MAP as primary maturity frameworks
- Keep board-appropriate: business impact, not technical details
