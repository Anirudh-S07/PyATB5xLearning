import os

file_name2 = "andy2.txt"
content2 = "This is a pramodwewe"
content3 = " This is added asas"

# This is one way, with in Python is a context manager that automatically handles setup and cleanup of resources
# like files, ensuring they are closed safely even if an exception occurs, So no need to close file, Prefer this method

with open(file_name2, "w") as file:
    file.write(content2)

with open(file_name2, "a") as file:
    file.write(content3)

with open(file_name2, "r") as file:
    print(file.read())

os.remove("andy2.txt")

