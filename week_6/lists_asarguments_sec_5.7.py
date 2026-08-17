"""
List As Arguments
"""

def sum_all_values(lst):
    total = 0
    for i in lst:
        total += i

    return total


list_for_fun = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum_all_values(list_for_fun))