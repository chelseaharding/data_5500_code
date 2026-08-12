"""
Files
"""

#opening a file
file = open("/workspaces/data_5500_code/week_5/example.txt")
print(file)

# readlines
lines = file.readlines()
print("lines:", lines)

for line in lines:
    print("line:", line)


# closing the file
file.close()

# three modes: read, write, append

file = open("/workspaces/data_5500_code/week_5/example.txt", "w")

# write a new line
file.write("My favorite thing to write down is this! :) \n")
file.write("This is a new line in my file!!! \n")

file.close()

# append mode

file = open("/workspaces/data_5500_code/week_5/example.txt", "a")
file.write("one more new line good sir! \n")
file.write("See how my old lines are still here? That is append mode! \n")
