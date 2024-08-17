from crewai import Agent
from dotenv import load_dotenv
import os
from tools import tool
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
## Call the gemini model
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", 
                             verbose=True,
                             temperature=0.5,
                             google_api_key=os.getenv("GOOGLE_API_KEY"))

# Create a senior researcher agent with memory and verbose mode

NewsResearcher = Agent(
    role="Senior Researcher",
    goal="Uncover ground breaking technologies in {topic}",
    verbose=True,
    memory=True,
    backstory=(
        "Driven by curiosity, you are an amazing news researcher who is at the forefront of innovation"
        "eager to explore and share knowledge that could change the world."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True
)

# Create a writing agent responsible in writing blogs
NewsWriter = Agent(
    role="Writer",
    goal="Narrate compelling tech stories about {topic}.",
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplification complex topics, you craft"
        "engaging narratives that captivate and eduacate, bringing new"
        "discoveries to light in an accessible manner."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True
)