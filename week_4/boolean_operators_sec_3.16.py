"""
Boolean Operators
"""

# boolean, True, False
having_a_great_time = True
if having_a_great_time:
    print("Awesome!!")
    
ready_to_quit = False
if ready_to_quit:
    print("Keep going!!")
else:
    print("Keep up the good work!!")

# comparison operators
age = 25
old = age > 90
print("old: ", old)

# and & not
if having_a_great_time and not ready_to_quit:
    print("Awesome, keep up the great work!!")

# or statement

print(True or False) #True
print(True or True) #True
print(False or True) #True
print(False or False) #False

#or is like addition
# 1 + 1 = 1 #boolean
# 1 + 0 = 1
# 0 + 1 = 1
# 0 + 0 = 0

# and statement

print(True and False) #False
print(True and True) #True
print(False and True) #False
print(False and False) #False

#and is like multiplication
# 1 * 0 = 0
# 1 * 1 = 1
# 0 * 1 = 0
# 0 * 0 = 0


age = 25
parent_permission = False # because I don't need permission
can_you_fly = age > 14 or (age <= 14 and parent_permission)
print("can_you_fly: ", can_you_fly)

age = 12
parent_permission = True 
can_you_fly = age > 14 or (age <= 14 and parent_permission)
print("can_you_fly: ", can_you_fly)

age = 12
parent_permission = False
can_you_fly = age > 14 or (age <= 14 and parent_permission)
print("can_you_fly: ", can_you_fly)