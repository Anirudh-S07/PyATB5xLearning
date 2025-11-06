list1 = [123, 23, 34, 45, 65, 21, 45]

"""
Approach :
1) Take the largest number that is float("inf")
2) then parse through the list checking if the current element in the list is less than the lowest
3) If it is lowest then replace the lowest with the current number
4) This way which ever is the lowest while iterating through the loop will be replaced
"""


def min_list(list_given):
    lowest = float("inf")
    for i in range(len(list_given)):
        if list_given[i] < lowest:
            lowest = list_given[i]
    return lowest


print(min_list(list1))
