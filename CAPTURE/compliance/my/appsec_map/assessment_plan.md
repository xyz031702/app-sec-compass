# AppSec Gap Assessment Workshop Plan

## Objective

Design a 10-15 minute assessment that produces **alignment** between facilitator and attendees (CISO, CIO, tech leaders) on the current state of Application Security capabilities and measurement gaps.

---

## Earning Buy-In: Why Should They Care?

### The Credibility Problem

Senior leaders have seen too many:
- Vendor assessments designed to sell products
- Consultants with predetermined conclusions
- Generic frameworks that ignore their context
- Exercises that produce reports, not action

### How This Assessment Is Different

| Their Concern | How We Address It |
|---------------|-------------------|
| "Is this relevant to us?" | Directly mapped to BNM RMIT requirements they must comply with |
| "Is this credible?" | Based on BSIMM15 - data from 130+ firms, not opinion |
| "Will my input matter?" | Their ratings drive the discussion, not our slides |
| "Am I being tested?" | No right answers - we're surfacing perception gaps |
| "What do I get out of this?" | Immediate visibility into where leadership is aligned vs. misaligned |

### Value Proposition by Role

| Role | What They Get |
|------|---------------|
| **CISO** | Validation of security concerns, data to support budget requests, peer alignment |
| **CIO** | Visibility into security maturity vs. business priorities, risk context |
| **Tech Leaders** | Voice in security priorities, surfacing of real blockers, realistic expectations |

### The Key Insight to Share

> "We're not here to grade you. We're here to find out where you **agree** on the gaps and where you **disagree**. The disagreements are the most valuable - that's where misalignment causes problems."

---

## How to Position the Assessment (Facilitator Script)

### Opening (Before Handing Out Forms)

> "Before we start, let me be clear about what this is and isn't.
>
> **This is NOT:**
> - A test with right or wrong answers
> - A way to judge your organization
> - A checklist to sell you tools
>
> **This IS:**
> - A way to surface where leadership sees things differently
> - Based on BSIMM15, the industry standard used by 130+ organizations
> - Directly mapped to RMIT requirements you'll need to address
>
> The most valuable outcome is when the CISO rates something a 2 and the Dev Lead rates it a 0. That gap is where real problems hide.
>
> Please be honest. A low score is useful. A dishonest high score wastes everyone's time."

### Why BSIMM15 Matters (Credibility Anchor)

If challenged on "where does this come from?":

> "The maturity levels come from BSIMM15 - the Building Security In Maturity Model, version 15. It's published by Black Duck and based on direct observation of 130+ software security programs at companies like Adobe, Microsoft, PayPal, and major banks. It's not our opinion - it's what the industry actually does."

