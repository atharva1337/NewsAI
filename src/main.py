#main file to run entire project
from app.imports.shared_imports import Crew, Process
from app.code.agents import Agents
from app.code.tasks import Tasks

researcher_agent = Agents.researcher_agent()
writer_agent = Agents.writer_agent()

research_task = Tasks.research_task()
write_task = Tasks.writer_task()

if __name__ == '__main__':
    crew = Crew(agents = [researcher_agent, writer_agent], tasks = [research_task, write_task], process = Process.sequential)
    result = crew.kickoff(inputs = {'topic' : 'AI in healthcare'})
    print(result)