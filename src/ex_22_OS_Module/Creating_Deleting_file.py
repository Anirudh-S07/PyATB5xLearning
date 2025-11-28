import os


full_path = os.getcwd()
full_path_file = full_path + r"\example.txt"
print(full_path_file)

# command for creating file is file.open("path or name of the file","mode")

file = open(full_path_file, "x")  # FileNotFoundError
file_exist = os.path.exists("example.txt")  # to check if path exists thus checking if folder exists
print(file_exist)
file.close()   # you should always close the file before you delete the file
os.remove(full_path_file)
