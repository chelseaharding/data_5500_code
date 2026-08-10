"""
Lists
"""

class_ages = [41, 52, 21, 22, 19, 65, 22, 90]

print(class_ages[2])
print(class_ages[0])
print(class_ages[-1])

# for loops
for age in class_ages:
    age += 1
    print("age:", age)


i = 0
for age in class_ages:
    # print("class_age[i]:", class_ages[i + 1])
    print("age:", age + 1)
    i += 1


# list of strings

fav_colors = ["aggie blue", "fighting white", "pink"]

for color in fav_colors:
    print("color:", color)
    for letter in color:
        print("letter:", letter)
