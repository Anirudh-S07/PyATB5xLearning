set1 = {123, 23, 34, 45, 65, 21, 48}

"""
Approach :
1) Take the smallest number that is float("-inf")
2) then parse through the list checking if the current element in the list is greater than the lowest
3) If it is lowest then replace the lowest with the current number
4) This way which ever is the lowest while iterating through the loop will be replaced
"""


def max_list(set2):
    highest = float("-inf")
    for i in set2:
        if i > highest:
            highest = i
    return highest


print(max_list(set1))

