from argparse import Namespace
import asyncio
import logging
from os import environ
from pathlib import Path

import notion_client as ntn
# import requests

from .cli import parse_args
from .constants import NOTION_API_KEY

def main(args: Namespace) -> int:
    """generic entrypoint for command line interface"""
    # response = reques`ts.post(
    #     "https://api.notion.com/v1/pages",
    #     headers={
    #         'Authorization': f'Bearer {NOTION_API_KEY}',
    #         "Notion-Version": "2026-03-11",
    #         "Content-Type": "application/json",
    #     }
    #     json={
    #         "icon": { "emoji": "🚀" },
    #         "markdown": "# Hello from the API\n\n"
    #         "## Welcome\n\nThis page was created with the Notion API. "
    #         "You just made your first request!\n\n- Read the [API reference]"
    #         "(https://developers.notion.com/reference/intro)\n"
    #         "- Explore [examples](https://developers.notion.com/page/examples)"
    #     },
    # )`
    # html = response.text

    if NOTION_API_KEY is None: 
        print("Undefined environment variable: $NOTION_API_KEY.")
        return 1
    notion = ntn.Client(auth=NOTION_API_KEY)
    
    try:
        new_page = notion.pages.create(
            # parent={"page_id": "TEST1"}, # Notion requires a target parent location context
            icon={"type": "emoji", "emoji": "🚀"},
            properties={
                "title": {
                    "title": [
                        {"text": {"content": "Hello from the Official Python Client!"}}
                    ]
                }
            }
        )
    except ntn.APIResponseError:
        print("Your API key probably expired.")
        raise
    
    print("Success! Page created cleanly.")
    print(f"Page URL: {new_page['url']}")

    return 0

if __name__ == '__main__':
    main(cli.parse_args())