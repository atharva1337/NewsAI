from ..imports.shared_imports import *
from ..configuration.environment import load_variables

api_key = load_variables()
class Agents:
    def setup_llm(self):
        self.llm = ChatGoogleGenerativeAI(model = "", verbose = True, temperature = 0.5, google_api_key = api_key) 
        print("llm setup successful")
# Creating a senior researcher agent with memory and verbose mode.
    def researcher_agent(self):
        researcher = Agent(
            role ="Senior Researcher",
            goal ="Uncover groundbreaking technologies in {topic}",
            verbose=True,
            memory=True,
            backstory = ("Driven by curiosity, you are at the forefront of innovation eager to explore and share knowledge that could change the world."),
            tools = [],
            llm = self.llm,
            allow_delegation = True
        )
        print("researcher agent created successfully")
#Creating a writer agent with custom tools responsible in writing news blogs

    def execute_all(self):
        self.setup_llm()
        self.researcher_agent()        
    
    
