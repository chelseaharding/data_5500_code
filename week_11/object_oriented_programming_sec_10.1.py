# 1. Everything in Python is an object
# Even basic data types like strings have attributes and methods.
message = "Hello, Object-Oriented Python!"

# Displaying the type of the object
print("Type of message:", type(message))

# Using a method belonging to the str class
print("Uppercase:", message.upper())
print("Split into words:", message.split())


# 2. Using objects from Python's standard library (e.g., Decimal)
from decimal import Decimal

# Creating Decimal objects (frequently emphasized in Deitel for precise financial data)
tax_rate = Decimal("0.05")
price = Decimal("49.99")

# Performing operations using methods/operators defined by the Decimal class
total = price + (price * tax_rate)
print(f"Price: {price}, Total with tax: {total}")

# Checking attributes and methods available on an object using dir()
# (Great for showing students how to inspect unknown objects)
print("\nSample methods available on a string object:")
print([method for method in dir(message) if not method.startswith("_")][:5])