"""
Files
"""

# Opening a file in read mode
file = open("/home/ubuntu/environment/DATA3500_SU_23/week6/content_videos/example.txt", "r")


# Reading the entire contents of the file
# content = file.read()
# print("content:", content)

# Reading the file line by line
lines = file.readlines()
for line in lines:
    print("line:", line)
    
# closing the file
file.close()

# Opening a file in write mode
file = open("output.txt", "w")

# Writing data to the file
file.write("Hello world!\n")
file.write("This is a new line in my file!!!\n")

# Closing the file
file.close()
