"""
Dictionaries
"""

person = {}
person["Name"] = "Chelsea Harding"
person["Employer"] = "Utah State University"
person["Height"] = 64
person["Has_Pets?"] = False
person["Fav_Movies"] = ["Dune", "Spider-Man", "Tarzan"]

# access individual elements of dictionary

# print(person["Has_Pets?"])
# print(person["Name"])
# print(person["Fav_Movies"][0])
# print(person.keys())

# access all elements in a loop
for key in person.keys():
    print(key, person[key])
