# AI Security Intelligence Agent - Project Rules

## Project Overview
A systematic LangGraph-based agent that monitors AI security trends, regulations, and vulnerabilities by ingesting Google Alerts, RSS feeds (ArXiv), and GitHub topics.

## Tech Stack
- Framework: LangGraph (StateGraph)
- Language: Python 3.11+ (Asyncio-first)
- Ingestion: Gmail API, ArXiv API, RSS
- Scraping: Crawl4AI (convert to Markdown)
- LLM Integration: LangChain with Gemini/Claude
- Documentation: English

## Formatting & Style Standards
- Markdown: Professional, simple, non-stylized. No emojis or decorative symbols.
- Coding Style: PEP 8 compliant, strict type hinting (Python Type Hints).
- Comments: All docstrings and comments must be in English.
- Error Handling: Async try-except blocks with detailed logging for scraping failures.

## Directory Structure
```
/src
  /nodes/         # Node logic (ingest, scrape, synthesize, report)
  /tools/         # Utilities (Gmail auth, URL decoder, scraper)
  state.py        # Unified TypedDict for AgentState
  graph.py        # LangGraph definition and compilation
  main.py         # CLI entry point
/tests/           # Pytest suites
/docs/            # Requirements and design specifications
/credentials/     # OAuth tokens (gitignored)
```

## Implementation Guidelines
- State Management: Do not pass large raw HTML blobs between nodes; convert to Markdown first to save tokens.
- URL Decoding: Always strip Google Alert redirects using the url_decoder utility before scraping.
- Concurrency: Use asyncio for scraping multiple links with rate limiting.
- Intelligence Focus: Prioritize Application Security (AppSec), Software Supply Chain (SBOM), and regional compliance (MAS/CSA/EU AI Act).

## Common Commands
```bash
# Install dependencies
pip install -r requirements.txt

# Run tests
pytest

# Run agent (outputs report to stdout)
python -m src.main

# Run agent with options
python -m src.main --output reports/report.md --max-emails 20 --mark-read

# Run with specific LLM provider
python -m src.main --provider anthropic --model claude-3-5-sonnet-20241022
```

## Environment Variables
Required in `.env` file:
- `GOOGLE_API_KEY`: Google Gemini API key
- `ANTHROPIC_API_KEY`: Anthropic Claude API key (optional)
- `GMAIL_CREDENTIALS_PATH`: Path to Gmail OAuth credentials JSON
- `GMAIL_TOKEN_PATH`: Path to store Gmail OAuth token
- `GMAIL_SEARCH_QUERY`: Default Gmail search query
- `LLM_PROVIDER`: Default LLM provider (gemini or anthropic)

## Gmail Setup
1. Create a project in Google Cloud Console
2. Enable Gmail API
3. Create OAuth 2.0 credentials (Desktop app type)
4. Download credentials.json to `credentials/credentials.json`
5. Run the agent once to complete OAuth flow

## Theme Categories
The agent classifies articles into these themes:
- REGULATION: AI governance, laws, compliance (EU AI Act, Singapore MAS/CSA)
- VULNERABILITIES: Security flaws, CVEs, prompt injection, model attacks
- REGIONAL: Singapore/ASEAN-specific AI developments
- RESEARCH: Academic papers, new techniques, tools
- INDUSTRY: Vendor announcements, product security, market trends
