import requests
import json
import time
    
ticker = 'AAPL'
url = "https://financialmodelingprep.com/stable/historical-price-eod/full?symbol="+ticker+"&from=2025-09-23&to=2026-09-23&apikey=x8xwEwpa1ujKsPAqiLDeXut6G2j11qQ1"


# see what it looks like
stock_txt = requests.get(url).text
stock_dct = json.loads(stock_txt)
date_key = "date"
close_key = "close"


# json.dump(stock_dct, open("stock_dict.json", "w"), indent=4)

data = []
for dict in stock_dct:
    data.append(dict[date_key]+", "+str(dict[close_key]))
    # print(dict[date_key]+", "+str(dict[close_key]))

print(data)
data = data[::-1]

