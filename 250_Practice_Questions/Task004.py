# Problem : Write a program to take a user age and let him know if he can go to club age is 21

user_age = int(input("Enter your age :\n"))

if user_age >= 21:
    print("you can go to club")
else:
    print("No you cannot go to club")

# ternary
print("you can go to club" if user_age >= 21 else "No you cannot go to club")
