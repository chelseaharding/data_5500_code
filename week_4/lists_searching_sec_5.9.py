"""
List Searching
"""

fav_colors = ["red", "yellow", "green", "blue", "orange", "pink", "green"]
print(fav_colors.index("green"))

if "Green" not in fav_colors:
    print("Green is in the list")
else:
    print("that value is not in the list")