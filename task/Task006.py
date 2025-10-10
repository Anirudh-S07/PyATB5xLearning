# Find the max of 2 numbers without using max() or min ()
a = float(input(" Please enter the first num :\n"))
b = float(input(" Please enter the second num :\n"))

# ternary
print(f"{a:.2f}is greater" if a > b else f"{b:.2f} is greater")

# if else
if a > b:
    print(f"{a:.2f}is greater")
else:
    print(f"{b:.2f} is greater")
