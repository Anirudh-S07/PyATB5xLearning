def even_odd(num):
    if num % 2 == 0:
        return "EVEN"
    else:
        return "ODD"

        # Ternary operator


even_odd_result = lambda num: "Even" if num % 2 == 0 else "ODD"
print(even_odd_result(8))

# Remember lambda is not recommended for multiple conditions
