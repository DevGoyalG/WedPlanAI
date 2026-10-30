from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

# Initialize Groq Model
groq_model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)

print(groq_model.invoke("Rohit Sharma's jersey number ?").content)