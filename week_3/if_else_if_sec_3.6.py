"""
If Statements
"""

if 5 < 10:
    print("five is greater")
    print("its a great day")

if 10 > 5:
    print("ten is greater")


print(10 < 5)
print(10 > 5)
print(10 <= 5)
print(10 >= 5)
print(10 == 5)
print(10 != 5)

"""
If Else
"""

grade = 95

if grade >= 95:
    print("You have an A in the class! Great work!")
else:
    print("You are still learning a lot!")

"""
If Elif
"""

grade = 45

if grade >= 95:
    print("A")
elif grade >= 90:
    print("A-")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
else:
    print("You should go get help! You can totally do this!")


