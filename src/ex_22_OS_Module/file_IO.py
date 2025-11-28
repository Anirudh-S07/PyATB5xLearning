import os

file_name1 = "andy.txt"
content1 = "This is a pramod"

file_name2 = "andy2.txt"
content2 = "This is a pramodwewe"

# This is one way, with in Python is a context manager that automatically handles setup and cleanup of resources
# like files, ensuring they are closed safely even if an exception occurs, So no need to close file, Prefer this method

with open(file_name2, "w") as file:
    file.write(content2)

with open(file_name2, "r") as file:
    print(file.read())

# This is another way
file1 = open(file_name1, "w")
file1.write(content1)
file1.close()

read_content1 = open(file_name1, "r")
print(read_content1.read())
read_content1.close()

# Deleting the file
os.remove("andy2.txt")
os.remove("andy.txt")
