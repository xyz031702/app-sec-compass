# Local Website Build Plan

## Objective

Build a single-page or multi-page local website that consolidates all RMIT-AppSec mapping content for easy navigation and reference. Professional Black Duck branding throughout.

---

## Existing Content Inventory

### Source Files Available

| Category | Files | Location | Status |
|----------|-------|----------|--------|
| **Original RMIT** | `pd-rmit-nov25.pdf`, `pd-rmit-nov25.txt` | `../` | Ready (link) |
| **RMIT Mappings** | 20x `rmit-*-appsec-map.md` | `./` | Ready |
| **Coverage Matrix** | `appsec-coverage-matrix.md` | `./` | Ready |
| **Review Guidelines** | `review.md` | `./` | Ready |
| **Summary Plan** | `summary.md` | `./` | Ready |
| **Executive Report** | `executive-report-appsec-rmit.html` | `./executive_report/` | Ready |
| **Assessment Forms** | 3x `.html` forms | `./assessment_forms/` | Ready |
| **Logo** | `logo.png` | `./assessment_forms/` | Ready |

---

## Website Structure

```
local_website/
├── index.html                    # Main dashboard/landing page
├── css/
│   ├── styles.css                # Core styles (Black Duck branding)
│   └── document.css              # Professional document styles for MD
├── js/
│   ├── main.js                   # Navigation, search, interactions
│   └── markdown-render.js        # MD to HTML converter (if needed)
├── assets/
│   ├── logo.png                  # Black Duck logo
│   ├── favicon.ico               # Browser favicon
│   └── icons/                    # SVG icons for UI
├── pages/
│   ├── mappings.html             # All RMIT-AppSec mappings browser
│   ├── coverage.html             # Coverage matrix with filters
│   ├── guidelines.html           # Review guidelines (from review.md)
│   ├── executive.html            # Executive report viewer
│   └── assessment.html           # Assessment forms hub
├── docs/
│   ├── rmit-source/
│   │   ├── pd-rmit-nov25.pdf     # Original RMIT PDF (copy)
│   │   └── pd-rmit-nov25.txt     # Original RMIT text (copy)
│   ├── mappings/                 # Converted mapping HTML files
│   │   ├── rmit-ch08-governance.html
│   │   ├── rmit-ch09-technology-risk-management.html
│   │   ├── ... (all 20 mapping docs)
│   │   └── index.json            # Mapping index for navigation
│   ├── reports/
│   │   └── executive-report.html # Board report (copy)
│   └── forms/
│       ├── assessment-full.html
│       ├── assessment-process.html
│       └── assessment-tools.html
└── data/
    ├── mappings.json             # Parsed mapping data for search
    ├── coverage-matrix.json      # Coverage data for matrix
    └── chapters.json             # RMIT chapter index
```

---

## Page Designs

### 1. Landing Page (`index.html`)

**Sections:**
- Header with Black Duck logo + title + RMIT PDF download button
- Quick stats cards (35% coverage, 20 chapters, 8 tool categories)
- Navigation cards to main sections
- Source document links

**Layout:**
```
┌─────────────────────────────────────────────────────────────┐
│  [BLACK DUCK LOGO]  RMIT AppSec Compliance Hub   [PDF ⬇]    │
│                                                             │
│  BNM Risk Management in Technology - November 2025          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐       │
│  │   35%    │ │    20    │ │    8     │ │   100+   │       │
│  │ AppSec   │ │ Chapters │ │  Tools   │ │ Controls │       │
│  │ Coverage │ │ Mapped   │ │ Assessed │ │ Analyzed │       │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘       │
│                                                             │
│  ┌─────────────────┐  ┌─────────────────┐                  │
│  │ 📋 MAPPINGS     │  │ 📊 COVERAGE     │                  │
│  │ Browse all RMIT │  │ Matrix & gap    │                  │
│  │ chapter maps    │  │ analysis        │                  │
│  └─────────────────┘  └─────────────────┘                  │
│                                                             │
│  ┌─────────────────┐  ┌─────────────────┐                  │
│  │ 📄 EXECUTIVE    │  │ 📝 ASSESSMENT   │                  │
│  │ Board report    │  │ Workshop forms  │                  │
│  └─────────────────┘  └─────────────────┘                  │
│                                                             │
│  ┌─────────────────┐  ┌─────────────────┐                  │
│  │ 📖 GUIDELINES   │  │ 📥 SOURCE DOCS  │                  │
│  │ AppSec scope &  │  │ • RMIT PDF      │                  │
│  │ ROI criteria    │  │ • RMIT Text     │                  │
│  └─────────────────┘  └─────────────────┘                  │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│  [LOGO]  Framework: BSIMM15 | BNM RMIT Nov 2025            │
└─────────────────────────────────────────────────────────────┘
```

