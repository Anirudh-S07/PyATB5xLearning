# Sort a dictionary by its values in descending order

dict1 = {"a": 12, "b": 3, "c": 14, "d": 8}

sorted_dict = sorted(dict1)
print(sorted_dict)


sorted_key_list = []
sorted_value_list = []
lowest_value = float("-inf")
for key, value in dict1.items():
    sorted_value_list.sort()
    sorted_key_list.append(key)
    sorted_value_list.append(value)

print(sorted_value_list)



my_dict = dict(zip(sorted_key_list, sorted_value_list))
print(my_dict)


