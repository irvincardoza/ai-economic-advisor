import random

def fetch_volatility(ticker):
    return f"{random.uniform(1, 5):.2f}% (simulated daily volatility)"

def fetch_trend(ticker):
    return random.choice([
        "Uptrend with growing investor interest",
        "Sideways movement indicating uncertainty",
        "Downtrend due to recent earnings miss"
    ])
