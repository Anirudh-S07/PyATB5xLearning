# single exception
try:
    a = int(input("Enter num 1"))
    b = int(input("Enter num 2"))
    c = a / b
    print("result is", c)
except Exception as e:
    print(e)

# Multiple Exceptions
try:
    a = int(input("Enter num 1"))
    b = int(input("Enter num 2"))
    c = a / b
    print("result is", c)
except ValueError:
    print(" This is a value error please enter only numbers")
except ZeroDivisionError:
    print("Please enter num 2 greater than zero")


