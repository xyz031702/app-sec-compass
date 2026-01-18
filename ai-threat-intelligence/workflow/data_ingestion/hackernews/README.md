# Hacker News AI Threat Intelligence Search

This script uses Google Custom Search API to find AI-related security threats and vulnerabilities on Hacker News from the last 2 weeks.

## Features

- **Site-specific search**: Only searches Hacker News (news.ycombinator.com)
- **Date filtering**: Automatically searches content from the last 2 weeks
- **AI threat keywords**: Comprehensive list of AI security-related terms
- **Rate limiting**: Built-in delays to respect API limits
- **JSON export**: Saves results in structured format
- **Summary reporting**: Displays search statistics and top findings

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set up Environment Variables

The script reads API credentials from the `.env` file in the root directory of the project.

Add the following variables to `/home/scantist/github/app-sec-compass/.env`:

```bash
GOOGLE_SEARCH_API_KEY=your_api_key_here
GOOGLE_SEARCH_ENGINE_ID=your_search_engine_id_here
```

#### Getting Google Custom Search API Credentials

You need two things:

#### A. Google Custom Search API Key
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing one
3. Enable the "Custom Search API"
4. Go to "Credentials" and create an API key
5. Copy the API key and add it to `.env` as `GOOGLE_SEARCH_API_KEY`

#### B. Custom Search Engine ID

The `GOOGLE_SEARCH_ENGINE_ID` is a unique identifier for a Custom Search Engine (CSE) that defines which websites to search and search configuration settings.

**Steps to get the Search Engine ID:**

1. **Create a Custom Search Engine**
   - Go to [Google Custom Search Engine](https://cse.google.com/)
   - Click **"Add"** or **"New search engine"**
   - In **"Sites to search"**, enter: `news.ycombinator.com`
   - Give your search engine a name (e.g., "Hacker News AI Threats")
   - Click **"Create"**

2. **Get the Search Engine ID**
   - After creation, you'll be taken to the control panel
   - Click on **"Setup"** in the left sidebar
   - Under **"Basics"** section, find **"Search engine ID"**
   - Copy this ID (format: `017576662512468239146:omuauf_lfve`)
   - Add it to `.env` as `GOOGLE_SEARCH_ENGINE_ID=your_search_engine_id_here`

3. **Optional Configuration**
   - Enable **"Search the entire web"** for broader results
   - Configure **SafeSearch** settings
   - Customize result appearance

The Search Engine ID connects your API calls to your specific search configuration, ensuring results come only from Hacker News with your defined settings.

## Troubleshooting

### Common API Key Issues

#### Wrong API Key Type Error
If you get an error like:
```
"API keys are not supported by this API. Expected OAuth2 access token"
```

This means you're using the wrong type of API key. Follow these steps:

1. **Create a Custom Search Specific API Key**
   - Go to [Google Cloud Console](https://console.cloud.google.com/) → **APIs & Services** → **Credentials**
   - Click **"+ Create Credentials"** → **"API key"**
   - After creation, click **"Restrict Key"**

2. **Configure API Restrictions**
   - Under **"API restrictions"**, select **"Restrict key"**
   - Choose **"Custom Search API"** from the dropdown list
   - Click **"Save"**

3. **Verify API Key Format**
   - Custom Search API keys typically start with `AIza...`
   - If your key starts with `AQ.` or other prefixes, it's likely for a different Google service

4. **Update Your .env File**
   ```bash
   GOOGLE_SEARCH_API_KEY=AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
   GOOGLE_SEARCH_ENGINE_ID=c58f74b07704e4179
   ```

#### Test Your Credentials
```bash
source .env && curl "https://www.googleapis.com/customsearch/v1?key=${GOOGLE_SEARCH_API_KEY}&cx=${GOOGLE_SEARCH_ENGINE_ID}&q=test"
```

### Alternative Authentication Methods

While this script uses API keys for simplicity, there are other authentication methods available:

- **Service Account Keys**: More secure for production environments
- **OAuth2**: For user-based authentication
- **Application Default Credentials**: For Google Cloud environments
- **Workload Identity**: For Kubernetes deployments

For production use cases, consider implementing service account authentication instead of API keys for better security practices.

## Usage

Run the script:

```bash
python googlesearch.py
```

The script will automatically load credentials from the `.env` file and start searching.

## Search Keywords

The script searches for these AI threat-related terms:
- AI vulnerability, AI security, AI attack, AI threat
- Machine learning vulnerability, ML security, AI model attack
- AI poisoning, adversarial AI, AI backdoor, AI jailbreak
- LLM vulnerability, LLM security, ChatGPT vulnerability
- AI model theft, AI privacy, AI bias attack, prompt injection

## Output

The script generates:
1. **Console output**: Real-time search progress and summary
2. **Directory with individual JSON files**: Each result saved as a separate file
3. **Index file**: Summary of all results and file listing

### Output Structure

The script creates a timestamped directory containing:
- Individual JSON files for each search result (e.g., `001_AI_vulnerability_12345.json`)
- An `index.json` file with summary information

#### Individual Result File Structure

```json
{
  "title": "Article title",
  "url": "https://news.ycombinator.com/item?id=12345",
  "description": "Article snippet",
  "hn_item_id": "12345",
  "found_date": "2026-01-11T11:03:00.000000",
  "search_keyword": "AI vulnerability"
}
```

#### Index File Structure

```json
{
  "total_results": 25,
  "search_date": "2026-01-11T11:30:00.000000",
  "files": ["001_AI_vulnerability_12345.json", "002_AI_security_67890.json"],
  "keywords_summary": {
    "AI vulnerability": 5,
    "AI security": 3
  }
}
```

## Rate Limiting

The script includes built-in rate limiting:
- 1 second delay between search requests
- 2 seconds delay between different keywords
- Maximum 10 results per keyword (configurable)

## Customization

You can modify the search behavior by editing:
- `threat_keywords`: Add/remove search terms
- `max_results_per_keyword`: Change result limit per keyword
- Date range in `get_date_range()`: Modify the 14-day window

## API Limits

Google Custom Search API has daily quotas:
- Free tier: 100 queries per day
- Paid tier: Up to 10,000 queries per day

Plan your searches accordingly based on the number of keywords and results needed.
