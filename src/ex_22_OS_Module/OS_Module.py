import os

# OS it works for Windows, Mac and Linux

print(os.getcwd())  # getting current working directory returns string with the current directory

files = os.listdir('D:/')  # Gives the list of iles in the current directory returns list of strings
print("files in this directory are", files)

os.mkdir("Test2")  # Creates new directory

file_exist = os.path.exists("Test2")  # to check if path exists thus checking if folder exists
print(file_exist)

os.rmdir("Test2")  # To delete the directory

print(os.name)  # to get the operating system name nt == windows, posix == mac and linux




