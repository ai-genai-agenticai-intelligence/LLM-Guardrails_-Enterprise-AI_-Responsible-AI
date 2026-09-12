# pyrefly: ignore [missing-import]
import os
# pyrefly: ignore [missing-import]
from dotenv import load_dotenv

from pathlib import Path

# Load environment variables from .env file located in this directory
ENV_PATH = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=ENV_PATH)

# Access variables
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

if not GEMINI_API_KEY:
    raise RuntimeError(
        "GEMINI_API_KEY is not set. Please set it in your .env file."
    )