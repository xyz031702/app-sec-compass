whats the threat
# From Component Scan to SBOM:  Developer's Perspective over PCI-DSS 6.4.3 and 11.6.1


## The Threat: Application & File Tampering for Malignant Intent

![XSS Attack Illustration](https://evalian.co.uk/wp-content/uploads/2022/03/XSS-attacks-what-is-cross-site-scripting.png)

### **What is at Risk**
* **Malicious code injection** into payment applications for cardholder data theft
* **Silent file tampering** in critical payment systems for payment processing disruption
* **Unauthorized modifications** to transaction processing logic for malicious transactions

### **Business Impact:**
* **$4.45M average** breach cost ([IBM Security 2023 Report](https://newsroom.ibm.com/2023-07-24-IBM-Report-Half-of-Breached-Organizations-Unwilling-to-Increase-Security-Spend-Despite-Soaring-Breach-Costs))
* **Payment processing disruption** → $9.3M/hour in banking losses ([UptimeRobot 2024](https://uptimerobot.com/blog/hidden-costs-of-downtime/))
* **Regulatory fines** $425M (Equifax) to $500K+ per violation ([Compyl 2025](https://compyl.com/blog/understanding-pci-dss-fines-and-penalties/))
* **Customer trust erosion** → 66% won't trust breached companies ([Security Magazine 2024](https://www.securitymagazine.com/articles/100296-66-of-consumers-would-not-trust-a-company-following-a-data-breach))

## Attack Demo1: Injection due to unsafe deps (jQuery CVE-2019-11358)

### **The Vulnerability**
* **CVE-2019-11358**: Prototype pollution in jQuery `$.extend()` function (last update, 11/20/2024, NVD)
* **Affected versions**: jQuery < 3.4.0 (released April 2019)
* **Attack vector**: Malicious `__proto__` properties in user data
* **72.8% of all websites** still use jQuery ([W3Techs 2024](https://w3techs.com/technologies/details/js-jquery))
* **'Mature' codebases** often stuck on vulnerable versions
* **Major sites affected**: Microsoft, Yahoo, WordPress, Adobe, Samsung

### **Demo Scenario**
* **Improper dependency management** → Vulnerable jQuery 3.3.1
* **Payment form exploitation** → Data theft via prototype pollution
* **Business impact** → Payment processing disruption

![Attack Demo](cases/pci-dss-643/demo/Screenshot%20(1048).png)


## Attack Demo2: XSS Injection (Script Tampering)

### **The Vulnerability**
* **Direct XSS via `innerHTML`** - No external dependencies required
* **Attack vector**: Malicious localStorage data rendered as HTML
* **File tampering**: External scripts inject payloads into browser storage

### **Demo Scenario**
* **Script tampering** → Malicious payload seeded via `seed.html`
* **Payment form exploitation** → SVG onload steals card data in real-time
* **File integrity bypass** → No change detection on localStorage manipulation
* **Business impact** → Silent payment data theft during checkout 


## Real World Case Studies (2022-2025)

### **1. British Airways Magecart Attack - 2022-2024**
* **Attack**: Script tampering via compromised third-party payment scripts
* **Impact**: 400,000+ customer payment cards stolen during checkout process
* **Root cause**: Malicious JavaScript injected into payment forms via supply chain compromise
* **Business impact**: £20M ICO fine, ongoing customer compensation claims

### **2. Ticketmaster Supply Chain Attack - June 2024**
* **Attack**: Compromised Inbenta chatbot script injected card skimming code
* **Impact**: Payment data from 40,000+ customers stolen via tampered JavaScript
* **Root cause**: Third-party script modification without integrity monitoring
* **Business impact**: $1.65M settlement, mandatory security upgrades

### **3. Newegg Magecart Script Injection - September 2022**
* **Attack**: Payment page JavaScript tampering for one month undetected
* **Impact**: Credit card data stolen from customers during checkout
* **Root cause**: Compromised payment processing scripts, no file integrity monitoring
* **Business impact**: Customer trust erosion, forced security infrastructure overhaul


## Defend the threat
### **Root Cause Overview**

**Development Issues:**
* **Vulnerable dependencies** → Outdated libraries with known CVEs (jQuery 3.3.1)
* **Script tampering** → Malicious code injection into legitimate files, due to unsafe file handling, no proper input validation

**Flow Flaws:**
* **Supply chain attacks** → Compromised third-party scripts/CDNs
* **Insufficient file integrity monitoring** → No detection of unauthorized changes
* **Missing Content Security Policy** → No restrictions on script execution sources

### **App Scan as A Pre-requisite**

**Component Scan (SCA):**
* **Detects vulnerable dependencies** → Identifies jQuery 3.3.1 CVE-2019-11358
* **License compliance** → Ensures legal usage of third-party components
* **Critical for Demo1** → Would have prevented prototype pollution attack

**Static Analysis (SAST):**
* **Code vulnerability detection** → Finds unsafe `innerHTML` usage patterns
* **Input validation flaws** → Identifies XSS injection points
* **Critical for Demo2** → Would have flagged dangerous localStorage rendering

**Dynamic Analysis (DAST):**
* **Runtime attack simulation** → Tests actual XSS payload execution
* **Real-world validation** → Confirms exploitability of found vulnerabilities
* **Critical for both demos** → Validates attack scenarios work in practice

**SBOM Inventory:**
* **Supply chain visibility** → Maps all components, scripts and dependencies
* **Risk surface analysis** → Identifies attack vectors across entire application
* **Change detection baseline** → Enables monitoring for unauthorized modifications

### **Compliance as a Teacher (Not a Judge)**

![Compliance Framework](https://cdn.prod.website-files.com/65bd91e2ec9fa84fd2a4b3be/6798fa3ac56352a40656aa66_Main%20Image.jpg)

**PCI-DSS Requirements Guide Us:**
* **6.4.3**: Implement change-detection mechanisms to ensure payment application integrity
* **11.6.1**: Continuously monitor critical files for unexpected changes to detect tampering

## SBOM Baseline (Align with 6.4.1)
* Developer's view over 6.4.3:  we want to exclude unstrusted scripts from production
  - we need a inventory of trusted scripts that consists of production
  - we need a security profile (meta info, vulnerabilities, hash) of each script
* SBOM baseline is a snapshot of the inventory and security profile of the scripts at a specific point in time
* Wait, what is a 'script'?
  - a library, a dependency can import scripts (e.g. jQuery, React, Bootstrap. E.g.: anything in package.json)
  - a remote script (e.g. a custom script, a third-party script, etc. E.g.: <script src="https://example.com/script.js"></script>)
  - a local file (e.g. a custom file, a third-party file, etc. E.g.: <script src="./script.js"></script>)
  - a embeded code snippet (e.g. <script>alert('xss')</script>)
  !! How to use Blackduck to generate a quality SBOM baseline for the above situations

## Enforce Integrity (Align with 6.4.3)

![CDN SRI Implementation](https://beautifycode.net/images/cdn-sri.png)

### **3-Step Integrity Enforcement:**

**1. Implement CSP + SRI Controls**
* **Content Security Policy** → Restrict script sources to trusted domains
* **Subresource Integrity** → Verify script content hasn't been tampered
* **Example**: `<script src="jquery.js" integrity="sha256-abc123" crossorigin="anonymous">`

**2. Automated SAST Detection**
* **BlackDuck SAST scanning** → Identifies missing CSP headers
* **Code quality gates** → Flags scripts without integrity attributes
* **Developer feedback** → Real-time alerts for security violations

**3. SBOM-Based Hash Generation**
* **Baseline inventory** → Known good scripts with verified hashes
* **Automated tagging** → CI/CD adds integrity hashes from SBOM
* **Version control** → Track hash changes for security review

### **Demo Connection:**
* **Demo1 Prevention** → CSP blocks unauthorized jQuery versions
* **Demo2 Prevention** → SRI detects localStorage script tampering

## Change Monitoring (Align with 11.6.1)

### **Why Monitor Production Scripts?**

**A Possible Case:**
* **CDN pollution** → CDN may be compromised and drops CSP headers
* **Security bypass** → CSP/SRI protections become ineffective
* **Silent attacks** → Malicious scripts load without detection
* **Need**: Monitor actual script changes in production environment

### **Monitoring Overview:**

**What to Monitor:**
* **Security headers** → CSP, SRI presence in production
* **Script content** → Actual JavaScript files served to users
* **Page integrity** → Detect unauthorized modifications

**How to Monitor:**
* **External scanning** → Check production pages weekly
* **Header validation** → Verify CSP headers are present
* **Script comparison** → Compare production scripts vs. baseline
* **Automated alerts** → Notify when changes detected
