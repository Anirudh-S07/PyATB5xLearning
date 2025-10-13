# User Defined
# 1. They cannot return anything , No return
# 2. They have parameters
# 3. No Return Type with Default Argument
# 4. They don't have parameters / arguments

# 1.They cannot return anything , No return
#  No return Type and No Parameter / Argument - NRNP
def greet():
    print("Hello")


greet()


# 2. They have parameters , No Return
def say_hello_user(name):
    print("Hello", name)


say_hello_user("Mald")


# 3. No Return Type with Default Argument ( # positional argument)
def say_hello_default_arg(name="Andy"):
    print("Hello", name.upper())


say_hello_default_arg("Dutta")
say_hello_default_arg()


# Multiple Arguments with no return type
def say_multi_default_arg(name="Andy", name1="Pramod"):
    print("Hello", name.upper(), name1.lower())


say_multi_default_arg("Dutta", "prash")
say_multi_default_arg("Dutta")
say_multi_default_arg(name="Dutta")
say_multi_default_arg(name1="Dutta")
say_multi_default_arg()


# Argument + Return Type
def sum_of_two(a, b):
    return a + b


print(sum_of_two(3, 4))


# Positional Argument + Return Type
def sum_of_two_numbers_with_defaults(num1=100, num2=200):
    print("I will sum the two numbers!")
    return num1 + num2


result = sum_of_two_numbers_with_defaults()
print(result)
result = sum_of_two_numbers_with_defaults(num1=456, num2=34)
print(result)
result = sum_of_two_numbers_with_defaults(num2=34)
print(result)
result = sum_of_two_numbers_with_defaults(34)
print(result)
result = sum_of_two_numbers_with_defaults(num1=34)
print(result)
