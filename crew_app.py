from crew import FinancialAdvisorCrew
from utils.report_generator import generate_pdf_report

def main():
    ticker = input("Enter stock ticker (default: AAPL): ").upper() or "AAPL"
    crew = FinancialAdvisorCrew(ticker)
    final_report = crew.run()

    # Format sections into a dictionary (manual split)
    sections = {
        "📊 Investment Strategy": final_report[0],
        "📈 Market Analysis": final_report[1],
        "⚠️ Risk Assessment": final_report[2]
    }

    pdf_path = generate_pdf_report(ticker, sections)
    print(f"\n✅ PDF Report saved to: {pdf_path}")

if __name__ == "__main__":
    main()
