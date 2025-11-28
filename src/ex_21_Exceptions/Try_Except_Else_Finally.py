# Multiple Exceptions
try:
    a = int(input("Enter num 1"))
    b = int(input("Enter num 2"))
    c = a / b

except ValueError:
    print("This is a value error please enter only numbers")   # If Errors happen these except blocks will be executed
except ZeroDivisionError:
    print("Please enter num 2 greater than zero")
else:
    print("No Errors so This executes: result is", c)  # If no errors happen then else will be executed
finally:
    print(" This will print any way")  # This will be executed always





