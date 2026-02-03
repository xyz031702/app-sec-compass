# AppSec Mapping Review Guidelines

## What IS AppSec (In Scope)

### Targets
- Source code (any language)
- Application binaries and executables
- Container images and configurations
- Infrastructure-as-Code (Terraform, CloudFormation, Pulumi)
- API definitions and implementations
- Mobile application packages (APK, IPA)
- Web applications and frontend code
- Serverless functions
- Configuration files (application-level)

### Problems to Address
- Code vulnerabilities (injection, XSS, CSRF, etc.)
- Insecure dependencies and libraries
- Hardcoded secrets in code
- Misconfigurations in application/container/IaC
- Insecure API implementations
- Authentication/authorization flaws in code
- Cryptographic weaknesses in implementation

### Practices
- SBOM generation and inventory
- Software supply chain security (SLSA)
- DevSecOps pipeline integration
- Shift-left security testing
- Security gates in CI/CD
- Secure coding standards
- Code review for security
- Threat modeling (application-focused)
- AppSec process maturity assessment
- Developer security training programs

### Tools
- SAST (Static Application Security Testing)
- DAST (Dynamic Application Security Testing)
- SCA (Software Composition Analysis)
- IAST (Interactive Application Security Testing)
- RASP (Runtime Application Self-Protection)
- Container image scanners
- IaC security scanners
- Secret detection tools
- API security testing tools
- Mobile app security testing (MAST)
- Maturity assessment frameworks (BSIMM15, Supply Chain MAP, OWASP SAMM)
- Developer training platforms (Security training platforms, etc.)

---

## Process Maturity Review

### Industry Frameworks

| Framework | Type | Description |
|-----------|------|-------------|
| **OWASP SAMM** | Open Source | Software Assurance Maturity Model - community standard |
| **SLSA** | Open Source | Supply-chain Levels for Software Artifacts - build integrity |
| **Black Duck BSIMM15** | Commercial | Building Security In Maturity Model v15 - data-driven benchmarking |
| **Software Supply Chain MAP** | Commercial | Maturity Assessment Program for supply chain security |

> **Recommendation:** OWASP SAMM and SLSA are widely accepted open standards. For comprehensive benchmarking with industry data, use **Black Duck BSIMM15** and **Software Supply Chain MAP**.

---

### Black Duck BSIMM15 (Recommended)

