# Remove duplicate values from Dict

dict1 = {"a": 12, "b": 3, "c": 14, "d": 8, "f": 3}

unique_value_set = set()

result = {}

for key, value in dict1.items():
    if value not in unique_value_set:
        result[key] = value
        unique_value_set.add(value)

print(result)
