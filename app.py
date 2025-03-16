import yfinance as yf
from agents.market_analyst_agent import create_market_analyst_agent
from agents.investment_strategy_agent import create_investment_strategy_agent
from agents.risk_management_agent import create_risk_management_agent
from agents.report_agent import create_report_agent
from crewai import Crew, Task
from utils.fingpt_wrapper import FinGPTWrapper
from utils.report_generator import generate_pdf_report

fingpt = FinGPTWrapper()

def run_pipeline(user_input):
    # 1. Get market data (example S&P500)
    snp500 = yf.download('^GSPC', period="1d")
    snp500_price = snp500['Close'].iloc[-1] if not snp500.empty else "N/A"
    print("Market Snapshot Fetched ✅")

    # 2. Create agents
    market_analyst = create_market_analyst_agent()
    investment_agent = create_investment_strategy_agent()
    risk_agent = create_risk_management_agent()
    report_agent = create_report_agent()

    # 3. Create Crew + Tasks
    crew = Crew(
        agents=[market_analyst, investment_agent, risk_agent, report_agent],
        tasks=[
            Task(agent=market_analyst, description=f"Analyze {user_input} vs S&P500 at ${snp500_price}"),
            Task(agent=investment_agent, description=f"Give recommendations for {user_input} considering S&P500 at ${snp500_price}"),
            Task(agent=risk_agent, description=f"Evaluate risks for {user_input} vs S&P500 at ${snp500_price}"),
            Task(agent=report_agent, description=f"Summarize findings for {user_input} with S&P500 at ${snp500_price}")
        ]
    )

    # 4. Execute crew pipeline
    result = crew.kickoff()

    # 5. Save output to PDF
    combined_content = "\n".join([task.output for task in crew.tasks])
    generate_pdf_report(combined_content, filename="reports/generated_reports/report.pdf")
    print("✅ Report generated: reports/generated_reports/report.pdf")
