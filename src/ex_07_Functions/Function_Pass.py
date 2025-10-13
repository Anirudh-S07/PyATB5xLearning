def first_part_last():
    pass  # Meaning in future I will complete this function


first_part_last()  # Nothing will happen


def greet_every_one():
    print("Yes, Hello every one")


# Function inside function
def greet():
    greet_every_one()
    print("Hello ram")

greet()