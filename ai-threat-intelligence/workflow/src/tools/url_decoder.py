"""
URL Decoder Tool
Handles Google Alert redirect links to extract actual target URLs
"""
import re
from urllib.parse import unquote, urlparse, parse_qs
from bs4 import BeautifulSoup


def decode_google_redirect_url(url: str) -> str:
    """
    Decode Google redirect URL to extract actual target link

    Args:
        url: Google redirect URL, format like https://www.google.com/url?url=...

    Returns:
        Decoded actual target URL
    """
    if not url:
        return url

    # Check if it's a Google redirect URL
    parsed = urlparse(url)
    if 'google.com' not in parsed.netloc:
        return url

    # Extract target URL from query parameters
    query_params = parse_qs(parsed.query)

    # Google Alert uses 'url' parameter
    if 'url' in query_params:
        target_url = query_params['url'][0]
        return unquote(target_url)

    # Fallback: use 'q' parameter (some Google link formats)
    if 'q' in query_params:
        target_url = query_params['q'][0]
        return unquote(target_url)

    return url


def extract_urls_from_html(html_content: str) -> list[str]:
    """
    Extract all article links from Google Alert email HTML

    Args:
        html_content: Email HTML content

    Returns:
        List of decoded URLs
    """
    if not html_content:
        return []

    soup = BeautifulSoup(html_content, 'html.parser')
    urls = []

    # Find all links
    for link in soup.find_all('a', href=True):
        href = link['href']

        # Filter out Google system links (unsubscribe, etc.)
        if _is_article_link(href):
            decoded_url = decode_google_redirect_url(href)
            if decoded_url and decoded_url not in urls:
                urls.append(decoded_url)

    return urls


def _is_article_link(url: str) -> bool:
    """
    Determine if URL is an article link (exclude Google system links)

    Args:
        url: URL to check

    Returns:
        True if it's an article link
    """
    # Excluded URL patterns
    exclude_patterns = [
        r'support\.google\.com',
        r'accounts\.google\.com',
        r'notifications\.google\.com',
        r'unsubscribe',
        r'manage.*alerts',
        r'feedback',
    ]

    for pattern in exclude_patterns:
        if re.search(pattern, url, re.IGNORECASE):
            return False

    # Must contain google.com/url (redirect format) or be a direct link
    if 'google.com/url' in url:
        return True

    # Direct http/https links
    if url.startswith('http://') or url.startswith('https://'):
        return True

    return False
