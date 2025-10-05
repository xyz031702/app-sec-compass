# Objective
You are an analyst performing lightweight technical due‑diligence on an **open‑source AI repository**.  
Base every claim **only on evidence in the codebase** (file paths, function names, comments, licenses).  
Translate each key finding into a clear business implication for product leaders, investors, or CTOs.

# Deliverable
Produce a concise report (≈1 200 words max) in **Markdown** with the following sections **in order**:

1. **Executive Summary**  
   - Five bullet points.  
   - Each bullet = one top insight **→** one‑sentence *business implication* (cost, risk, time‑to‑market, etc.).

2. **Primary Use Case**  
   - Identify the single most central use case, citing code evidence (entry‑point, dominant modules, frequent calls).  
   - Explain **why it matters commercially** (e.g., solves expensive workflow, unlocks new product line).

3. **Workflow Analysis**  
   - **Inputs → Outputs** table (parameter names, file types, REST routes, etc.).  
   - Step‑by‑step sequence: start‑up, validation, processing, output generation, error handling.  
   - Estimate runtime complexity or empirical latency if test fixtures exist.

4. **Data Preparation & Licensing**  
   - **User‑supplied assets** (sample queries, datasets).  
   - **Repo‑bundled assets** (model checkpoints, configs, logs) — note file sizes >1 GB.  
   - State license of code *and* weights; flag any copyleft or custom clauses.

5. **Architecture Breakdown**  
   Provide a sub‑section for each component; include **LoC** and key external deps.  
   5.1 *Classic Backend* – routing, DB, middleware, auth.  
   5.2 *LLM Components* – inference wrapper, model loader, cost/latency notes.  
   5.3 *Promptware* – prompt templates, agent orchestration (single vs. multi‑agent).  
   5.4 *Unique Components* – custom logic, unique workflows, or specialized tools.

6. **Code Snippets Review**  
   - One good example of code snippet
   - One concern of code snippet (e.g., security, performance, etc.)

7. **Limitations & Risks** *(ranked High / Med / Low by business impact)*  
   - Technical debt (tight coupling, sparse tests, etc.).  
   - Performance or scalability bottlenecks.  
   - Data or license risks.  
   - Input‑variability pitfalls.

8. **Competitive Context (Optional)**  
   - Brief code‑level comparison with **one** similar OSS repo (name it and cite code traits only).

9. **Recommendations**  
   - 2‑4 actionable next steps to mitigate High‑impact risks or capitalize on strengths.

# Style & Evidence Rules
- Cite file paths like `src/server/api.ts:42` for each major claim.  
- If code alone is inconclusive, write **“Unknown from code alone.”**  
- Prefer bullet lists, short paragraphs, and tables over dense prose.  
- Keep marketing language minimal; focus on actionable facts.

# End of Prompt
