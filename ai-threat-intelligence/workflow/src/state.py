"""
Unified AgentState definition
Used for state passing between LangGraph nodes
"""
from typing import TypedDict, Optional
from pydantic import BaseModel


class EmailData(BaseModel):
    """Email data structure"""
    message_id: str
    subject: str
    sender: str
    date: str
    urls: list[str]  # Decoded article links


class ArticleData(BaseModel):
    """Article data structure"""
    url: str
    title: str
    content_markdown: str  # Markdown format to save tokens
    source_email_id: str
    scrape_error: Optional[str] = None


class ThemeGroup(BaseModel):
    """Theme grouping structure"""
    theme_name: str  # Regulation, Vulnerabilities, Regional
    summary: str
    articles: list[ArticleData]
    security_takeaways: list[str]


class AgentState(TypedDict):
    """
    LangGraph agent state
    Shared by all nodes
    """
    # Ingestion phase
    emails: list[EmailData]

    # Scraping phase
    articles: list[ArticleData]

    # Analysis phase
    themes: list[ThemeGroup]

    # Output phase
    report: str

    # Error tracking
    errors: list[str]

    # Configuration
    config: dict
