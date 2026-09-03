# create a dictionary
person = {}
person["name"] = "Chelsea"
person["age"] = 25
person["employer"] = "Utah State University"
person["height_inches"] = 64
person["favorite_movies"] = ["Marvel", "Jurassic Park", "Treasure Planet"]

# access individual elements of a dictionary
# print(person["name"])
# print(person["age"])


# access elements in a loop
for key in person.keys():
    print(key, ":", person[key])
    

   
 



# checkpoint activity

# Write a program that asks the user the following 
# survey information (a mixture of strings and numbers)
# How many years have you lived in Cache Valley (enter a float)?
# What is your favorite color (enter a string)?
# What is your favorite programming language (enter a string)?

# store the user's answers in a Dictionary
# loop through the dictionary and print all the values








# solution
years = float(input("How many years have you lived in Cache Valley? (enter a float)"))
favorite_color = input("What is your favorite color? (enter a string)")
language = input("What is your favorite programming language? (enter a string)")

personal_info = {}
personal_info["years"] = years
personal_info["color"] = favorite_color
personal_info["lang"] = language

for key in personal_info.keys():
    print(personal_info[key])
    
