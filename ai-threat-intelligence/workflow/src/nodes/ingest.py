"""
Ingest Node
Fetches unread Google Alert emails and extracts article URLs
"""
import os
from typing import Any

from ..state import AgentState, EmailData
from ..tools.gmail_client import GmailClient


def ingest_node(state: AgentState) -> dict[str, Any]:
    """
    Ingest node: Fetch emails from Gmail and extract URLs

    Args:
        state: Current agent state

    Returns:
        Updated state with emails list
    """
    errors = state.get('errors', [])
    config = state.get('config', {})

    # Get configuration
    credentials_path = config.get(
        'credentials_path',
        os.getenv('GMAIL_CREDENTIALS_PATH', 'credentials/credentials.json')
    )
    token_path = config.get(
        'token_path',
        os.getenv('GMAIL_TOKEN_PATH', 'credentials/token.json')
    )
    search_query = config.get(
        'search_query',
        os.getenv('GMAIL_SEARCH_QUERY', 'label:"AI Security News" is:unread')
    )

    emails: list[EmailData] = []

    try:
        client = GmailClient(
            credentials_path=credentials_path,
            token_path=token_path
        )

        emails = client.fetch_unread_alerts(
            query=search_query,
            max_results=config.get('max_emails', 50)
        )

        # Optionally mark as read after fetching
        if config.get('mark_as_read', False):
            message_ids = [email.message_id for email in emails]
            client.mark_as_read(message_ids)

    except FileNotFoundError as e:
        errors.append(f"Gmail credentials not found: {e}")
    except Exception as e:
        errors.append(f"Email ingestion error: {e}")

    return {
        'emails': emails,
        'errors': errors
    }
