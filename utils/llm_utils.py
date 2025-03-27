import os
from dotenv import load_dotenv

load_dotenv()

default_llm_config = {
    "model": "gpt-4",
    "api_key": os.getenv("OPENAI_API_KEY")
}
