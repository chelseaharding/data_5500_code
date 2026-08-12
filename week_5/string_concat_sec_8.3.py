"""
String concatenation
"""

variable = "book"

print("hello", variable, "world")

# string concatenation
first_name = "Chelsea"
last_name = "Harding"
full_name = first_name + " " + last_name

print("full name:", full_name)

# augmented assignment
full_name += ", welcome!"
print(full_name)

fruit = "apple"
for i in range(10):
    fruit *= 2

print(fruit)