### 2. Mappings Page (`pages/mappings.html`)

**Features:**
- Sidebar with chapter/appendix list
- Main content area showing selected mapping
- Search box to find controls
- Filter by AppSec tool category

**Layout:**
```
┌────────────────┬────────────────────────────────────────────┐
│ CHAPTERS       │  RMIT Chapter 10 - Technology Operations   │
│                │                                            │
│ ▼ Part A       │  Control 10.1                              │
│   Overview     │  ┌──────────────────────────────────────┐  │
│                │  │ Requirement: ...                     │  │
│ ▼ Chapters     │  │ AppSec Mapping:                      │  │
│   Ch 8         │  │ • SAST: SonarQube...                 │  │
│   Ch 9         │  │ • DAST: OWASP ZAP...                 │  │
│ ► Ch 10        │  └──────────────────────────────────────┘  │
│   Ch 11        │                                            │
│   Ch 12        │  Control 10.2                              │
│   ...          │  ┌──────────────────────────────────────┐  │
│                │  │ ...                                  │  │
│ ▼ Appendices   │  └──────────────────────────────────────┘  │
│   App 1        │                                            │
│   App 2        │                                            │
│   ...          │                                            │
└────────────────┴────────────────────────────────────────────┘
```

### 3. Coverage Page (`pages/coverage.html`)

**Features:**
- Interactive matrix table
- Click to filter by tool/chapter
- Color-coded cells (AppSec applicable vs not)
- Summary stats at top

