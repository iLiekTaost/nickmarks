from pathlib import Path
from os import environ

from dotenv import load_dotenv

load_dotenv()

TOP_LEVEL = Path(__file__).parent
NOTION_API_KEY = environ.get("NOTION_API_TOKEN")