# AI Threat Intelligence Data Sources

## 1. Aggregators & High-Velocity News (The "Triage" List)

**Definition:** Speed and trend-spotting. Use these to find out WHAT happened.

- **The Hacker News:** Primary for vulnerability summaries and RCEs
- **TLDR Information Security:** High-signal curated news (includes a dedicated AI security section)
- **Dark Reading (AI Section):** Deep coverage of enterprise AI breaches
- **CVE Website:** Filtered for keywords: LLM, Prompt Injection, RAG, Vector, LangChain

## 2. Primary Research & Labs (The "Origin" List)

**Definition:** The entities finding the bugs or building the models. Use these for technical HOW-TOs.

### Frontier Creators (The Labs)
- **OpenAI / Anthropic Blogs:** Specifically their "Cybersecurity" and "Red Teaming" reports (e.g., Anthropic's Constitutional Classifiers or OpenAI's Disrupting Malicious Use)
- **Meta AI Research:** Critical for "Open Source" threats and weight poisoning

### The Cloud Giants (Inference Infrastructure)
- **Google Threat Intelligence Group (GTIG):** The leading source for real-world AI malware (e.g., PROMPTSTEAL)
- **Microsoft Security Response Center (MSRC):** Specifically for "Atlas" and prompt injection hardening

### Cybersecurity Specialists
- **Protect AI (Huntr):** The world's first AI bug bounty platform
- **HiddenLayer:** Research on model theft, weight extraction, and inference attacks
- **Datadog Security Labs / AppOmni:** Specialists in "Agentic AI" and SaaS-based injection

### The Big 4 Auditors
- **Deloitte (Tech Trends) / PwC (Digital Trust):** Excellent for "AI Assurance" and reports on where corporate AI agents are failing in production
- **KPMG (AI Trust):** Focuses on governance and "Trusted AI" marks

## 3. Academic & Pre-Print Repositories (The "Horizon" List)

**Definition:** Future threats (6–12 months out). Use these for mathematical proofs of vulnerability.

- **arXiv:** Focus on Adversarial ML and Robustness categories
- **Hugging Face "Papers" / OpenReview:** Better curated than raw arXiv for high-impact security papers
- **Conferences:** NDSS, IEEE, AAAI, and USENIX Security

## 4. Governance & Standards Bodies (The "Rulebook" List)

**Definition:** Frameworks and scoring. Use these for compliance and risk metrics.

- **NIST:** AI RMF and Cyber AI Profile (NIST IR 8596)
- **OWASP:** Top 10 for LLM Applications and AIVSS scoring
- **Singapore MAS / CSA / IMDA:** Leading the world in "Securing Agentic AI" guidelines
- **MITRE ATLAS:** The "ATT&CK" for AI. Essential for mapping tactics

## 5. Tooling (The "Pratice" List)

**Definition:** Software and expert assessments. Use these to find resources for testing.

### Open Source Tooling
- **Giskard:** RAG testing
- **Promptfoo:** Red Teaming
- **Microsoft's PyRIT:** Security testing framework

## 6. Community Signals (The "Wildcard" List)

**Definition:** Raw, unverified reports. Use these for early detection of zero-days.

- **Reddit (r/LocalLLM):** First place users report when a model's guardrails are "soft-broken"
- **Hugging Face Discussions:** Check the "Community" tabs on popular models for user reports of malicious weights or unexpected data leakage
- **Jailbreak Chat:** Monitoring the latest "jailbreak" payload trends

## What's New in this Version

- **Merged Big 4 into Category 5:** Their value is in "Evaluation" and "Assurance" rather than original vulnerability discovery
- **Merged Cloud Giants into Category 2:** They are "Primary Research" because they own the infrastructure where the threats are caught
- **Hugging Face Integration:** Added to both Category 3 (Papers) and Category 6 (Community) to reflect its dual role as a research hub and a "Wildcard" signal

---

*Would you like me to create a "Bi-Weekly Reading Workflow" to help you process these sources in under 2 hours?*