"""
Article Scraper
Async web scraper using Crawl4AI for fetching article content
"""
import asyncio
from typing import Optional
from urllib.parse import urlparse

from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig


class ArticleScraper:
    """
    Async article scraper with rate limiting and error handling
    """

    def __init__(self, delay_between_domains: float = 1.5):
        """
        Initialize scraper

        Args:
            delay_between_domains: Delay in seconds between scraping different domains
        """
        self.delay = delay_between_domains
        self._last_domain: Optional[str] = None

    async def scrape_url(self, url: str) -> dict:
        """
        Scrape a single URL and return markdown content

        Args:
            url: URL to scrape

        Returns:
            Dict with 'title', 'content', 'error' keys
        """
        result = {
            'url': url,
            'title': '',
            'content': '',
            'error': None
        }

        try:
            # Rate limiting between different domains
            current_domain = urlparse(url).netloc
            if self._last_domain and current_domain != self._last_domain:
                await asyncio.sleep(self.delay)
            self._last_domain = current_domain

            # Configure browser
            browser_config = BrowserConfig(
                headless=True,
                verbose=False
            )

            # Configure crawler
            crawler_config = CrawlerRunConfig(
                word_count_threshold=50,
                remove_overlay_elements=True,  # Handle cookie popups
            )

            async with AsyncWebCrawler(config=browser_config) as crawler:
                crawl_result = await crawler.arun(
                    url=url,
                    config=crawler_config
                )

                if crawl_result.success:
                    result['title'] = crawl_result.metadata.get('title', '')
                    result['content'] = crawl_result.markdown or ''
                else:
                    result['error'] = crawl_result.error_message or 'Unknown scraping error'

        except asyncio.TimeoutError:
            result['error'] = 'Timeout while scraping'
        except Exception as e:
            result['error'] = str(e)

        return result

    async def scrape_urls(self, urls: list[str]) -> list[dict]:
        """
        Scrape multiple URLs with rate limiting

        Args:
            urls: List of URLs to scrape

        Returns:
            List of scrape results
        """
        results = []

        for url in urls:
            result = await self.scrape_url(url)
            results.append(result)

        return results


async def scrape_articles(urls: list[str], delay: float = 1.5) -> list[dict]:
    """
    Convenience function to scrape multiple articles

    Args:
        urls: List of URLs to scrape
        delay: Delay between domains in seconds

    Returns:
        List of scrape results
    """
    scraper = ArticleScraper(delay_between_domains=delay)
    return await scraper.scrape_urls(urls)
