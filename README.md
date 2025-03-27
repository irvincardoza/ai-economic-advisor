# 💼 AI Financial Advisor (CrewAI + GPT + Live Stock Data)

This project is an **AI-powered financial assistant** that uses OpenAI’s GPT, real-time stock data via `yfinance`, and CrewAI to simulate collaboration between financial agents. It generates a formal, multi-section **investment report PDF** based on your selected stock.

---

## 📊 Key Features

✅ CrewAI multi-agent orchestration  
✅ GPT-3.5-powered investment analysis  
✅ Real-time stock data from Yahoo Finance  
✅ Professional PDF report generation  
✅ CLI interface to enter ticker symbols  
✅ Easily extensible with more agents or web interface  

---

## 🧠 How It Works

1. You enter a **stock ticker** (e.g., `AAPL`, `TSLA`, `GOOG`).
2. The `FinancialAdvisorCrew` orchestrates **3 agents**:
   - **Investment Strategist**: Generates a strategy based on current valuation
   - **Market Analyst**: Evaluates trend data and 6-month history
   - **Risk Manager**: Assesses volatility and risk levels
3. Each agent uses:
   - `yfinance` to pull live stock data
   - `OpenAI GPT-3.5` to generate expert-level text
4. A structured, well organised **PDF report** is generated and saved in `/reports`.

---
