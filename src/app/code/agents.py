from ..imports.shared_imports import *
from ..configuration.environment import gemini_key
from .tools import tool

def setup_llm():
    api_key = gemini_key()
    llm = ChatGoogleGenerativeAI(model = "gemini-1.5-flash", verbose = True, temperature = 0.5, google_api_key = api_key) 
    return llm
    
class Agents:
# Creating a senior researcher agent with memory and verbose mode.
    def researcher_agent():
        researcher = Agent(
            role ="Senior Researcher",
            goal ="Uncover groundbreaking technologies in {topic}",
            verbose=True,
            memory=True,
            backstory = ("Driven by curiosity, you are at the forefront of innovation eager to explore and share knowledge that could change the world."),
            tools = [tool],
            llm = setup_llm(),
            allow_delegation = True
        )
        return researcher
#Creating a writer agent with custom tools responsible in writing news blogs
    def writer_agent():
        writer = Agent(
            role ="Writer",
            goal ="Narrate compelling tech stories about {topic}",
            verbose=True,
            memory=True,
            backstory = ("With a flare for simplifying complex topics, you craft engaging narratives that captivate and educate, bringing new discoveries to light in an accessible manner."),
            tools = [tool],
            llm = setup_llm(),
            allow_delegation = True
        )
        return writer
    
    
