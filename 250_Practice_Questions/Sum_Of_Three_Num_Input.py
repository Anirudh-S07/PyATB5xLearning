# Create a program to sum of three numbers from  user input, if user doesn't enter any number, use defaults as
# 100, 200, 300


num1 = int(input("Please enter 1st number: "))
num2 = int(input("Please enter 2nd number: "))
num3 = int(input("Please enter 3rd number: "))


def sum_of_3_numbers(a=100, b=200, c=300):
    result = a + b + c
    return result


print(sum_of_3_numbers(num1, num2, num3))
print(sum_of_3_numbers())