**Source to cite:** [BSIMM15](https://www.blackduck.com/services/security-program/bsimm-maturity-model.html)

### Why RMIT Matters (Regulatory Anchor)

> "The eight capabilities we're assessing map directly to Bank Negara's RMIT requirements - specifically Chapters 9-13 and Appendices 3, 4, 5, 7, 8, and 10. This isn't theoretical - these are compliance gaps that BNM will assess."

---

## Anti-Patterns: What NOT to Do

| Don't Do This | Do This Instead |
|---------------|-----------------|
| Hand out forms without context | Explain why this matters first |
| Use jargon without definition | Define each capability clearly |
| Collect forms and disappear | Discuss results immediately in the room |
| Present pre-made conclusions | Let their data drive the conversation |
| Make low scores feel like failure | Celebrate honesty, gaps are expected |
| Rush through facilitation | Take time on perception gaps |
| Promise tools will fix everything | Focus on process and people first |

---

## Making It Relevant to THEIR Context

### Pre-Workshop Research (Do This First)

Before the workshop, find out:

1. **What applications do they build?** (Web, mobile, APIs, internal tools)
2. **What's their development model?** (Waterfall, Agile, DevOps, outsourced)
3. **Recent incidents?** (Any breaches, near-misses, audit findings)
4. **Regulatory pressure?** (BNM findings, audit timeline, board concerns)

### Customize the Introduction

Use what you learned:

> "I understand you're building [mobile banking apps / API platform / etc.] and BNM has [upcoming audit / recent findings / etc.]. The eight capabilities we'll assess are specifically relevant to [mobile = Appendix 4, APIs = Appendix 5.E, etc.]."

This signals: "I did my homework. This isn't generic."

---

## The "So What" Test

Before each question, ask yourself:

| Question | Why Do They Care? |
|----------|-------------------|
| Rate your SAST maturity | RMIT 10.2 requires secure SDLC. Board will ask "do we scan code?" |
| Rate your SCA maturity | Supply chain attacks (Shai-Hulud, xz Utils) are in the news. RMIT App 8 requires this. |
| Rate your DevSecOps | Speed vs security trade-off. How do we ship fast AND secure? |
| Top 3 priorities | Forces them to choose. Reveals what they actually care about. |
| Biggest blocker | Gives them voice to share constraints. You're not assuming you know. |
| Success in 12 months | They define success, not you. This becomes their KPI. |

---

## Why Traditional Approaches Fail

| Approach | Problem |
|----------|---------|
| MCQ (Multiple Choice) | Tests knowledge, not reality. Attendees pick "correct" answers, not truthful ones. |
| Open Questions Only | Time-consuming, hard to aggregate, produces inconsistent data. |
| Yes/No Checklists | Binary thinking misses nuance. "We have SAST" could mean 1 app or 100 apps. |
| Self-assessment surveys | Without anchors, ratings are subjective ("What is a 3 vs 4?") |

---

## Recommended Approach: Anchored Maturity + Priority Alignment

### Design Principles

1. **Anchored scales** - Each level has concrete, observable criteria (no subjective 1-5)
2. **Role-based perspective** - Same questions, different viewpoints reveal gaps
3. **Forced prioritization** - Ranking prevents "everything is priority 1"
4. **Minimal open text** - Only where context is essential
5. **Immediate discussability** - Results can be compared in real-time

---

## Assessment Structure (Total: 12-15 minutes)

### Part A: Capability Maturity Rating (6-8 minutes)

**Instructions to attendees:**
> "Rate your organization's CURRENT state for each capability. Be honest - this is about alignment, not judgment. Use the maturity definitions provided."

#### Maturity Level Definitions (Print on assessment form)

| Level | Label | Definition |
|-------|-------|------------|
| 0 | Not Present | Capability does not exist or is ad-hoc only |
| 1 | Emerging | Capability exists but inconsistent. Used on some projects, not all. |
| 2 | Established | Capability is standardized. Defined process, consistent execution across teams. |
| 3 | Optimizing | Capability is metrics-driven. Continuous improvement, benchmarked against industry. |

#### Capabilities to Assess (8 items)

| # | Capability | What to Consider |
|---|------------|------------------|
| 1 | **Static Analysis (SAST)** | Code scanning in development. Integrated in IDE/CI? Coverage? |
| 2 | **Dynamic Testing (DAST)** | Runtime scanning of applications. Automated? Manual only? |
| 3 | **Dependency Scanning (SCA)** | Third-party library vulnerability detection. Coverage? Remediation process? |
| 4 | **Software Inventory (SBOM)** | Bill of materials for applications. Generated? Maintained? Used? |
| 5 | **DevSecOps Integration** | Security gates in CI/CD pipeline. Blocking? Advisory? None? |
| 6 | **Penetration Testing** | Application-focused pentesting. Frequency? Scope? Remediation? |
| 7 | **Secure Coding Training** | Developer security education. Mandatory? Measured? Effective? |
| 8 | **Vulnerability Management** | Process from discovery to remediation. SLAs? Tracking? Metrics? |

**Response format:** Circle one level (0, 1, 2, 3) for each capability.

---

### Part B: Investment Priority Ranking (2-3 minutes)

**Instructions:**
> "From the 8 capabilities above, select your TOP 3 priorities for investment in the next 12 months. Rank them 1, 2, 3."

| Priority | Capability # | Reason (optional, 3-5 words) |
|----------|--------------|------------------------------|
| 1st | ___ | |
| 2nd | ___ | |
| 3rd | ___ | |

---

### Part C: Blockers and Constraints (3-4 minutes)

**Two targeted questions only:**

**Q1: What is the single biggest barrier to improving AppSec in your organization?**
(Choose ONE)

- [ ] Budget/funding
- [ ] Lack of skilled staff
- [ ] Competing priorities
- [ ] Developer resistance
- [ ] Unclear ownership/accountability
- [ ] Legacy systems/tech debt
- [ ] Other: _______________

**Q2: What would success look like in 12 months?**
(One sentence - what measurable outcome would you want to report to the Board?)

_________________________________________________________________

---

## Facilitation Guide: How to Use Results

### Pre-Workshop Preparation

1. Print assessments (one per attendee)
2. Prepare a whiteboard/flipchart grid:

```
             SAST  DAST  SCA  SBOM  DevSecOps  Pentest  Training  VulnMgmt
CISO
CIO
Dev Lead 1
Dev Lead 2
...
```

3. Have colored markers ready (green=3, yellow=2, orange=1, red=0)

### During Workshop (After Assessment Collection)

**Step 1: Visual Mapping (5 min)**
- Ask each attendee to share their ratings
- Plot on the grid using colors
- Immediately visible: Where do ratings differ?

**Step 2: Gap Discussion (10-15 min)**
Focus on:
- **Perception gaps**: "CISO rated SAST as 2, Dev Lead rated it 0 - let's discuss"
- **Priority alignment**: "3 of 5 ranked SCA as priority 1 - is there consensus?"
- **Blocker patterns**: "4 of 6 said 'competing priorities' - what's competing?"

**Step 3: Alignment Summary (5 min)**
Capture:
- Agreed current state (consensus ratings)
- Agreed top 3 priorities
- Key blockers to address
- Success metrics for 12 months

---

## Alternative Formats

### Option A: Digital (Google Forms / MS Forms)

**Pros:** Instant aggregation, anonymous option, remote-friendly
**Cons:** Less discussable in real-time, harder to see group patterns

**Implementation:**
- Same questions as above
- Add "Role" dropdown (CISO, CIO, Dev Lead, etc.)
- Show summary charts after submission

### Option B: Shorter Version (5-7 minutes)

For time-constrained workshops, reduce to:
- 5 capabilities only (SAST, SCA, DevSecOps, Pentest, VulnMgmt)
- Top 2 priorities only
- Single blocker question only

### Option C: Pre-Workshop Version

Send assessment 1-2 days before workshop:
- Collect data in advance
- Prepare gap analysis slides
- Use workshop time for discussion, not data collection

---

## Sample Assessment Form (Print-Ready)

```
===============================================================================
APPLICATION SECURITY GAP ASSESSMENT
[Company Name] | [Date] | Confidential
===============================================================================

Your Role: [ ] CISO  [ ] CIO  [ ] Tech Lead  [ ] Other: _____

===============================================================================
SECTION 1: PROCESS MATURITY (Compliance-Linked)
===============================================================================

Rate your organization's PROCESS maturity. This links to RMIT compliance.

Maturity Levels:
  0 = Not Present (no formal process)
  1 = Ad-hoc (done inconsistently, no documentation)
  2 = Defined (documented process, assigned ownership)
  3 = Measured (metrics tracked, reviewed regularly)
  4 = Optimized (continuous improvement, benchmarked)

                                                    RMIT Ref    Your Rating
---------------------------------------------------------------------------
1. Secure SDLC Process                              Ch 10.2     0  1  2  3  4
   (Security integrated into dev lifecycle)

2. Security Requirements Process                    Ch 9.2      0  1  2  3  4
   (Security reqs defined, validated, tracked)

3. Security Testing Process                         Ch 10.2     0  1  2  3  4
   (Test planning, execution, remediation workflow)

4. Vulnerability Management Process                 Ch 11.3     0  1  2  3  4
   (Discovery→triage→remediation→verification)

5. Third-Party/Supply Chain Risk Process            App 8       0  1  2  3  4
   (Vendor assessment, dependency governance)

6. Security Training & Awareness Process            Ch 15       0  1  2  3  4
   (Training program, tracking, effectiveness)

7. Security Metrics & Reporting Process             Ch 8        0  1  2  3  4
   (KPIs defined, reported to management/board)

8. Incident Response Process (AppSec)               Ch 11.4     0  1  2  3  4
   (Detection, containment, remediation for app vulns)

                                          PROCESS MATURITY TOTAL: ___/32

===============================================================================
SECTION 2: TOOL COVERAGE (Capability Assessment)
===============================================================================

Rate your TOOL deployment and effectiveness. This links to technical capability.

Coverage Levels:
  0 = None (no tool in place)
  1 = Pilot (tool exists, limited scope <25% apps)
  2 = Partial (25-75% app coverage)
  3 = Comprehensive (>75% coverage, integrated in workflow)
  4 = Optimized (full coverage, automated, metrics-driven)

                                                    RMIT Ref    Your Rating
---------------------------------------------------------------------------
1. SAST (Static Analysis)                           App 3,4,5   0  1  2  3  4
   Tool(s) used: _______________________

2. DAST (Dynamic Testing)                           App 3,4,5   0  1  2  3  4
   Tool(s) used: _______________________

3. SCA (Dependency Scanning)                        App 4,5,8   0  1  2  3  4
   Tool(s) used: _______________________

4. SBOM (Software Inventory)                        App 5,8     0  1  2  3  4
   Tool(s) used: _______________________

5. Container/IaC Security                           App 10      0  1  2  3  4
   Tool(s) used: _______________________

6. API Security Testing                             App 5.E     0  1  2  3  4
   Tool(s) used: _______________________

7. Mobile App Security                              App 4       0  1  2  3  4
   Tool(s) used: _______________________

8. Secret Detection                                 Ch 11       0  1  2  3  4
   Tool(s) used: _______________________

                                          TOOL COVERAGE TOTAL: ___/32

===============================================================================
SECTION 3: MATURITY SUMMARY (Plot Your Position)
===============================================================================

Based on your totals, plot your organization:

                            TOOL COVERAGE
                    Low (0-10)  Med (11-21)  High (22-32)
                   ┌───────────┬───────────┬───────────┐
    High (22-32)   │  Process  │  Balanced │  OPTIMAL  │
                   │  Focused  │   Growth  │  (Target) │
PROCESS            ├───────────┼───────────┼───────────┤
MATURITY Med       │   Early   │  Typical  │   Tool    │
         (11-21)   │   Stage   │           │  Focused  │
                   ├───────────┼───────────┼───────────┤
    Low (0-10)     │  STARTING │  Tool-Led │  Tool-    │
                   │  (Risk)   │  (Risky)  │  Heavy    │
                   └───────────┴───────────┴───────────┘

Your Position: Process ___/32  |  Tools ___/32  |  Quadrant: ___________

===============================================================================
SECTION 4: PRIORITIES & BLOCKERS
===============================================================================

TOP 3 PROCESS priorities (from Section 1, write #):
   1st: ___    2nd: ___    3rd: ___

TOP 3 TOOL priorities (from Section 2, write #):
   1st: ___    2nd: ___    3rd: ___

Biggest PROCESS barrier (check ONE):
[ ] No ownership assigned    [ ] Lack of documentation    [ ] No management support
[ ] Siloed teams            [ ] Unclear requirements     [ ] Other: ____________

Biggest TOOL barrier (check ONE):
[ ] Budget                  [ ] Integration complexity   [ ] Lack of skills
[ ] Too many false positives [ ] Developer pushback      [ ] Other: ____________

===============================================================================
SECTION 5: SUCCESS DEFINITION
===============================================================================

In 12 months, what PROCESS improvement would you report to the Board?
__________________________________________________________________________

In 12 months, what TOOL metric would you report to the Board?
__________________________________________________________________________

===============================================================================
```

### Interpreting the Two-Dimensional Assessment

| Quadrant | Diagnosis | Recommendation |
|----------|-----------|----------------|
| **Low Process + Low Tools** | Starting point, high risk | Focus on process first (cheaper, foundational) |
| **Low Process + High Tools** | Tool-heavy, ROI at risk | Tools won't help without process. Invest in process. |
| **High Process + Low Tools** | Process-focused, manual effort | Ready for tools. Will get good ROI from automation. |
| **High Process + High Tools** | Optimal state | Maintain, optimize, benchmark with BSIMM15 |

### Why Two Dimensions?

| Dimension | What It Measures | Compliance Link |
|-----------|------------------|-----------------|
| **Process Maturity** | How you work | RMIT requires defined, measured processes |
| **Tool Coverage** | What you use | Tools provide evidence and efficiency |

**Key Insight:** High tool coverage with low process maturity = wasted investment. Tools generate findings, but without process, findings don't get fixed.

```
Tools without process = Dashboard of ignored alerts
Process without tools = Manual effort, doesn't scale
Both together = Effective, measurable AppSec program
```

---

## Expected Outcomes

After completing this assessment and discussion:

| Outcome | How It's Achieved |
|---------|-------------------|
| Shared understanding of current state | Consensus ratings after discussion |
| Alignment on priorities | Visible priority ranking patterns |
| Identified perception gaps | Role-based rating differences |
| Concrete blockers | Aggregated barrier data |
| Success criteria | Board-reportable metrics defined |

---

## Connection to RMIT Compliance

The 8 capabilities assessed map directly to RMIT requirements:

| Capability | RMIT Sections |
|------------|---------------|
| SAST | Ch 10.2, App 3, App 4, App 5.E |
| DAST | Ch 10.2, App 3, App 4, App 5.D-E |
| SCA | Ch 9.2, App 4, App 5.E, App 8 |
| SBOM | Ch 9.2, App 5.E, App 8 |
| DevSecOps | Ch 10.2, All chapters |
| Pentest | Ch 11.3, App 3, App 5.D, App 7 |
| Training | Ch 15.1-15.2, App 4 |
| VulnMgmt | Ch 10.2, Ch 11.3, App 5.E |

This allows direct translation of gap assessment results into RMIT compliance roadmap.

---

## Next Steps After Workshop

1. **Document consensus ratings** - Create baseline scorecard
2. **Validate with evidence** - Spot-check claims ("We have SAST" - show me)
3. **Map to RMIT gaps** - Use coverage matrix to identify compliance risk
4. **Build roadmap** - Prioritize based on workshop alignment
5. **Define metrics** - Turn "success in 12 months" into KPIs

---

## Validation: How Do You Know It's Working?

### Signs the Assessment is Landing Well

| Signal | What It Means |
|--------|---------------|
| Leaders ask clarifying questions | They're engaged, taking it seriously |
| Honest "0" or "1" ratings appear | They trust the process, not gaming it |
| Discussion gets animated at gaps | They care about alignment |
| They reference their real challenges | Not giving textbook answers |
| They push back on definitions | Good - means they're thinking critically |

### Signs It's Failing (Pivot Immediately)

| Signal | What to Do |
|--------|------------|
| Everyone rates everything 2-3 | Stop. Ask: "If everything is established, why are we here?" |
| Quick, disengaged responses | Pause. Share a breach example relevant to them. |
| "This doesn't apply to us" | Listen. Ask what WOULD apply. Adapt on the fly. |
| Cross-talk and checking others' answers | They're not confident. Reassure: no wrong answers. |
| "We already did this assessment" | Acknowledge. Ask: "What changed? What was the outcome?" |

### The Ultimate Test

At the end, ask:

> "Was there anything surprising in what we discovered today?"

If YES - the assessment surfaced something valuable.
If NO - either they already knew everything (unlikely) or we didn't dig deep enough.

---

## Quick Reference: The 3 Things That Matter

If you remember nothing else:

1. **Anchor to BSIMM15 and RMIT** - This is industry standard and regulatory requirement, not our invention

2. **Celebrate gaps and disagreements** - "The CISO rated it 2, Dev Lead rated it 0 - this is exactly what we need to discuss"

3. **Their input drives the outcome** - Don't arrive with predetermined conclusions. Let their data shape the roadmap.

---

*Assessment designed for RMIT AppSec compliance workshops*
*Reference: appsec-coverage-matrix.md, executive-report-appsec-rmit.md*
