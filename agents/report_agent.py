# agents/report_agent.py
from crewai import Agent
from utils.finGPT_wrapper import FinGPTWrapper

def create_report_agent():
    return Agent(
        role="Report Compiler",
        goal="Summarize and format all findings into a report.",
        backstory="An AI system designed to convert financial analyses into client-ready reports.",
        llm=FinGPTWrapper()
    )
