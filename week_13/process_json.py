"""
Processing Json
"""

import requests
import json


ticker = 'aapl'
url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol="+ticker+"&apikey=NG9C9EPVYBMQT0C8"
request = requests.get(url)

request_dict = json.loads(request.text)
# print(request_dict)

key1 = "Time Series (Daily)"
# key2 = "2026-11-13" # I need all the dates??
key3 = "4. close"

# print(request_dict[key1].keys())

# open a csv file
csv_file = open("/workspaces/data_5500_code/week_13/"+ticker+".csv", "w")

lines = []
for date in request_dict[key1].keys():
    lines.append(str(date+", "+request_dict[key1][date][key3]+"\n"))

lines = lines[::-1]
csv_file.writelines(lines)