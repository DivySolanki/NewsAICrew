from crewai import Crew, Process
from agents import NewsResearcher, NewsWriter
from task import ResearchTask, WriteTask
# Forming the tech focused crew with some enhanced configuration.
crew = Crew(
    agents=[NewsResearcher, NewsWriter],
    tasks=[ResearchTask, WriteTask],
    process=Process.sequential,
)

# starting the task execution process with enhanced feedback

result = crew.kickoff(inputs={"topic": "AI in healthcare"})
print(result)
