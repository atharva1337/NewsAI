#main file to run entire project
from app.code.agents import Agents

agents = Agents()

if __name__ == '__main__':
    agents.execute_all()
    