from langchain.tools import tool
from tavily import TavilyClient
import logging
import os
from dotenv import load_dotenv
load_dotenv()


# Logging Configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)


# Initialize Tavily Client
tavily_client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)


# Web Search Tool
@tool
def search_web(topic: str) -> str:
    """Search the web for a given topic and return relevant results."""

    logging.info(f"Searching the web for topic: {topic}")
    results = tavily_client.search(topic)
    return str(results)