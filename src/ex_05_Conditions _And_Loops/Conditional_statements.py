# If Else Statement
# Problem Find the max of 3 numbers

# logic Building
# User Inputs - num1, num2, num3
# User Output - str with int type of max number

# Logic ? If else if else
# if num1>num2 and num3 then num1 is max
# if num2>num1 and num3 then num2 is max
# if num3>num1 and num2 then num3 is max

# Brute force
num1 = int(input("please enter num1: "))
num2 = int(input("please enter num2: "))
num3 = int(input("please enter num3: "))

if num1 >= num2 and num1 >= num3:
    print(f"{num1} is max")
elif num3 >= num2 and num3 >= num2:
    print(f"{num3} is max")
else:
    print(f"{num2} is max")
# Optimization

