"""
String Character Test
"""

string = "-12345"
print(string.isdigit())

string = "12345"
print(string.isdigit())

# is alnum

address = " 123 N Main St. Logan, Utah"
print(address.isalnum())
address = address.replace(" ", "")
address = address.replace(".",  "")
address = address.replace(",", "")

print(address)
print(address.isalnum())