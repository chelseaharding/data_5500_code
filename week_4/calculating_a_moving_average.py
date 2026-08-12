"""
Calculate a Moving Average
"""

prices = [148.1, 147.5, 146.25, 144.8, 145.5]

# moving three day average
total = 0
for price in prices:
    total += price

avg = total/len(prices)
print("total average:", avg)

three_day_avg = (prices[0] + prices[1] + prices[2])/3
print("three day avg:", three_day_avg)

three_day_avg = (prices[1] + prices[2] + prices[3])/3
print("three day avg:", three_day_avg)

three_day_avg = (prices[2] + prices[3] + prices[4])/3
print("three day avg:", three_day_avg)