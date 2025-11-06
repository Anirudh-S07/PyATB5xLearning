# Dictionary from Two Lists use zip method inside the dict method
# First create two lists one for keys and another for values then
# new_dict = dict(zip(keys_list,values_list))

keys = ["name", "role", "experience"]
values = ["Aman", "SDET", 3]

my_dict = dict(zip(keys, values))

print(my_dict)

# if length is not same it will match till where it is present
keys1 = ["name", "role", "experience"]
values1 = ["Aman", "SDET"]

my_dict1 = dict(zip(keys1, values1))

print(my_dict1)

# To merge dictionaries

dict1 = {1: "r", 2: "e", 3: "t"}
dict2 = {4: "h", 5: "h", 6: "j"}

merged_dict = dict1 | dict2
print(merged_dict)

# To get the value from key can use get("key")
print(my_dict.get("name"))

# difference between get("key") and dict["key"] is if key is not present in dict then get() will return None
# it will not throw error, But dict["key"] will throw KeyError: 'ytg'

print(my_dict.get("ytg"))  # Returns None
print(my_dict["ytg"])  # Returns KeyError: 'ytg'
