tup = (123, 23, 34, 45, 65, 21, 48)

"""
Approach :
1) Take the largest number that is float("inf")
2) then parse through the list checking if the current element in the list is less than the lowest
3) If it is lowest then replace the lowest with the current number
4) This way which ever is the lowest while iterating through the loop will be replaced
"""


def min_list(tup1):
    lowest = float("inf")
    for i in tup1:
        if i < lowest:
            lowest = i
    return lowest


print(min_list(tup))
