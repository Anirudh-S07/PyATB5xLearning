import math


def power(number):
    return math.pow(number, 2)


# OR

power_result = lambda number: math.pow(int(input("Please input the number that you want to give power to: ")), 2)
print(power_result(3))
