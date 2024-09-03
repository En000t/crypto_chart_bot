from tradingview_ta import TA_Handler, Interval
from config import CRYPTO_PAIRS

def fetch_crypto_charts():
    charts = []
    for pair in CRYPTO_PAIRS:
        handler = TA_Handler(
            symbol=pair,
            screener="crypto",
            exchange="BINANCE",
            interval=Interval.INTERVAL_15_MINUTES
        )
        analysis = handler.get_analysis()
        summary = analysis.summary
        charts.append(f"{pair}: {summary['RECOMMENDATION']}")

    return "\n".join(charts)
