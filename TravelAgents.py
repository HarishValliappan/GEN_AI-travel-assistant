from crewai import Agent, LLM
from TravelTools import search_web_tool  # Ensure this tool is correctly imported and configured
import os
# Initialize LLM once
API_KEY=os.environ.get(GEMINI_API_KEYS)
llm = LLM(model="gemini/gemini-2.0-flash",temperature=0.7,api_key=API_KEY)

# Agents
guide_expert = Agent(
    role="City Local Guide Expert",
    goal="Provides information on things to do in the city based on user interests.",
    backstory="A local expert passionate about sharing city experiences.",
    tools=[search_web_tool],
    verbose=True,
    max_iter=1,
    llm=llm,  # Use the initialized LLM
    allow_delegation=False,
    max_tokens=300,
)

location_expert = Agent(
    role="Travel Trip Expert",
    goal="Provides travel logistics and essential information.",
    backstory="A seasoned traveler who knows everything about different cities.",
    tools=[search_web_tool],
    verbose=True,
    max_iter=1,
    llm=llm,  # Use the initialized LLM
    allow_delegation=False,
    max_tokens=300,
)

planner_expert = Agent(
    role="Travel Planning Expert",
    goal="Compiles all gathered information to create a travel plan.",
    backstory="An expert in planning seamless travel itineraries.",
    tools=[search_web_tool],
    verbose=True,
    max_iter=1,
    llm=llm,  # Use the initialized LLM
    allow_delegation=False,
    max_tokens=300,
)
