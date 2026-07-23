"""
print function and strings
"""

# comma separated list
age = 98
print("age: ", age)

# escape characters
print("Welcome\nto\n\tPython!")

print("Backslash: \\")

# line break
print("This print statement is really really really long \
and I want to put it onto 2 lines")


# printing an expression
print("sum of 3 and 5: ", 3+5)

first_name = "Chelsea"
last_name = 'Harding'

print("my name is: ", first_name, last_name)
print("my name is: " + first_name + last_name)

"""
Triple Quote Strings
"""

# including quotes in strings
# you can include double quotes inside single quote strings
print('Display "hi" in quotes')
print("Display \"hi\" in quotes")
print("Display 'hi' in quotes")

# triple line string
story = """Hi this is my string.
This is a really long string, so I am using triple double quotes
to store everything in here.

To continue my story, I wanted to put another line here!

"""
print("story: ", story)

# triple single quote comments
'''
This is a comment, similar to # hashtag character but this is 
used for multi-line comments. Usually at the top of your code to 
provide documentation or an explaination of your code
'''