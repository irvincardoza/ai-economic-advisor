from crewai import Agent


report_agent = Agent(
    role='Report Writer',
    goal='Compile a well-structured investment report from findings',
    backstory='You are a financial content specialist creating investor-ready reports.',
    verbose=True,
    allow_delegation=False,
    llm = "gpt-4"  


)
