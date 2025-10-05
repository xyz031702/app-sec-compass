# Investigation Framework for Malicious Code in AI Models

## Executive Summary
Organizations adopting AI models must remain vigilant against **malicious code embedded in AI systems**. This framework provides a comprehensive strategy to detect and analyze backdoors and malware across all stages of an AI model’s lifecycle, including hidden logic in model weights, poisoned training data, and runtime code injection. Key steps combine static scanning (e.g., [ModelScan](https://github.com/protectai/modelscan)), sandboxed execution monitoring, and behavioral testing (e.g., Neural Cleanse) to uncover hidden model functionalities. Each step includes clear success metrics and escalation criteria, with potential pitfalls and mitigation tactics. A risk–benefit matrix compares supply‑chain controls, automated scanning, and runtime sandboxing, enabling enterprises to choose a layered defense-in-depth approach.

---
## 2  Analysis Framework

### 2.1 Scope & Threat Model
* **Scope**: Enterprise‑deployed models (open‑source or proprietary) where model files are accessible.  
* **Threat actors**: External attackers, insider threats, and supply‑chain compromises.  
* **Attack surfaces**:  
  1. **Embedded logic in model weights** (Trojan/backdoor).  
  2. **Poisoned training data**.  
  3. **Runtime code injection** (e.g., Pickle RCE).  

### 2.2 Source Selection & Literature‑Review Plan
1. **Academic papers** (e.g., [BadNets (Gu et al., 2017)](https://arxiv.org/abs/1708.06733), [Goldwasser et al., 2022](https://arxiv.org/abs/2204.06974), [Ning et al., 2025](https://arxiv.org/abs/2504.11182)).  
2. **Industry reports** (e.g., [Trail of Bits “Sleepy Pickle” blog](https://trailofbits.com/2024/03/14/sleepy-pickle/)).  
3. **Security advisories & CVE feeds** (TensorFlow, PyTorch).  
4. **Community forums & MITRE ATLAS**.  
5. Continuous monitoring of arXiv feeds (`cs.CR`, `cs.LG`) and security news (Dark Reading, HackerNews).

### 2.3 Data / Artifact Collection Strategy
* Collect **model files** & SHA‑256 hashes.  
* Gather **training data/logs** when available.  
* Snapshot **runtime environment** (OS, library versions).  
* Record **sandbox execution logs**, network traces, and anomalous inputs/outputs.  
* Store artefacts in an evidence repository with chain‑of‑custody metadata.

### 2.4 Methodology (Step‑by‑Step)
| Step | Purpose | Core Techniques & Tools |
|------|---------|-------------------------|
| 1. Static scan | Detect unsafe opcodes in model files | **ModelScan**, **[Fickling](https://github.com/trailofbits/fickling)** |
| 2. Sandbox load | Observe runtime behavior safely | Docker + Firejail, `strace`, Sysdig/Falco |
| 3. Behavioral tests | Uncover hidden triggers/backdoors | **IBM ART** Neural Cleanse, STRIP, adversarial fuzzing (TextAttack/Foolbox) |
| 4. Data forensics | Spot poisoned samples | Spectral Signatures, manual review |
| 5. Code & deps audit | Find malicious hooks | **Bandit**, `pip audit`, typosquat scan |
| 6. Mitigation verify | Confirm & remove backdoors | Fine‑pruning, NAD, retraining |

### 2.5 Metrics / Success Criteria
* **Static scan**: Zero unsafe opcodes or hash mismatch.  
* **Sandbox**: No outbound network / unexpected syscalls.  
* **Neural Cleanse**: No trigger size outlier > 3 MAD.  
* **STRIP**: Prediction variance on perturbed inputs > 10 %.  
* Detailed thresholds per step enable pass/fail gating.

### 2.6 Tools & Resources
* **ModelScan 0.1.2** – <https://github.com/protectai/modelscan>  
* **Fickling 0.6.0** – <https://github.com/trailofbits/fickling>  
* **Adversarial Robustness Toolbox 1.14** – <https://github.com/Trusted-AI/adversarial-robustness-toolbox>  
* **TextAttack**, **Foolbox**, **Strace**, **Sysdig**, **Bandit**, **Falco**.  
* **Safetensors** format – <https://huggingface.co/docs/safetensors/index>  

### 2.7 Potential Pitfalls & Mitigations
* **False positives** → cross‑verify with alternate tools & human review.  
* **False negatives** → layered defense (static + dynamic + behavioral).  
* **Resource limits on large models** → chunked scans & selective testing.  
* **Undetectable backdoors ⚠️** → supplement with supply‑chain trust & runtime sandboxing.

### 2.8 Escalation Points
1. Malicious opcode detected → Incident Response.  
2. Anomalous sandbox behavior → Security & ML experts.  
3. Backdoor trigger found → Product owner & CISO.  
4. Suspicious training data → Data engineering team.  
5. High‑severity code findings → Software security audit.  

---
## 3  Evidence Pack (Illustrative)
* Model file hash list (`SHA‑256`).  
* ModelScan JSON report.  
* Fickling disassembly snippet.  
* Strace log highlighting forbidden syscall.  
* Neural Cleanse trigger images / token sequences.  
* CSV of poisoned training samples.  
* Signed PDF expert assessment.

---
## 4  Risk–Benefit Matrix

| Solution Path | Benefits | Risks |
|---------------|----------|-------|
| **Supply‑chain control**<br>(signed & safetensors models) | Authenticated origin; mitigates Pickle RCE | Limited model choice; signatures can be compromised |
| **Automated scanning pipeline** | Detects code & neural backdoors before prod | Resource intensive; tuning needed to reduce false alerts |
| **Runtime sandboxing & monitor** | Contains unknown threats; real‑time alerts | Doesn’t stop logic backdoors; performance overhead |

---
## 5  Annotated Bibliography

1. Gu, T., Dolan‑Gavitt, B., & Garg, S. (2017). *BadNets: Identifying Vulnerabilities in the Machine Learning Model Supply Chain*. <https://arxiv.org/abs/1708.06733>  
2. Trail of Bits. (2024). *Exploiting ML Models with Pickle File Attacks – Sleepy Pickle*. <https://trailofbits.com/2024/03/14/sleepy-pickle/>  
3. Hugging Face. (2023). *Security Note: Pickle Scanning & Safetensors*. <https://huggingface.co/docs/hub/security>  
4. King, C. (2023). *ModelScan: Open Source Protection Against Model Serialization Attacks*. <https://github.com/protectai/modelscan>  
5. Goldwasser, S., et al. (2022). *Planting Undetectable Backdoors in Machine Learning Models*. <https://arxiv.org/abs/2204.06974>  
6. Ning, L., et al. (2025). *Exploring Backdoor Attack and Defense for LLM‑empowered Recommendations*. <https://arxiv.org/abs/2504.11182>  
7. Nelson, N. (2024). *‘Sleepy Pickle’ Exploit Subtly Poisons ML Models*. Dark Reading. <https://www.darkreading.com/editorial/sleepy-pickle-poisons-ml-models>  

---
*© 2025 Security Research Analyst Framework*

