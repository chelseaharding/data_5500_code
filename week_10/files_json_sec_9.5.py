"""
JSON
"""

import json

my_hobbies = {}
my_hobbies["outdoors"] = ["run", "disc golf", "ski", "paddleboard", "garden"]
my_hobbies["indoors"] = ["read", "write", "sew", "watch movies"]

print("old:", my_hobbies)

json.dump(my_hobbies, open("/workspaces/data_5500_code/week_10/my_hobbies.json", "w"), indent=2)

dict1 = json.load(open("/workspaces/data_5500_code/week_10/my_hobbies.json"))
print("new:", dict1)