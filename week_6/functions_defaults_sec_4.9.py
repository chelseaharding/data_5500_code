"""
Function Defaults
"""

def biggest(arg1, arg2=0, arg3=0, arg4=0, arg5=0):
    biggest = max(arg1, arg2, arg3, arg4, arg5)
    return biggest

# large_boi = biggest(1, 5, 45, 1000009, 9)
# print(large_boi)

large_boi = biggest(-1, 5, 45, -1000009, 90)
print(large_boi)

large_boi = biggest(-1, 5, 45, -1000009)
print(large_boi)

large_boi = biggest(-1, 5, 45)
print(large_boi)

large_boi = biggest(-1)
print(large_boi)

large_boi = biggest()
print(large_boi)