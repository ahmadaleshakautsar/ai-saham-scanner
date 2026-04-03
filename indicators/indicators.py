import pandas as pd
from ta.volatility import AverageTrueRange

def apply_indicators(data):

    # Moving Average
    data['MA20'] = data['Close'].rolling(20).mean()
    data['MA50'] = data['Close'].rolling(50).mean()

    # Trend
    data['trend_up'] = data['MA20'] > data['MA50']

    # Breakout
    data['resistance'] = data['High'].rolling(20).max()
    data['breakout'] = data['Close'] > data['resistance'].shift(1)

    # Volume 1.5x
    data['vol_avg'] = data['Volume'].rolling(20).mean()
    data['volume_valid'] = data['Volume'] > (1.5 * data['vol_avg'])

    # ATR (anti sideways)
    atr = AverageTrueRange(
        high=data['High'],
        low=data['Low'],
        close=data['Close'],
        window=14
    )

    data['ATR'] = atr.average_true_range()

    # Sideways filter
    data['sideways'] = data['ATR'] < data['ATR'].rolling(20).mean()

    # Final Signal
    data['BUY_SIGNAL'] = (
        data['breakout'] &
        data['trend_up'] &
        data['volume_valid'] &
        (~data['sideways'])
    )

    return data
