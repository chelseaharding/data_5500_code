"""
Files with open
"""

file = open("/workspaces/data_5500_code/week_5/output.txt", "w")
file.write("hello")
file.close()

# with open
with open("/workspaces/data_5500_code/week_5/output2.txt", "w") as file2:
    file2.write("hello\n")
    file2.write("goodbye\n")


file2_again = open("/workspaces/data_5500_code/week_5/output2.txt")
print(file2_again.readlines())
file2_again.close()