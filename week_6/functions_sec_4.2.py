"""
Functions
"""

square = 2 ** 2
cubed = 2 ** 3
fourth = 2 ** 4


# function definiton
# name, arguments, main body of logic, return

def square(number):
    square_num = number ** 2
    return square_num

print(square(7))
print(square(10))
result = square(5)
result += 4
print("result:", result)

for i in range(1000):
    print(square(i))