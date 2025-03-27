from crew import FinancialAdvisorCrew
from dotenv import load_dotenv
load_dotenv()

def main():
    ticker = input("Enter stock ticker (default: AAPL): ") or "AAPL"
    print(f"\n🚀 Running CrewAI for stock: {ticker}\n")

    crew_instance = FinancialAdvisorCrew(ticker)
    result = crew_instance.crew().kickoff()

    print("\n📝 Final Investment Report:\n")
    print(result)

if __name__ == "__main__":
    main()
