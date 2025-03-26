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

def get_volatility(ticker="AAPL"):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="3mo")
    return hist["Close"].std()

def assess_risk(ticker="AAPL"):
    vol = get_volatility(ticker)
    prompt = f"""
    Assess the investment risk for {ticker}:
    - Volatility (3mo): {vol}
    Rate risk as Low/Medium/High with reasoning.
    """
    return ask_openai(prompt)
