# agents/market_analyst_agent.py
from crewai import Agent
from utils.finGPT_wrapper import FinGPTWrapper

def create_market_analyst_agent():
    return Agent(
        role="Market Analyst",
        goal="Analyze current market trends and provide insights.",
        backstory="A Wall Street veteran using AI to forecast market trends.",
        llm=FinGPTWrapper()
    )
