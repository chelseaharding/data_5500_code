"""
Boolean Operators
"""

# boolean variables
having_a_great_time = True

if having_a_great_time:
    print("Awesome!!")
else:
    print("That's too bad")


# comparisons
age = 45
old = age > 80
print("old:", old)


# and
if having_a_great_time and old:
    print("You are old and having a great time!")

# or
if having_a_great_time or old:
    print("you're either having a great time or you're old...i don't know")

# not
if having_a_great_time and not old:
    print("You're young and ready to party!")

"""
or is like addition

1 + 1 = 1
1 + 0 = 1
0 + 1 = 1
0 + 0 = 0

"""

"""
and is like multiplication

1 * 1 = 1
1 * 0 = 0
0 * 1 = 0
0 * 0 = 0

"""

age = 15
parent_permission = True
can_you_drive = age > 16 or (age == 15 and parent_permission)
print("Can you drive?", can_you_drive)