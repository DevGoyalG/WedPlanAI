from langchain.agents import create_agent
from langchain.messages import HumanMessage
from .prompts import WEDDING_PLANNER_AGENT_PROMPT, USER_PROMPT_FOR_MAIN_AGENT
from .models import groq_model
from .agents import delegate_to_subagent1, delegate_to_subagent2
import logging


# Logging Configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)


# Collecting User Requirements
logging.info("Asking user for wedding requirements...")

user_requirements = input(
    "Please enter your requirements and preferences for your wedding: "
)


# Updating System Prompt
updated_system_prompt = WEDDING_PLANNER_AGENT_PROMPT.format(
    requirements=user_requirements
)


# Creating Main Agent
logging.info("Initializing Main Wedding Planner Agent...")

main_wedding_planner_agent = create_agent(
    model=groq_model,
    tools=[delegate_to_subagent1, delegate_to_subagent2],
    name="MainWeddingPlannerAgent",
    system_prompt=updated_system_prompt,
)


# Invoking Main Agent
logging.info("Invoking Main Wedding Planner Agent...")

main_wedding_planner_agent_response = main_wedding_planner_agent.invoke({
    "messages": [
        HumanMessage(content=USER_PROMPT_FOR_MAIN_AGENT)
    ]
})


# Displaying Agent Response
print("\nMain Wedding Planner Agent's Response:")
print(main_wedding_planner_agent_response["messages"][-1].content)