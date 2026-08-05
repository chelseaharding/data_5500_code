"""
For Loops
"""

name = "Chelsea Harding"
for letter in name:
    print(letter, end="")


print()


fav_colors = ["Aggie Blue", "Fighting White", "Blush Pink"]
for color in fav_colors:
    print("fav colors:", color)


# range

for i in range(10):
    print(i)

num = 0

while num < 10:
    print(num)
    num = num + 1
