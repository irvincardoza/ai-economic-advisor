from crewai import Agent


risk_management_agent = Agent(
    role='Risk Manager',
    goal='Identify and mitigate investment risks from stock data',
    backstory='You specialize in portfolio risk, volatility, and macroeconomic shocks.',
    verbose=True,
    allow_delegation=False,
    llm = "gpt-4" 


)
