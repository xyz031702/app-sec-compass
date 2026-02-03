# AI Security Intelligence Agent - Project Plan

## Executive Summary

Build a LangGraph-based agent that monitors AI security trends by ingesting Google Alerts from Gmail, scraping linked articles with Crawl4AI, and generating structured intelligence reports focused on AppSec, supply chain security, and regional compliance.

---

## Phase 1: Project Setup & Foundation

### 1.1 Environment Configuration
- Initialize Python 3.11+ project structure
- Create `requirements.txt` with dependencies:
  - `langgraph`, `langchain`, `langchain-google-genai`
  - `google-api-python-client`, `google-auth-oauthlib`
  - `crawl4ai`, `aiohttp`
  - `pytest`, `pytest-asyncio`
- Set up `.env` template for API keys (Gmail OAuth, LLM API keys)

### 1.2 Directory Structure
```
/src
  /nodes       # Ingest, Scrape, Synthesize, Report nodes
  /tools       # Gmail auth, URL decoder, ArXiv fetcher
  state.py     # AgentState TypedDict
  graph.py     # LangGraph definition
/tests
/docs
/credentials   # OAuth tokens (gitignored)
```

---

## Phase 2: Core Tools Development

### 2.1 Gmail Integration (`/src/tools/gmail_client.py`)
- OAuth2 authentication flow
- List unread emails with query: `label:"AI Security News" is:unread`
- Parse Google Alert HTML to extract headline/URL pairs
- Mark processed emails as read

### 2.2 URL Decoder (`/src/tools/url_decoder.py`)
- Regex utility to strip Google redirect wrappers
- Extract clean target URLs from `https://google.com/url?url=...`

### 2.3 Scraper Wrapper (`/src/tools/scraper.py`)
- Async Crawl4AI wrapper
- HTML to Markdown conversion
- Handle errors: timeouts, 403, consent popups
- Rate limiting (1-2s delay between domains)

---

## Phase 3: LangGraph Nodes

### 3.1 State Definition (`/src/state.py`)
```python
class AgentState(TypedDict):
    emails: list[EmailData]
    articles: list[ArticleData]
    themes: dict[str, list[ArticleData]]
    report: str
    errors: list[str]
```

### 3.2 Node Implementations

| Node | File | Responsibility |
|------|------|----------------|
| Ingest | `/src/nodes/ingest.py` | Fetch Gmail, extract URLs, decode redirects |
| Scrape | `/src/nodes/scrape.py` | Parallel async scraping with Crawl4AI |
| Synthesize | `/src/nodes/synthesize.py` | LLM grouping by theme (Regulation, Vulnerabilities, Region) |
| Report | `/src/nodes/report.py` | Format final Markdown summary |

### 3.3 Graph Assembly (`/src/graph.py`)
- Linear pipeline: `Ingest -> Scrape -> Synthesize -> Report`
- Checkpointer integration for resumable execution
- Conditional edges for error handling

---

## Phase 4: LLM Integration

### 4.1 Synthesize Logic
- Chunk long articles before LLM processing
- Theme classification prompt:
  - Regulation (EU AI Act, MAS/CSA)
  - Vulnerabilities (CVE, prompt injection, model attacks)
  - Regional (Singapore/ASEAN focus)
- Extract security takeaways

### 4.2 Report Generation
- Professional Markdown output (no emojis)
- Sections: Executive Summary, Themes, Actionable Takeaways
- Focus areas: AppSec, DevSecOps, SME guidance

---

## Phase 5: Testing & Validation

### 5.1 Unit Tests
- `/tests/test_url_decoder.py`: Redirect stripping
- `/tests/test_gmail_client.py`: Email parsing (mocked)
- `/tests/test_scraper.py`: Error handling scenarios

### 5.2 Integration Tests
- End-to-end graph execution with sample data
- Checkpointer resume testing

---

## Phase 6: Future Enhancements (Optional)

| Feature | Description |
|---------|-------------|
| ArXiv RSS | Add ArXiv feed ingestion for academic papers |
| GitHub Topics | Monitor security tool repos |
| Scheduling | Cron/Airflow for daily runs |
| Persistence | Database for historical tracking |

---

## Implementation Order (Priority)

1. **Project setup** - Directory structure, requirements.txt
2. **URL decoder tool** - Simplest, testable independently
3. **Gmail client** - OAuth flow, email parsing
4. **Scraper wrapper** - Crawl4AI async integration
5. **State definition** - AgentState TypedDict
6. **Ingest node** - Connect Gmail + URL decoder
7. **Scrape node** - Parallel article fetching
8. **Synthesize node** - LLM theme grouping
9. **Report node** - Markdown output
10. **Graph assembly** - Wire all nodes together

---

## Key Technical Decisions

| Decision | Rationale |
|----------|-----------|
| Markdown over raw HTML | Reduces LLM token usage significantly |
| Asyncio-first | Required for efficient parallel scraping |
| Checkpointers | Resume interrupted long-running jobs |
| Rate limiting | Avoid IP bans from aggressive scraping |
| Theme-based grouping | Makes reports actionable and scannable |
