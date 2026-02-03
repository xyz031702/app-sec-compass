"""
Tests for URL decoder utility
"""
import pytest
from src.tools.url_decoder import decode_google_redirect_url, extract_urls_from_html


class TestDecodeGoogleRedirectUrl:
    """Tests for decode_google_redirect_url function"""

    def test_google_redirect_with_url_param(self):
        """Should extract URL from google.com/url?url=... format"""
        redirect_url = (
            "https://www.google.com/url?"
            "url=https%3A%2F%2Fexample.com%2Farticle%2Fai-security&"
            "ct=ga&cd=CAEYASoTODY3NjQwNjQzMjEwMTIzNDU2MjI"
        )
        result = decode_google_redirect_url(redirect_url)
        assert result == "https://example.com/article/ai-security"

    def test_google_redirect_with_q_param(self):
        """Should extract URL from google.com/url?q=... format"""
        redirect_url = (
            "https://www.google.com/url?"
            "q=https%3A%2F%2Fnews.example.org%2Fstory&"
            "sa=D&source=editors"
        )
        result = decode_google_redirect_url(redirect_url)
        assert result == "https://news.example.org/story"

    def test_non_google_url_unchanged(self):
        """Should return non-Google URLs unchanged"""
        url = "https://example.com/direct-article"
        result = decode_google_redirect_url(url)
        assert result == url

    def test_empty_url_returns_empty(self):
        """Should handle empty string input"""
        result = decode_google_redirect_url("")
        assert result == ""

    def test_none_url_returns_none(self):
        """Should handle None input"""
        result = decode_google_redirect_url(None)
        assert result is None


class TestExtractUrlsFromHtml:
    """Tests for extract_urls_from_html function"""

    def test_extracts_google_redirect_links(self):
        """Should extract and decode Google redirect links from HTML"""
        html = """
        <html>
        <body>
            <a href="https://www.google.com/url?url=https%3A%2F%2Fexample.com%2Farticle1">Article 1</a>
            <a href="https://www.google.com/url?url=https%3A%2F%2Fexample.com%2Farticle2">Article 2</a>
        </body>
        </html>
        """
        urls = extract_urls_from_html(html)
        assert len(urls) == 2
        assert "https://example.com/article1" in urls
        assert "https://example.com/article2" in urls

    def test_filters_google_system_links(self):
        """Should filter out Google system links (unsubscribe, etc.)"""
        html = """
        <html>
        <body>
            <a href="https://www.google.com/url?url=https%3A%2F%2Fexample.com%2Farticle">Article</a>
            <a href="https://support.google.com/alerts">Support</a>
            <a href="https://www.google.com/alerts/manage">Manage Alerts</a>
        </body>
        </html>
        """
        urls = extract_urls_from_html(html)
        assert len(urls) == 1
        assert "https://example.com/article" in urls

    def test_deduplicates_urls(self):
        """Should not include duplicate URLs"""
        html = """
        <html>
        <body>
            <a href="https://www.google.com/url?url=https%3A%2F%2Fexample.com%2Farticle">Link 1</a>
            <a href="https://www.google.com/url?url=https%3A%2F%2Fexample.com%2Farticle">Link 2</a>
        </body>
        </html>
        """
        urls = extract_urls_from_html(html)
        assert len(urls) == 1

    def test_empty_html_returns_empty_list(self):
        """Should return empty list for empty HTML"""
        urls = extract_urls_from_html("")
        assert urls == []

    def test_none_html_returns_empty_list(self):
        """Should return empty list for None input"""
        urls = extract_urls_from_html(None)
        assert urls == []
