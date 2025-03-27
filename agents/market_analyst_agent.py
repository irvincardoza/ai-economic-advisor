from crewai import Agent


market_analyst_agent = Agent(
    role='Market Analyst',
    goal='Analyze market trends and extract stock performance insights',
    backstory='You are an expert in technical and fundamental analysis.',
    verbose=True,
    allow_delegation=False,
    llm = "gpt-4"  


)
