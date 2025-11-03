# List can be converted into a set
list1 = [45.2, 33, 56, 78, 33]
set1 = set(list1)
print(set1)  # the result will be set of unique elements with no order

# Tuple can be converted to set
t = ("The Testing Academy", "for", "The Testing Academy")
print(t)
print(set(t))  # {'for', 'The Testing Academy'}

# Union Adding new set along with the common elements as a unique set
set1 = {1, 2, 3, 7, 8, 9}
set2 = {1, 2, 3, 4, 5, 6}
union_set = set1.union(set2)
print(union_set)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}

# Intersection will give you common elements
intersection_set = set1.intersection(set2)
print(intersection_set)  # {1, 2, 3}

# Difference will give the noncommon elements from the set that the difference is being made
difference_of_set1 = set1.difference(set2)
print(difference_of_set1)  # {8, 9, 7}
difference_of_set2 = set2.difference(set1)
print(difference_of_set2)  # {4, 5, 6}






