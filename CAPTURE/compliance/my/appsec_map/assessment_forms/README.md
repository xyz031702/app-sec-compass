# AppSec Assessment Forms (PDF-Ready)

## Branding

Forms use **Black Duck** color scheme:
- Primary: Black (#000000)
- Accent: Purple (#9F81BD)
- Backgrounds: Gray scale

Logo file: `logo.png` (must be in same folder as HTML files)

## Files

| File | Description | Pages |
|------|-------------|-------|
| `appsec-assessment-full.html` | Complete assessment (Process + Tools + Summary Quadrant) | 2 pages |
| `appsec-assessment-process.html` | Process Maturity only (Compliance-Linked) | 1 page |
| `appsec-assessment-tools.html` | Tool Coverage only (Capability Assessment) | 1 page |
| `colors.css` | Brand color definitions (reference) | - |
| `logo.png` | Company logo | - |

## How to Use

### Print to PDF
1. Open the HTML file in a browser (Chrome recommended)
2. Click the **"Print / Save PDF"** button (top-right)
3. In print dialog:
   - Destination: **Save as PDF**
   - Paper size: **A4**
   - Margins: **Default** or **Minimum**
   - Background graphics: **Enabled** (required for colors/branding)
4. Save

### Direct Print
1. Open in browser
2. Click **Print** button or Ctrl+P
3. Select printer, ensure A4 paper
4. Enable background graphics

## Assessment Structure

### Section 1: Process Maturity (Compliance-Linked)
- 8 process areas mapped to RMIT chapters
- Maturity levels: 0-4 (Not Present → Optimized)
- Links to BNM RMIT compliance requirements
- Total score: /32

### Section 2: Tool Coverage (Capability Assessment)
- 8 tool categories with space to write tool names
- Coverage levels: 0-4 (None → Optimized)
- Links to RMIT appendices
- Total score: /32

### Maturity Quadrant
```
                    TOOL COVERAGE
              Low       Med       High
         ┌─────────┬─────────┬─────────┐
  High   │ Process │ Balanced│ OPTIMAL │
PROCESS  │ Focused │ Growth  │ (Target)│
MATURITY ├─────────┼─────────┼─────────┤
  Med    │  Early  │ Typical │  Tool   │
         │  Stage  │         │ Focused │
         ├─────────┼─────────┼─────────┤
  Low    │STARTING │Tool-Led │ Tool-   │
         │ (Risk)  │ (Risky) │ Heavy   │
         └─────────┴─────────┴─────────┘
```

## Facilitation Tips

1. **Before workshop**: Research the company's applications, dev model, recent incidents
2. **Opening**: Explain this is about alignment, not judgment
3. **During**: Collect ratings, plot on whiteboard, discuss perception gaps
4. **After**: Document consensus, validate with evidence, create roadmap

## Key Insight

> Tools without process = Dashboard of ignored alerts
> Process without tools = Manual effort, doesn't scale
> Both together = Effective, measurable AppSec program

## Framework References

- **BSIMM15**: [blackduck.com/bsimm](https://www.blackduck.com/services/security-program/bsimm-maturity-model.html)
- **BNM RMIT**: Bank Negara Malaysia Risk Management in Technology
- **Supply Chain MAP**: Black Duck Software Supply Chain Maturity Assessment
