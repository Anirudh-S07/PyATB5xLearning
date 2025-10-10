# Program - if age >18 - print you can go to goa and vote else not

user_age = int(input("Enter your age :\n"))

if user_age >= 18:
    print("you can go to goa and vote")
else:
    print("No you cannot go to goa and vote")

# ternary
print("you can go to goa and vote" if user_age >= 18 else "No you cannot go to goa and vote")
