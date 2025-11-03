# Lamda Function
# Used to shorten the function into a single line
# Suppose there is this function called cube

def cube(num):
    return num ** 3


print(cube(2))

# How to write this as a lambda function
# lamda parameter:returned logic with the parameter

result_l = lambda num: num ** 3

print(result_l(5))
