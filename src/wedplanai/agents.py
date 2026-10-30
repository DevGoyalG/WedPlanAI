from langchain.agents import create_agent
from langchain.tools import tool
from langchain.messages import HumanMessage
from .models import groq_model
from .tools import search_web
import logging


# Logging Configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)


# Creating Sub-Agents
logging.info("Initializing SubAgent1...")
subagent1 = create_agent(
    model=groq_model,
    tools=[search_web],
    name="SubAgent1"
)

logging.info("Initializing SubAgent2...")
subagent2 = create_agent(
    model=groq_model,
    tools=[search_web],
    name="SubAgent2"
)


# Delegation Tools
@tool
def delegate_to_subagent1(query: str) -> str:
    """Delegate wedding-related web research to SubAgent1."""

    logging.info(f"Delegating query to SubAgent1: {query}")

    response = subagent1.invoke({
        "messages": [HumanMessage(content=query)]
    })

    return response["messages"][-1].content


@tool
def delegate_to_subagent2(query: str) -> str:
    """Delegate wedding-related web research to SubAgent2."""

    logging.info(f"Delegating query to SubAgent2: {query}")

    response = subagent2.invoke({
        "messages": [HumanMessage(content=query)]
    })

    return response["messages"][-1].content