import yfinance as yf

def fetch_market_snapshot():
    data = yf.download("^GSPC", period="1mo", interval="1d")
    latest = data.tail(1)
    return latest.to_dict()
