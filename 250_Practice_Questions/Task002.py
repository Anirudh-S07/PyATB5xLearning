# take 2 input from user and print quotient and remainder

a = int(input("Please Enter number 1: "))
b = int(input("Please Enter number 2: "))

print("the decimal quotient of the numbers are:", (a / b), "The integer quotient of the numbers are:", (a // b),
      "The remainder of the division is ", (a % b))

# using divmod
divmod_result = divmod(a,b)

quotient = divmod_result[0]
remainder = divmod_result[1]
print("The quotient is", quotient, "the remainder is", remainder)
