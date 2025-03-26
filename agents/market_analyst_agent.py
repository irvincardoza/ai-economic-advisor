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

def get_historical_prices(ticker="AAPL"):
    stock = yf.Ticker(ticker)
    return stock.history(period="6mo")

def analyze_market_trend(ticker="AAPL"):
    hist = get_historical_prices(ticker)
    avg_close = hist["Close"].mean()
    prompt = f"""
    Analyze the market trend for {ticker}:
    - Avg closing price (6mo): {avg_close}
    Give insight on momentum and direction.
    """
    return ask_openai(prompt)
