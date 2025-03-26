from crewai import Agent, Crew, Task
from agents.investment_strategy_agent import generate_investment_strategy
from agents.market_analyst_agent import analyze_market_trend
from agents.risk_management_agent import assess_risk

class FinancialAdvisorCrew:
    def __init__(self, ticker: str):
        self.ticker = ticker
        self._build_crew()

    def _build_crew(self):
        self.investor = Agent(
            role="Investment Strategist",
            goal="Create a smart 2025 investment plan",
            backstory="Experienced Wall Street strategist using live data.",
            tools=[], verbose=True
        )

        self.analyst = Agent(
            role="Market Analyst",
            goal="Provide stock market trend insights",
            backstory="Specialist in market momentum and forecasting.",
            tools=[], verbose=True
        )

        self.risk_mgr = Agent(
            role="Risk Manager",
            goal="Assess risk and volatility of investment",
            backstory="Financial risk expert evaluating stock behavior.",
            tools=[], verbose=True
        )

        self.task1 = Task(
            description=f"Evaluate {self.ticker} and provide a long-term investment strategy.",
            agent=self.investor,
            expected_output=generate_investment_strategy(self.ticker)
        )

        self.task2 = Task(
            description=f"Analyze historical price trends for {self.ticker} and market indicators.",
            agent=self.analyst,
            expected_output=analyze_market_trend(self.ticker)
        )

        self.task3 = Task(
            description=f"Assess risk exposure for {self.ticker} based on volatility.",
            agent=self.risk_mgr,
            expected_output=assess_risk(self.ticker)
        )

        self.crew = Crew(
            agents=[self.investor, self.analyst, self.risk_mgr],
            tasks=[self.task1, self.task2, self.task3],
            verbose=True
        )

    def run(self):
        return self.crew.run()
