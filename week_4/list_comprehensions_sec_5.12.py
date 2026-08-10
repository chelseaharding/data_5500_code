"""
List Comprehension
"""

# list_name = [item for item in iterable if ______ ]


nums = []
for i in range(10):
    nums.append(i)

nums2 = [num for num in range(10)]

print(nums)
print(nums2)

colors = ["red", "yellow", "green", "blue", "orange", "pink", "green"]

green_colors = [color for color in colors if color == "green"]
print(green_colors)