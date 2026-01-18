# AI Threat Intelligence MVP v0.3

Ultra-simple AI threat intelligence generator using Gemini deep thinking mode.

## Quick Start

1. **Setup Environment**
   ```bash
   cd ai-threat-intelligence/mvp
   pip install -r requirements.txt
   cp .env.template .env
   ```

2. **Configure API Key**
   Edit `.env` and add your Gemini API key:
   ```
   GEMINI_API_KEY=your_actual_api_key_here
   ```

3. **Generate Report**
   ```bash
   python threat_intel.py
   ```

4. **View Report**
   ```bash
   python threat_intel.py --show
   ```

## Features

- **Single API Call**: Complete report generation with one Gemini request
- **Deep Thinking**: Advanced reasoning for comprehensive analysis
- **Auto-formatting**: Professional executive summary output
- **Time-bounded**: Focuses on last 14 days of AI security developments
- **Source Priority**: Emphasizes HackerNews and major security outlets

## Output

Reports are saved to `reports/` directory with timestamp:
- Format: `ai_threat_intel_YYYYMMDD_HHMMSS.md`
- Structure: 5-section executive summary
- Metadata: Analysis period, generation method, next report date

## System Requirements

- Python 3.8+
- Gemini API key
- Internet connection

## Cost

Approximately $0.10-0.50 per report depending on output length.

## Architecture

```
Input: Threat Intelligence Analyst Prompt
  ↓
Gemini API (Deep Thinking Mode)
  ↓
Output: Complete Executive Summary
```

Simple, reliable, effective.
