import requests
import json


ticker = 'AAPL'
url = 'http://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+ticker+'&apikey=NG9C9EPVYBMQT0C8'
req = requests.get(url)

req_dict = json.loads(req.text)

print(req_dict.keys())

key1 = "Time Series (Daily)" # dictionary with all prices by date
key2 = '4. close'

csv_file = open(ticker + ".csv", "w")

write_lines = []
for date in req_dict[key1]: #this is how you get all the dates as keys to look up data
    # print(date + "," + req_dict[key1][date][key2]) 
    write_lines.append(date + "," + req_dict[key1][date][key2]+"\n")
    
csv_file.writelines(write_lines[::-1])
csv_file.close()
