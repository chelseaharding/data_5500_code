"""
Object Oriented Programming
"""

message = "Hello, today is a great day!"

print(type(message))

print("Uppercase:", message.upper()) # built in function to str class
print(message.split())

print([method for method in dir(message) if not method.startswith("_")])

"""
decimal class
"""

from decimal import Decimal

# create a decimal object
tax_rate = Decimal("0.05")
price = Decimal("49.99")

total = price + (price * tax_rate)
print("Total bill:", total)

print(type(price))
