# agents/risk_management_agent.py
from crewai import Agent
from utils.finGPT_wrapper import FinGPTWrapper

def create_risk_management_agent():
    return Agent(
        role="Risk Analyst",
        goal="Identify and assess risks for financial decisions.",
        backstory="An AI-powered risk manager specializing in global market volatility.",
        llm=FinGPTWrapper()
    )
