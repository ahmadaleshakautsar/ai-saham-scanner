from services.data_service import get_data
from indicators.indicators import apply_indicators
from config import TICKERS, PERIOD, INTERVAL

def run_scanner():
    results = []

    for ticker in TICKERS:
        try:
            data = get_data(ticker, PERIOD, INTERVAL)

            if len(data) < 50:
                continue

            # APPLY INDICATOR
            data = apply_indicators(data)

            last = data.iloc[-1]

            if last['BUY_SIGNAL']:
                results.append(f"🔥 BUY SIGNAL: {ticker}")

        except Exception as e:
            print(f"Error {ticker}: {e}")

    return results
