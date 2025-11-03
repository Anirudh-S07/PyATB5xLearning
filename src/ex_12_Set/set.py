# SET
# Collection of Unique Elements
# {} - parenthesis

set_of_unique_items = {1, 2, 23, 4, 5, 5, 75, 6, 6, 5, 8, "sfsfs", True, False, False, True}
print(set_of_unique_items)  # will return the set of unique set of elements also remember 1 and True are considered same
# the reason why if you run this print multiple times 'sfsfs' jumps because string hashing is randomized for security
# reasons in each new Python session.
"""
| Element   | Reason kept / removed                                |
| --------- | ---------------------------------------------------- |
| `1`       | same as `True`, kept once                            |
| `False`   | unique, same as 0 if 0 was present                   |
| `True`    | merged with 1                                        |
| `5`, `6`  | duplicates removed                                   |
| `'sfsfs'` | unique string, hash randomization moves its position |
| Others    | unique numeric values                                |

"""

