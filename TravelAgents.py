from crewai import Agent
from TravelTools import search_web_tool
#from TravelTools import search_web_tool, web_search_tool
from crewai import LLM
#from langchain_ollama.llms import OllamaLLM


# Initialize LLM
llm = LLM(model="groq/llama-3.1-70b-versatile",
    api_key = "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"
)


# Agents
guide_expert = Agent(
    role="City Local Guide Expert",
    goal="Provides information on things to do in the city based on user interests.",
    backstory="A local expert passionate about sharing city experiences.",
    tools=[search_web_tool],
    verbose=True,
    max_iter=1,
    llm=LLM(model="groq/llama-3.3-70b-versatile",api_key = "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"),
    allow_delegation=False,
    max_tokens=50,
)

location_expert = Agent(
    role="Travel Trip Expert",
    goal="Provides travel logistics and essential information.",
    backstory="A seasoned traveler who knows everything about different cities.",
    tools=[search_web_tool],  
    verbose=True,
    max_iter=1,
    llm= LLM(model="groq/llama-3.3-70b-versatile",api_key = "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"),   # ChatOpenAI(temperature=0, model="gpt-4o-mini"),
    allow_delegation=False,
    max_tokens=50
)

planner_expert = Agent(
    role="Travel Planning Expert",
    goal="Compiles all gathered information to create a travel plan.",
    backstory="An expert in planning seamless travel itineraries.",
    tools=[search_web_tool],
    verbose=True,
    max_iter=1,
    llm=LLM(model="groq/llama-3.3-70b-versatile",api_key = "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"),
    allow_delegation=False,
    max_tokens=50,
)
