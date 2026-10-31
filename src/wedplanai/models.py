from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

# Initialize Groq Model
groq_model = ChatGroq(
    model="qwen/qwen3.8-27b",
    temperature=0,
    max_tokens=900
)

# print(groq_model.invoke("Rohit Sharma's jersey number ?").content)