**Layout:**
```
┌─────────────────────────────────────────────────────────────┐
│  COVERAGE MATRIX                    [Filter: All Tools ▼]   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Summary: 35% AppSec | 65% Other Layers                     │
│  ████████████░░░░░░░░░░░░░░░░░░░░                          │
│                                                             │
│  ┌────────┬────┬────┬────┬────┬────┬────┬────┬────┐        │
│  │ RMIT   │SAST│DAST│SCA │SBOM│API │Mob │Pen │... │        │
│  ├────────┼────┼────┼────┼────┼────┼────┼────┼────┤        │
│  │ Ch 10  │ ●  │ ●  │ ●  │ ●  │ —  │ —  │ ●  │    │        │
│  │ Ch 11  │ ●  │ ●  │ ●  │ —  │ —  │ —  │ ●  │    │        │
│  │ Ch 12  │ ●  │ ●  │ —  │ —  │ ●  │ ●  │ ●  │    │        │
│  │ App 3  │ ●  │ ●  │ —  │ —  │ ●  │ —  │ ●  │    │        │
│  │ App 4  │ ●  │ ●  │ ●  │ —  │ —  │ ●  │ ●  │    │        │
│  │ ...    │    │    │    │    │    │    │    │    │        │
│  └────────┴────┴────┴────┴────┴────┴────┴────┴────┘        │
│                                                             │
│  ● = AppSec Applicable    — = Not AppSec                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 4. Executive Report Page (`pages/executive.html`)

**Options:**
- Embed existing HTML report in iframe
- Or convert to native page sections
- Include download PDF button

### 5. Assessment Page (`pages/assessment.html`)

**Features:**
- Cards for each assessment form
- Preview + download/print buttons
- Embed forms or link to HTML files

---

## Technical Approach

### Option A: Static HTML (Recommended)

**Pros:** No dependencies, works offline, fast
**Cons:** Manual updates needed

**Implementation:**
1. Convert MD files to HTML using simple script
2. Build navigation with vanilla JS
3. Use CSS for Black Duck styling
4. Single folder, open index.html in browser

### Option B: Simple Python Server

**Pros:** Can parse MD dynamically
**Cons:** Requires Python installed

```bash
# Run from local_website folder
python -m http.server 8080
# Open http://localhost:8080
```

### Option C: Node.js Static Site Generator

**Pros:** More features, templating
**Cons:** Requires Node.js, more complex

---

## Implementation Steps

### Phase 1: Setup (1 hour)
1. Create `local_website/` folder structure
2. Copy `logo.png` to assets
3. Create `styles.css` with Black Duck colors
4. Create basic `index.html` shell

### Phase 2: Content Conversion (2 hours)
1. Parse all `*-appsec-map.md` files to HTML
2. Parse `appsec-coverage-matrix.md` to interactive table
3. Parse `review.md` for reference sidebar
4. Copy existing HTML reports/forms

### Phase 3: Navigation (1 hour)
1. Build sidebar navigation JS
2. Add search functionality
3. Add filter by tool category
4. Add breadcrumbs

### Phase 4: Polish (1 hour)
1. Responsive design tweaks
2. Print styles
3. Test all links
4. Add favicon

---

## Branding & Design System

### Black Duck Logo

Use existing `logo.png` from `assessment_forms/` folder. Logo placement:
- Header: 40px height, left-aligned
- Footer: 20px height, with opacity 0.7
- Favicon: Generate 32x32 from logo

### Color Scheme

```css
:root {
    /* Primary Brand */
    --bd-black: #000000;
    --bd-purple: #9F81BD;
    --bd-purple-light: #E8E0F0;
    --bd-purple-dark: #7B5FA0;
    --bd-white: #FFFFFF;

    /* Neutral Scale */
    --bd-gray-50: #FAFAFA;
    --bd-gray-100: #F7F7F8;
    --bd-gray-200: #E5E5E7;
    --bd-gray-300: #D4D4D8;
    --bd-gray-500: #71717A;
    --bd-gray-600: #52525B;
    --bd-gray-700: #3F3F46;
    --bd-gray-800: #27272A;
    --bd-gray-900: #18181B;

    /* Semantic Colors */
    --bd-success: #10B981;
    --bd-warning: #F59E0B;
    --bd-danger: #DC2626;
    --bd-info: #3B82F6;
}
```

### Professional Document Styles for MD Content

```css
/* Document Container */
.document {
    max-width: 900px;
    margin: 0 auto;
    padding: 40px 50px;
    background: white;
    box-shadow: 0 2px 10px rgba(0,0,0,0.08);
    border-radius: 8px;
}

/* Document Header */
.document-header {
    border-bottom: 3px solid var(--bd-purple);
    padding-bottom: 20px;
    margin-bottom: 30px;
}

.document-title {
    font-size: 24pt;
    font-weight: 700;
    color: var(--bd-black);
    margin-bottom: 8px;
}

.document-meta {
    font-size: 10pt;
    color: var(--bd-gray-500);
}

/* Headings */
.document h1 {
    font-size: 20pt;
    font-weight: 700;
    color: var(--bd-black);
    margin: 30px 0 15px;
    padding-bottom: 10px;
    border-bottom: 2px solid var(--bd-purple);
}

.document h2 {
    font-size: 14pt;
    font-weight: 600;
    color: var(--bd-gray-800);
    margin: 25px 0 12px;
    padding-left: 12px;
    border-left: 4px solid var(--bd-purple);
}

.document h3 {
    font-size: 12pt;
    font-weight: 600;
    color: var(--bd-gray-700);
    margin: 20px 0 10px;
}

/* Paragraphs */
.document p {
    font-size: 11pt;
    line-height: 1.7;
    color: var(--bd-gray-700);
    margin-bottom: 12px;
    text-align: justify;
}

/* Tables */
.document table {
    width: 100%;
    border-collapse: collapse;
    margin: 20px 0;
    font-size: 10pt;
}

.document thead th {
    background: var(--bd-black);
    color: white;
    padding: 12px 10px;
    text-align: left;
    font-weight: 600;
}

.document tbody td {
    padding: 10px;
    border-bottom: 1px solid var(--bd-gray-200);
}

.document tbody tr:nth-child(even) {
    background: var(--bd-gray-50);
}

