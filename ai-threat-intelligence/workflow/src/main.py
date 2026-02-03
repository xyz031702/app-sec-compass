"""
Main Entry Point
CLI interface for running the AI Security Intelligence Agent
"""
import argparse
import os
import sys
from pathlib import Path
from datetime import datetime

from dotenv import load_dotenv

from .graph import run_agent


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description='AI Security Intelligence Agent - Generate intelligence reports from Google Alerts'
    )

    parser.add_argument(
        '--credentials',
        default='credentials/credentials.json',
        help='Path to Gmail OAuth credentials JSON file'
    )
    parser.add_argument(
        '--token',
        default='credentials/token.json',
        help='Path to store/load Gmail OAuth token'
    )
    parser.add_argument(
        '--query',
        default=None,
        help='Gmail search query (default: from GMAIL_SEARCH_QUERY env var)'
    )
    parser.add_argument(
        '--output', '-o',
        default=None,
        help='Output file path (default: stdout)'
    )
    parser.add_argument(
        '--max-emails',
        type=int,
        default=50,
        help='Maximum number of emails to process'
    )
    parser.add_argument(
        '--mark-read',
        action='store_true',
        help='Mark processed emails as read'
    )
    parser.add_argument(
        '--provider',
        choices=['gemini', 'anthropic'],
        default=None,
        help='LLM provider (default: from LLM_PROVIDER env var)'
    )
    parser.add_argument(
        '--model',
        default=None,
        help='LLM model name to use'
    )

    args = parser.parse_args()

    # Load environment variables
    load_dotenv()

    # Build config
    config = {
        'credentials_path': args.credentials,
        'token_path': args.token,
        'max_emails': args.max_emails,
        'mark_as_read': args.mark_read,
    }

    if args.query:
        config['search_query'] = args.query

    if args.provider:
        config['llm_provider'] = args.provider

    if args.model:
        config['llm_model'] = args.model

    # Run agent
    print("Starting AI Security Intelligence Agent...", file=sys.stderr)
    print(f"Processing up to {args.max_emails} emails...", file=sys.stderr)

    try:
        report = run_agent(config)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    # Output report
    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(report)
        print(f"Report saved to: {args.output}", file=sys.stderr)
    else:
        print(report)


if __name__ == '__main__':
    main()