[BSIMM15](https://www.blackduck.com/services/security-program/bsimm-maturity-model.html) is a data-driven maturity model based on observations from 130+ organizations.

#### BSIMM Domains & Practices

| Domain | Practices | AppSec Relevance |
|--------|-----------|------------------|
| **Governance** | Strategy & Metrics, Compliance & Policy, Training | Program management, policies |
| **Intelligence** | Attack Models, Security Features & Design, Standards & Requirements | Threat intelligence, secure design |
| **SSDL Touchpoints** | Architecture Analysis, Code Review, Security Testing | SAST, DAST, design review |
| **Deployment** | Penetration Testing, Software Environment, Configuration & Vulnerability Management | Runtime security, operations |

#### BSIMM Maturity Levels

| Level | Description | Characteristics |
|-------|-------------|-----------------|
| **Level 1** | Emerging | Ad-hoc activities, basic practices in place |
| **Level 2** | Maturing | Defined processes, consistent execution |
| **Level 3** | Optimizing | Metrics-driven, continuous improvement, industry-leading |

#### Why BSIMM15 Over OWASP SAMM
- Data-driven: Based on real-world observations from 130+ firms
- Benchmarking: Compare against industry peers (finance, tech, healthcare)
- Prescriptive: Specific activities ranked by adoption frequency
- Updated annually: BSIMM15 reflects current practices

---

### Software Supply Chain Maturity Assessment MAP (Recommended)

Black Duck's Supply Chain MAP assesses maturity across the software supply chain lifecycle.

#### MAP Assessment Domains

| Domain | Focus Areas | AppSec Relevance |
|--------|-------------|------------------|
| **Sourcing** | Vendor assessment, OSS selection criteria, license compliance | SCA, dependency management |
| **Ingestion** | Component validation, vulnerability scanning, SBOM generation | SBOM, artifact verification |
| **Development** | Secure coding, CI/CD security, build integrity | DevSecOps, SLSA compliance |
| **Distribution** | Artifact signing, provenance, release security | SLSA, supply chain integrity |
| **Operations** | Continuous monitoring, vulnerability response, EOL management | Runtime SCA, patch management |

#### MAP vs SLSA

| Aspect | SLSA | Supply Chain MAP |
|--------|------|------------------|
| **Scope** | Build integrity focus | End-to-end supply chain |
| **Type** | Open framework (levels 1-4) | Commercial assessment service |
| **Output** | Compliance level | Maturity score + roadmap |
| **Benchmarking** | Self-assessment | Industry comparison data |

> **Use Together:** SLSA for build integrity compliance, Supply Chain MAP for comprehensive maturity assessment.

---

### How to Use for Compliance Mapping
- Map RMIT controls to BSIMM15 practices for AppSec maturity
- Map supply chain controls to Supply Chain MAP domains
- Use SLSA levels for build/artifact integrity requirements
- Benchmark against industry peers using BSIMM data
- Create improvement roadmap based on assessment gaps

---

## Staff AppSec Training

Developer and staff security training is a core AppSec practice.

### Training Categories (In Scope)

| Category | Description | Examples |
|----------|-------------|----------|
| **Secure Coding** | Language-specific secure coding practices | OWASP Top 10, CWE/SANS Top 25, language-specific pitfalls |
| **Security Champions** | Embedded security advocates in dev teams | Champion programs, security guild |
| **Threat Modeling** | Application-focused threat identification | STRIDE, PASTA, attack trees |
| **Tool Training** | Using AppSec tools effectively | SAST/DAST interpretation, IDE plugins |
| **Security Requirements** | Writing and validating security requirements | Abuse cases, security user stories |
| **Incident Response (Dev)** | Developer role in security incidents | Vulnerability remediation, hotfix procedures |

### Training Platforms & Resources

| Type | Examples |
|------|----------|
| **Interactive Labs** | OWASP WebGoat, Hack The Box, TryHackMe, PentesterLab |
| **E-Learning** | Secure Code Warrior, Checkmarx Codebashing, Veracode Security Labs |
| **Certifications** | CSSLP, GWEB, CASE (Certified Application Security Engineer) |
| **Internal Programs** | Lunch & learns, CTF competitions, bug bounty participation |

### Training Metrics to Track
- % of developers completing secure coding training
- Time to remediate vulnerabilities (before/after training)
- Security defect density trends
- Security champion coverage per team

### NOT Training (Out of Scope)
- General security awareness (phishing, password hygiene) - this is InfoSec, not AppSec
- Physical security training
- Compliance/audit training (unless code-specific)

---

## Practical ROI: AppSec vs Better Alternatives

Even if a control *could* technically be addressed with AppSec tools, there's often a more practical industry approach. Always ask: **"What's the common/cost-effective solution?"**

### When NOT to Use AppSec (Better Alternatives Exist)

| Control Area | Overthinking (AppSec) | Better Approach (Industry Standard) |
|--------------|----------------------|-------------------------------------|
| **Endpoint/Device Security** | Scan code on each end device | Endpoint Management (MDM, EDR, UEM) |
| **SST/ATM Security** | SAST on ATM application code | Device hardening + application whitelisting |
| **Kiosk Hardening** | Code analysis of kiosk apps | OS hardening (CIS Benchmarks) + kiosk mode |
| **Antivirus/Malware** | Build custom detection in code | Commercial AV/EDR solutions |
| **Network Segmentation** | Application-level network code | Firewall/SDN configuration |
| **DDoS Protection** | Rate limiting in every app | Cloud DDoS service (Cloudflare, AWS Shield) |
| **Full Disk Encryption** | Encrypt in application code | OS-level encryption (BitLocker, LUKS) |
| **BIOS/Firmware Security** | N/A | Hardware vendor tools, secure boot |
| **Physical Tamper Detection** | N/A | Physical security systems, sensors |
| **Data Center Security** | N/A | Facility security, SOC 2 audits |
| **General Security Awareness** | N/A | HR/Training platforms |

### Decision Rule

```
IF control can be solved by:
  - Device/endpoint management → NOT AppSec (use MDM/EDR)
  - OS/platform configuration  → NOT AppSec (use hardening standards)
  - Network infrastructure     → NOT AppSec (use firewall/SDN)
  - Physical security          → NOT AppSec (use facility controls)
  - Commercial off-the-shelf   → NOT AppSec (use vendor solution)
THEN mark as "Out of AppSec Scope - use [alternative]"

ONLY use AppSec when:
  - You are building/modifying the application code
  - You control the source code or container images
  - You are integrating security into CI/CD pipeline
  - Vulnerabilities are in YOUR code or dependencies
```

### Quick ROI Test

Before mapping a control to AppSec, ask:

1. **"Do we write/control this code?"** → No = Not AppSec
2. **"Is there a commercial product for this?"** → Yes = Probably not AppSec
3. **"Would a platform team handle this?"** → Yes = Infrastructure, not AppSec
4. **"Is this about our application vulnerabilities?"** → Yes = AppSec

---

## What is NOT AppSec (Out of Scope - "Overthinking")

### 1. Physical Security
**Never map these to AppSec tools:**
- CCTV/surveillance cameras
- Physical locks, keys, tamper detection
- Physical access control (badges, biometrics for building entry)
- Data center physical security
- Hardware theft protection
- Environmental controls (fire, flood, temperature)
- Chain of custody for physical media
- Secure disposal of physical equipment

### 2. Network Security
**Never map these to AppSec tools:**
- Firewall configuration and management
- IDS/IPS (Intrusion Detection/Prevention Systems)
- Network segmentation and zones
- DDoS protection (clean pipe, traffic scrubbing)
- VPN and network tunnels (unless application-level mTLS)
- Perimeter defense
- Network packet capture/forensics
- Router/switch security
- Network monitoring tools

### 3. Data/Process Security (Non-Application)
**Never map these to AppSec tools:**
- Data classification policies (unless automated in code)
- Data retention policies
- Backup and recovery procedures
- Business continuity planning
- Incident response procedures (organizational)
- Security awareness training (general)
- Governance frameworks (unless technical implementation)
- Audit procedures (organizational)

---

## Decision Criteria for Borderline Cases

| If the control mentions... | AppSec? | Reason |
|---------------------------|---------|--------|
| Source code, binaries, containers | YES | Core AppSec target |
| API security testing, secure coding | YES | AppSec practice |
| Firewall rules, IPS signatures | NO | Network security |
| Physical locks, CCTV, tamper | NO | Physical security |
| Encryption in code/libraries | YES | Application crypto |
| Network encryption (IPSec, VPN) | NO | Network security |
| Container image scanning | YES | AppSec tooling |
| Server hardening (OS-level) | NO | Infrastructure security |
| Application hardening (code) | YES | AppSec practice |
| WAF rules for applications | YES | Application protection |
| DDoS at network level | NO | Network security |
| Rate limiting in API code | YES | Application security |
| Secure coding training for devs | YES | AppSec training |
| General phishing awareness | NO | InfoSec, not AppSec |
| Security maturity assessment (BSIMM, MAP) | YES | AppSec governance |
| Security policy documents | MAYBE | Only if tied to code/SDLC |

---

## Keywords to Watch (Likely Out of Scope)

- "physical", "premises", "data center"
- "firewall", "IDS", "IPS", "perimeter"
- "network segmentation", "zones", "DMZ"
- "DDoS", "clean pipe", "traffic scrubbing"
- "CCTV", "surveillance", "tamper"
- "hardware", "equipment disposal"
- "backup", "recovery", "BCM/BCP"