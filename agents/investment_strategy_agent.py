# agents/investment_strategy_agent.py
from crewai import Agent
from utils.finGPT_wrapper import FinGPTWrapper

def create_investment_strategy_agent():
    return Agent(
        role="Investment Strategist",
        goal="Recommend 3-5 actionable investment strategies.",
        backstory="An expert advisor helping investors maximize ROI through AI insights.",
        llm=FinGPTWrapper()
    )
