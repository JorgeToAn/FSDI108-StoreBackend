# importing the dictionary
from data import me

# getting data
print(me["first_name"])

# modify
me["color"] = "Turqoise"

# add
me["height"] = "1.90m"

# read non existing key
# print(me["title"]) # will crash the code

# check if a key exists
if "title" in me:
    print(me["title"])

# print the full address
my_address = me["address"]
print(my_address["street"], str(my_address["number"]), my_address["city"])
print(my_address.values())