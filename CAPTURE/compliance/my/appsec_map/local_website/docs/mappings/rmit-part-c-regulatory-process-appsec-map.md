# RMIT Part C: Regulatory Process - AppSec Mapping

## Control 16.1-16.2
**Type:** S (Standard)
**Requirement:** Notify BNM prior to new digital services. First-time notification must include risk assessment, security arrangements, terms/conditions, privacy policy, third-party arrangements.

### AppSec Mapping

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| Threat Modeling | Security risk assessment | Risk assessment documentation |
| SAST/DAST | Security scan reports | Security arrangements evidence |
| SCA | Third-party dependency analysis | Third-party arrangements |
| SBOM | Component inventory | Document components |

---

## Control 16.3-16.4
**Type:** S (Standard)
**Requirement:** Simplified notification for minor enhancements per Appendix 6. Non-simplified requires independent external assurance and CISO/board confirmation.

### AppSec Mapping

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| Application Pentest | Independent third-party pentest | External security assurance |
| Threat Modeling | Change impact assessment | Risk assessment of changes |
| DevSecOps | Security sign-off workflow | CISO confirmation |

**Notes:** Requires **external** independent assurance - internal scans alone not sufficient.

---

## Control 16.5-16.7
**Type:** S (Standard)
**Requirement:** External party must be competent; provide documents to BNM when required.

### AppSec Mapping

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| Application Pentest | Certified pentest firms | Competent assessors |
| DevSecOps | Documentation repository | Archive security artifacts |

**Notes:** **Industry practice:** Use CREST-certified or OSCP-certified application security testers.

---

## Control 17.1
**Type:** S (Standard)
**Requirement:** Consult BNM prior to first-time public cloud or emerging technology adoption for critical systems. Requires comprehensive risk assessment, CISO/board confirmation, third-party pre-implementation review.

### AppSec Mapping

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| Container Security | Container/image scanning | Cloud workload security |
| IaC Security | Terraform/CloudFormation scanning | Infrastructure security |
| SCA | Cloud service dependency analysis | Third-party cloud risk |
| Threat Modeling | Cloud/emerging tech threat modeling | Comprehensive risk assessment |

---

## Control 17.2-17.5
**Type:** S (Standard)
**Requirement:** Subsequent cloud adoptions require notification; include roadmap in annual outsourcing plan.

### AppSec Mapping

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| Container Security | Continuous container scanning | Ongoing cloud security |
| DevSecOps | Cloud security policy enforcement | Framework implementation |

---

## Control 18.1-18.2
**Type:** S (Standard)
**Requirement:** Perform gap analysis against RMIT requirements within 90 days. Develop action plan with timeline.

### AppSec Mapping

| Category | Tool/Practice | How It Addresses the Control |
|----------|--------------|------------------------------|
| Maturity Assessment | BSIMM15, OWASP SAMM | Assess AppSec control gaps |
| SAST/DAST/SCA | Current state assessment | Baseline security posture |
| DevSecOps | Remediation tracking | Track gap closure |
