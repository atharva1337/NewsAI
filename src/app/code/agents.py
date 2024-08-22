from ..imports.shared_imports import *
from ..configuration.environment import gemini_key
from .tools import tool
api_key = gemini_key()
class Agents:
    def setup_llm(self):
        self.llm = ChatGoogleGenerativeAI(model = "gemini-1.5-flash", verbose = True, temperature = 0.5, google_api_key = api_key) 
        print("llm setup successful")
# Creating a senior researcher agent with memory and verbose mode.
    def researcher_agent(self):
        researcher = Agent(
            role ="Senior Researcher",
            goal ="Uncover groundbreaking technologies in {topic}",
            verbose=True,
            memory=True,
            backstory = ("Driven by curiosity, you are at the forefront of innovation eager to explore and share knowledge that could change the world."),
            tools = [tool],
            llm = self.llm,
            allow_delegation = True
        )
        print("researcher agent created successfully")
#Creating a writer agent with custom tools responsible in writing news blogs
    def writer_agent(self):
        writer = Agent(
            role ="Writer",
            goal ="Narrate compelling tech stories about {topic}",
            verbose=True,
            memory=True,
            backstory = ("With a flare for simplifying complex topics, you craft engaging narratives that captivate and educate, bringing new discoveries to light in an accessible manner."),
            tools = [tool],
            llm = self.llm,
            allow_delegation = True
        )
        print("writer agent created successfully")

    def execute_all(self):
        self.setup_llm()
        self.researcher_agent()
        self.writer_agent()       
    
    
