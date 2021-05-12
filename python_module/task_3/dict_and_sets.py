
"""Trying dictionaries and sets in python"""

# dictionary task
phonebook = {
    "John": 938477566,
    "Jack": 938377264,
    "Jill": 947662781
}

phonebook.pop("Jill")
phonebook["Jake"] = 938273443

if "Jake" in phonebook:
    print("Jake is listed in the phonebook.")

if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook.")

# set task
a = ["Jake", "John", "Eric"]
b = ["John", "Jill"]
first_set = set(a)
second_set = set(b)
print(first_set.difference(second_set))
