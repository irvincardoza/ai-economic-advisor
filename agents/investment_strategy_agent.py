import os
import yfinance as yf
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv(""))

def ask_openai(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def get_stock_data(ticker="AAPL"):
    stock = yf.Ticker(ticker)
    info = stock.info
    return {
        "price": info.get("currentPrice"),
        "pe": info.get("trailingPE"),
        "market_cap": info.get("marketCap"),
        "sector": info.get("sector")
    }

def generate_investment_strategy(ticker="AAPL"):
    data = get_stock_data(ticker)
    prompt = f"""
    You're a financial advisor. Analyze the following stock:
    - Ticker: {ticker}
    - Sector: {data['sector']}
    - Current Price: {data['price']}
    - P/E Ratio: {data['pe']}
    - Market Cap: {data['market_cap']}
    Provide a 2025 investment strategy.
    """
    return ask_openai(prompt)
