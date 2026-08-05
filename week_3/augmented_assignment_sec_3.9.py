"""
Augmented Assignment
"""

age = 90

age = age + 1
print("age:", age)

age += 1
print("age:", age)

age -= 11
print("age: ", age)

age //= 2
print("age: ", age)

age *= 7
print("age: ", age)


# example

grades = [90, 91, 89, 100, 34]
total = 0

for grade in grades:
    total += grade

print("total grades are:", total)
print("avg grade is:", total/5)