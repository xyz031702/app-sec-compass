"""
Scrape Node
Fetches full article content from extracted URLs
"""
import asyncio
from typing import Any

from ..state import AgentState, ArticleData, EmailData
from ..tools.scraper import scrape_articles


def scrape_node(state: AgentState) -> dict[str, Any]:
    """
    Scrape node: Fetch article content from URLs

    Args:
        state: Current agent state with emails

    Returns:
        Updated state with articles list
    """
    emails: list[EmailData] = state.get('emails', [])
    errors = state.get('errors', [])
    config = state.get('config', {})

    articles: list[ArticleData] = []

    # Collect all URLs with their source email IDs
    url_to_email: dict[str, str] = {}
    for email in emails:
        for url in email.urls:
            if url not in url_to_email:
                url_to_email[url] = email.message_id

    urls = list(url_to_email.keys())

    if not urls:
        errors.append("No URLs found to scrape")
        return {'articles': articles, 'errors': errors}

    # Run async scraping
    delay = config.get('scrape_delay', 1.5)

    try:
        # Run async scraper in sync context
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            results = loop.run_until_complete(scrape_articles(urls, delay))
        finally:
            loop.close()

        # Convert results to ArticleData
        for result in results:
            url = result['url']
            article = ArticleData(
                url=url,
                title=result.get('title', ''),
                content_markdown=result.get('content', ''),
                source_email_id=url_to_email.get(url, ''),
                scrape_error=result.get('error')
            )
            articles.append(article)

            if result.get('error'):
                errors.append(f"Scrape error for {url}: {result['error']}")

    except Exception as e:
        errors.append(f"Scraping failed: {e}")

    return {
        'articles': articles,
        'errors': errors
    }
