"""
Web Json API
"""
import requests
import json

tickers = ["aapl", "tsla"]

for ticker in tickers:
    url = "https://financialmodelingprep.com/stable/historical-price-eod/full?symbol="+ticker+"&from=2025-09-23&to=2026-09-23&apikey=x8xwEwpa1ujKsPAqiLDeXut6G2j11qQ1"

    stock_info = requests.get(url).text
    # print(stock_info.text)
    stock_json = json.loads(stock_info)

    ticker_key = "symbol"
    date_key = "date"
    close_key = "close"

    for dict in stock_json:
        print("Ticker:", dict[ticker_key], "Date:", dict[date_key], "Price:", dict[close_key])