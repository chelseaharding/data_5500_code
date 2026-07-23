"""
For Loops
"""

#for loop through a string
name = "Chelsea Harding"
for n in name:
    print(n, end="")
    
print()

#for loop through a list
fav_colors = ["aggie blue", "fighting white", "purple"]
for color in fav_colors:
    print("color: ", color)

#for loop using range
for r in range(1, 11):
    print("r:", r)

#
i = 1
while i < 11:
    print("i: ", i)
    i += 1
    
#grades
grades = [50.0, 45.0, 48.0, 10.0]

#adding grades
tot = 0.0
num_grades = 0
for grad in grades:
    tot += grad
    num_grades += 1

#finding average
avg = tot / num_grades
print("average grade is: ", avg)

