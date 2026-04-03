from services.data_service import get_data
from config import TICKERS, PERIOD, INTERVAL

def run_scanner():
    results = []

    for ticker in TICKERS:
        data = get_data(ticker, PERIOD, INTERVAL)

        if len(data) < 50:
            continue

        last = data.iloc[-1]

        results.append(f"{ticker} checked")

    return results
