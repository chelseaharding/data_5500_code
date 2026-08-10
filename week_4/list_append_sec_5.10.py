"""
list appending
"""

lst = []
for i in range(10):
    lst.append(i)

print("lst:", lst)

lst.append(10)
print("lst:", lst)

# insert

lst.insert(0, -1)
print("lst:", lst)

lst.insert(5, 3.5)
print("lst:", lst)

# extend kind of like augmented assignment (+=)
lst.extend((11, 12, 13, 14))
print("lst:", lst)

# remove
lst.remove(10)
print("lst:", lst)

# pop
lst.pop()
print("lst:", lst)

# clear
# lst.clear()
# print("lst:", lst)

# count
for num in lst:
    print(num, "is found", lst.count(num), "times")