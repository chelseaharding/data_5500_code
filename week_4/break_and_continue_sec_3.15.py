"""
Break and Continue
"""

for i in range(20):
    if i == 10:
        continue
    print("i:", i)

print()

for i in range(20):
    if i == 10:
        break
    print("i:", i)


age = 5
while age:
    age += 1
    if age == 56:
        break

    print("age:", age)