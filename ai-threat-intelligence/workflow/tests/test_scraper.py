"""
Tests for article scraper
"""
import pytest
from src.tools.scraper import ArticleScraper


class TestArticleScraper:
    """Tests for ArticleScraper class"""

    def test_scraper_initialization(self):
        """Should initialize with default delay"""
        scraper = ArticleScraper()
        assert scraper.delay == 1.5

    def test_scraper_custom_delay(self):
        """Should accept custom delay"""
        scraper = ArticleScraper(delay_between_domains=2.5)
        assert scraper.delay == 2.5


@pytest.mark.asyncio
async def test_scrape_invalid_url():
    """Should handle invalid URL gracefully"""
    scraper = ArticleScraper(delay_between_domains=0)
    result = await scraper.scrape_url("https://this-domain-does-not-exist-12345.com")

    assert result['url'] == "https://this-domain-does-not-exist-12345.com"
    assert result['error'] is not None


@pytest.mark.asyncio
async def test_scrape_urls_empty_list():
    """Should handle empty URL list"""
    scraper = ArticleScraper(delay_between_domains=0)
    results = await scraper.scrape_urls([])

    assert results == []
