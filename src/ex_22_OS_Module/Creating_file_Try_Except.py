import os
try:
    full_path = os.getcwd()
    full_path_file = full_path + r"\example.txt"
    print(full_path_file)
    # command for creating file is file.open("path or name of the file","mode")
    file = open(full_path_file)  # FileNotFoundError
except Exception as fnfe:
    print(fnfe, "File not found error bro")
finally:
    print("This code will be executed anyhow")


