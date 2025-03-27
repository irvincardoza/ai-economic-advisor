from crewai import Crew, Task
from agents.investment_strategy_agent import investment_strategy_agent
from agents.market_analyst_agent import market_analyst_agent
from agents.report_agent import report_agent
from agents.risk_management_agent import risk_management_agent
from utils.finance import fetch_trend, fetch_volatility

class FinancialAdvisorCrew:
    def __init__(self, ticker):
        self.ticker = ticker
        self.trend = fetch_trend(ticker)
        self.volatility = fetch_volatility(ticker)

    def crew(self):
        # Tasks
        strategy_task = Task(
            description=f"Based on {self.ticker}'s performance, devise an investment strategy for 2025.\nTrend: {self.trend}",
            expected_output="A strategic investment recommendation for the next 12 months",
            agent=investment_strategy_agent,
        )

        analysis_task = Task(
            description=f"Analyze recent market data for {self.ticker}.\nTrend: {self.trend}, Volatility: {self.volatility}",
            expected_output="Key findings from market analysis and stock indicators",
            agent=market_analyst_agent,
        )

        risk_task = Task(
            description=f"Identify risks in investing in {self.ticker}.\nVolatility: {self.volatility}",
            expected_output="Risk assessment report with suggested mitigations",
            agent=risk_management_agent,
        )

        report_task = Task(
            description="Combine all insights and write a professional investment report.",
            expected_output="A detailed, readable report summarizing strategy, analysis, and risk findings",
            agent=report_agent,
        )

        # Crew setup
        return Crew(
            agents=[
                investment_strategy_agent,
                market_analyst_agent,
                risk_management_agent,
                report_agent,
            ],
            tasks=[strategy_task, analysis_task, risk_task, report_task],
            verbose=True
        )
