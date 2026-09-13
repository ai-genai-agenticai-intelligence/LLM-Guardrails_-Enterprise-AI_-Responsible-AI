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

# Streamlit Cloud secrets support
if not GEMINI_API_KEY:
    try:
        # pyrefly: ignore [missing-import]
        import streamlit as st
        if hasattr(st, "secrets") and "GEMINI_API_KEY" in st.secrets:
            GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
        if hasattr(st, "secrets") and "GEMINI_MODEL" in st.secrets:
            GEMINI_MODEL = st.secrets["GEMINI_MODEL"]
    except Exception:
        pass

if not GEMINI_API_KEY:
    raise RuntimeError(
        "GEMINI_API_KEY is not set. Please set it in your .env file or Streamlit Cloud Secrets."
    )