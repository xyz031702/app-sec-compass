"""
Gmail API Client
Handles OAuth2 authentication and email fetching for Google Alerts
"""
import os
import base64
from pathlib import Path
from typing import Optional

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from .url_decoder import extract_urls_from_html
from ..state import EmailData


# Gmail API scopes - readonly for security
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly',
          'https://www.googleapis.com/auth/gmail.modify']


class GmailClient:
    """
    Gmail API client for fetching Google Alert emails
    """

    def __init__(
        self,
        credentials_path: str = "credentials/credentials.json",
        token_path: str = "credentials/token.json"
    ):
        """
        Initialize Gmail client

        Args:
            credentials_path: Path to OAuth credentials JSON file
            token_path: Path to store/load OAuth token
        """
        self.credentials_path = Path(credentials_path)
        self.token_path = Path(token_path)
        self.service = None
        self._authenticate()

    def _authenticate(self) -> None:
        """Authenticate with Gmail API using OAuth2"""
        creds = None

        # Load existing token if available
        if self.token_path.exists():
            creds = Credentials.from_authorized_user_file(
                str(self.token_path), SCOPES
            )

        # Refresh or get new credentials if needed
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                if not self.credentials_path.exists():
                    raise FileNotFoundError(
                        f"Credentials file not found: {self.credentials_path}\n"
                        "Download from Google Cloud Console and save to this path."
                    )
                flow = InstalledAppFlow.from_client_secrets_file(
                    str(self.credentials_path), SCOPES
                )
                creds = flow.run_local_server(port=0)

            # Save token for future use
            self.token_path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.token_path, 'w') as token:
                token.write(creds.to_json())

        self.service = build('gmail', 'v1', credentials=creds)

    def fetch_unread_alerts(
        self,
        query: str = 'label:"AI Security News" is:unread',
        max_results: int = 50
    ) -> list[EmailData]:
        """
        Fetch unread Google Alert emails

        Args:
            query: Gmail search query
            max_results: Maximum number of emails to fetch

        Returns:
            List of EmailData objects with extracted URLs
        """
        emails = []

        # List messages matching query
        results = self.service.users().messages().list(
            userId='me',
            q=query,
            maxResults=max_results
        ).execute()

        messages = results.get('messages', [])

        for msg_info in messages:
            msg_id = msg_info['id']
            try:
                email_data = self._process_message(msg_id)
                if email_data and email_data.urls:
                    emails.append(email_data)
            except Exception as e:
                print(f"Error processing message {msg_id}: {e}")
                continue

        return emails

    def _process_message(self, message_id: str) -> Optional[EmailData]:
        """
        Process a single email message

        Args:
            message_id: Gmail message ID

        Returns:
            EmailData object or None if processing fails
        """
        message = self.service.users().messages().get(
            userId='me',
            id=message_id,
            format='full'
        ).execute()

        headers = message.get('payload', {}).get('headers', [])
        header_dict = {h['name']: h['value'] for h in headers}

        # Extract HTML body
        html_body = self._extract_html_body(message.get('payload', {}))
        if not html_body:
            return None

        # Extract URLs from HTML
        urls = extract_urls_from_html(html_body)

        return EmailData(
            message_id=message_id,
            subject=header_dict.get('Subject', 'No Subject'),
            sender=header_dict.get('From', 'Unknown'),
            date=header_dict.get('Date', ''),
            urls=urls
        )

    def _extract_html_body(self, payload: dict) -> Optional[str]:
        """
        Extract HTML body from email payload

        Args:
            payload: Gmail message payload

        Returns:
            Decoded HTML content or None
        """
        # Check if payload has body directly
        if payload.get('mimeType') == 'text/html':
            data = payload.get('body', {}).get('data', '')
            if data:
                return base64.urlsafe_b64decode(data).decode('utf-8')

        # Check parts for multipart messages
        parts = payload.get('parts', [])
        for part in parts:
            if part.get('mimeType') == 'text/html':
                data = part.get('body', {}).get('data', '')
                if data:
                    return base64.urlsafe_b64decode(data).decode('utf-8')

            # Recursively check nested parts
            if part.get('parts'):
                result = self._extract_html_body(part)
                if result:
                    return result

        return None

    def mark_as_read(self, message_ids: list[str]) -> None:
        """
        Mark messages as read

        Args:
            message_ids: List of message IDs to mark as read
        """
        for msg_id in message_ids:
            self.service.users().messages().modify(
                userId='me',
                id=msg_id,
                body={'removeLabelIds': ['UNREAD']}
            ).execute()
