"""
Substrings
"""

# string.count() function
phrase = "to be or not to be that is the question"

count = phrase.count("to")
print("count:", count)

count = phrase.count("to", 1)
print("count:", count)

count = phrase.count("to", 14)
print("count:", count)

# string index function
index = phrase.index("to")
print("index:", index)

index = phrase.index("to", 10)
print("index:", index)

# in
print("what" in phrase)