.document tbody tr:hover {
    background: var(--bd-purple-light);
}

/* Code/Control IDs */
.document code {
    background: var(--bd-gray-100);
    padding: 2px 6px;
    border-radius: 4px;
    font-family: 'Consolas', 'Monaco', monospace;
    font-size: 9pt;
    color: var(--bd-purple-dark);
}

/* Callout Boxes */
.document .callout {
    padding: 15px 20px;
    margin: 20px 0;
    border-radius: 6px;
    border-left: 4px solid;
}

.document .callout.note {
    background: var(--bd-purple-light);
    border-color: var(--bd-purple);
}

.document .callout.warning {
    background: #FEF3C7;
    border-color: var(--bd-warning);
}

.document .callout.important {
    background: #FEE2E2;
    border-color: var(--bd-danger);
}

/* Lists */
.document ul, .document ol {
    margin: 15px 0 15px 25px;
}

.document li {
    margin-bottom: 8px;
    line-height: 1.6;
}

/* RMIT Reference Badge */
.rmit-ref {
    display: inline-block;
    background: var(--bd-purple-light);
    color: var(--bd-purple-dark);
    padding: 2px 8px;
    border-radius: 4px;
    font-size: 9pt;
    font-weight: 500;
}

/* Tool Category Badge */
.tool-badge {
    display: inline-block;
    padding: 3px 10px;
    border-radius: 12px;
    font-size: 8pt;
    font-weight: 600;
    margin-right: 4px;
}

.tool-badge.sast { background: #DBEAFE; color: #1D4ED8; }
.tool-badge.dast { background: #D1FAE5; color: #059669; }
.tool-badge.sca { background: #FEF3C7; color: #B45309; }
.tool-badge.sbom { background: #E8E0F0; color: #7B5FA0; }
.tool-badge.api { background: #FCE7F3; color: #BE185D; }
.tool-badge.mobile { background: #CFFAFE; color: #0891B2; }
```

---

## Original RMIT Document Links

### Source Documents

| Document | Path | Usage |
|----------|------|-------|
| **PDF** | `../pd-rmit-nov25.pdf` | Primary reference, download link |
| **Text** | `../pd-rmit-nov25.txt` | Searchable text, quick lookup |

### Integration in Website

1. **Header Link**: "View Original RMIT Document" button linking to PDF
2. **Per-Control Links**: Each mapping control links to relevant section in TXT
3. **Reference Sidebar**: Quick links to RMIT chapters in PDF

### HTML Implementation

```html
<!-- Header Download Button -->
<a href="../pd-rmit-nov25.pdf" class="btn-download" target="_blank">
    <svg><!-- PDF icon --></svg>
    Download RMIT PDF
</a>

<!-- Control Reference Link -->
<div class="control-header">
    <h3>Control 10.2</h3>
    <a href="../pd-rmit-nov25.txt#control-10-2" class="rmit-ref">
        View in RMIT Source
    </a>
</div>
```

---

## File Generation Script

Create a simple script to convert MD to HTML:

```python
# scripts/build.py
import markdown
import os
from pathlib import Path

def convert_md_to_html(md_file, output_dir):
    with open(md_file, 'r') as f:
        content = f.read()
    html = markdown.markdown(content, extensions=['tables', 'fenced_code'])
    # Wrap in template
    # Save to output_dir
```

---

## Deliverables

| Deliverable | Description |
|-------------|-------------|
| `local_website/index.html` | Main dashboard |
| `local_website/pages/*.html` | Section pages |
| `local_website/css/styles.css` | Branding styles |
| `local_website/js/main.js` | Navigation/search |
| `local_website/data/mappings.json` | Parsed mapping data |

---

## Success Criteria

- [ ] Opens in browser without server (file://)
- [ ] All 20 RMIT mappings accessible
- [ ] Coverage matrix interactive
- [ ] Executive report viewable
- [ ] Assessment forms printable
- [ ] Search finds controls
- [ ] Consistent Black Duck branding
- [ ] Works offline

---

## Next Steps

1. Approve this plan
2. Create folder structure
3. Build index.html with navigation
4. Convert MD content to HTML
5. Add interactivity (search, filters)
6. Test and polish
