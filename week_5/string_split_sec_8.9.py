"""
Splitting and Joining Strings
"""

# split
data_str = "1, 2, 3, 4, 5, 6, 7, 8, 9"
nums = data_str.split(" ")
print("nums:", nums)

# join
new_str = " ".join(nums)
print("new str:", new_str)

new_str = ";".join(nums)
print("new str:", new_str)

# join with list comprehension
# lst = []
# for i in range(100):
#     lst.append(i)

# print(lst)

str_lst = ", ".join([str(i) for i in range(100)])
print(str_lst)

