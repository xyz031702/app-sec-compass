"""
Synthesize Node
Groups articles by theme and extracts security insights using LLM
"""
import os
from typing import Any

from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

from ..state import AgentState, ArticleData, ThemeGroup


# Theme classification and synthesis prompt
SYNTHESIS_PROMPT = """You are an AI security intelligence analyst. Analyze the following articles and:

1. Classify each article into one of these themes:
   - REGULATION: AI governance, laws, compliance (EU AI Act, Singapore MAS/CSA guidelines)
   - VULNERABILITIES: Security flaws, CVEs, prompt injection, model attacks, data poisoning
   - REGIONAL: Singapore/ASEAN-specific AI developments
   - RESEARCH: Academic papers, new techniques, tools
   - INDUSTRY: Vendor announcements, product security, market trends

2. For each theme group, provide:
   - A 2-3 sentence summary
   - 2-3 actionable security takeaways for AppSec/DevSecOps teams

Articles to analyze:
{articles}

Respond in the following JSON format:
{{
  "themes": [
    {{
      "theme_name": "REGULATION",
      "summary": "Brief summary of regulation-related articles...",
      "article_urls": ["url1", "url2"],
      "security_takeaways": [
        "Takeaway 1 for security teams",
        "Takeaway 2 for security teams"
      ]
    }}
  ]
}}

Only include themes that have matching articles. Focus on practical implications for security practitioners.
"""


def synthesize_node(state: AgentState) -> dict[str, Any]:
    """
    Synthesize node: Group articles by theme and extract insights

    Args:
        state: Current agent state with articles

    Returns:
        Updated state with theme groups
    """
    articles: list[ArticleData] = state.get('articles', [])
    errors = state.get('errors', [])
    config = state.get('config', {})

    themes: list[ThemeGroup] = []

    # Filter out failed scrapes
    valid_articles = [a for a in articles if not a.scrape_error and a.content_markdown]

    if not valid_articles:
        errors.append("No valid articles to synthesize")
        return {'themes': themes, 'errors': errors}

    # Prepare article summaries for LLM (truncate long content)
    max_chars = config.get('max_article_chars', 2000)
    article_summaries = []

    for article in valid_articles:
        content = article.content_markdown[:max_chars]
        if len(article.content_markdown) > max_chars:
            content += "... [truncated]"

        article_summaries.append(
            f"URL: {article.url}\n"
            f"Title: {article.title}\n"
            f"Content: {content}\n"
            f"---"
        )

    articles_text = "\n\n".join(article_summaries)

    try:
        # Initialize LLM
        llm_provider = config.get('llm_provider', os.getenv('LLM_PROVIDER', 'gemini'))

        if llm_provider == 'gemini':
            llm = ChatGoogleGenerativeAI(
                model=config.get('llm_model', 'gemini-2.0-flash'),
                google_api_key=os.getenv('GOOGLE_API_KEY')
            )
        else:
            # Fallback to Anthropic
            from langchain_anthropic import ChatAnthropic
            llm = ChatAnthropic(
                model=config.get('llm_model', 'claude-3-5-sonnet-20241022'),
                api_key=os.getenv('ANTHROPIC_API_KEY')
            )

        # Create and run prompt
        prompt = ChatPromptTemplate.from_template(SYNTHESIS_PROMPT)
        chain = prompt | llm

        response = chain.invoke({"articles": articles_text})

        # Parse response
        import json
        response_text = response.content

        # Extract JSON from response
        json_start = response_text.find('{')
        json_end = response_text.rfind('}') + 1
        if json_start >= 0 and json_end > json_start:
            result = json.loads(response_text[json_start:json_end])

            # Build ThemeGroup objects
            url_to_article = {a.url: a for a in valid_articles}

            for theme_data in result.get('themes', []):
                theme_articles = [
                    url_to_article[url]
                    for url in theme_data.get('article_urls', [])
                    if url in url_to_article
                ]

                if theme_articles:
                    theme = ThemeGroup(
                        theme_name=theme_data.get('theme_name', 'UNKNOWN'),
                        summary=theme_data.get('summary', ''),
                        articles=theme_articles,
                        security_takeaways=theme_data.get('security_takeaways', [])
                    )
                    themes.append(theme)

    except Exception as e:
        errors.append(f"Synthesis error: {e}")

    return {
        'themes': themes,
        'errors': errors
    }
