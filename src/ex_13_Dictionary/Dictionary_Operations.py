# Dictionary
# Key Value Pair
# Syntax { key:value }
# Dictionary is Unordered, mutable, and indexed collection of key-value pairs in Python.
# Duplicate keys will be overridden with the last value

my_dict = {
    "name": "Aman",
    "age": 34,
    "role": "SDET",
    "experience": 3,
    "married": True
}

print(my_dict)

# To create an empty dictionary
empty_dict = dict() or {}
print(empty_dict)

# To access the values from dict print(dict[key])
print(my_dict["age"])

# To update the value of a key from dict
my_dict["age"] = 16
my_dict["married"] = False
print(my_dict)

# To delete the key-value from dict
del my_dict["age"]
print(my_dict)

# To add the key-value to a dictionary
my_dict["age"] = 34
print(my_dict)

# To Iterate through the dictionary
for key, value in my_dict.items():
    print(key, "->", value)

# To check key existence in dictionary
print("age" in my_dict)  # will return true
print("marriedrf" in my_dict)  # will return false

# to check if 2 dictionaries are same
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"a": 1, "b": 2, "c": 3}
print(dict1 == dict2)
