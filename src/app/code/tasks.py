from ..imports.shared_imports import Task
from .tools import tool
from .agents import Agents

# researcher = Agents.researcher_agent()
# writer = Agents.writer_agent()

#research task

class Tasks:
    def research_task():
        research = Task(
            description = ("Identify the next big trend in {topic}. Focus on identifying pros and cons and the overall narrative. Your final report should clearly articulate the key points, its market opportunities and potential risks."),
            expected_output = "A comprehensive 3 paragraphs long report on the latest AI trends",
            tools = [tool],
            agent = Agents.researcher_agent(),
        )
        return research    
    #writer task
    def writer_task():
        write = Task(
            description = ("Compose an insightful article on {topic}. Focus on the latest trends and how it's impacting the industry. This article should be easy to understand, engaging and positive."),
            expected_output = "",
            tools = [tool],
            agent = Agents.writer_agent(), 
            output_file = "news-blog-post.md"
        )
        return write
