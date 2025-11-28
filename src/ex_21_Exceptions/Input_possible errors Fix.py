print(" --- Start of the Program")
# Try and Except to fix

try:
    a = int(input("Enter num 1"))
    b = int(input("Enter num 2"))
    c = a / b
    print("result is", c)  # Possible errors might be Zero division error, Value error,
except Exception as e:
    print(e)

    print(" --- End of the Program")
