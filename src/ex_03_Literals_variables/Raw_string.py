#  Escape Sequence

# '' or ""
c = 'C'
c1 = "C"

# In a string if we put the escape characters they will be executed whether it might in '' or ""  but if we want to
# escape that then we put r in front of a String known as raw string this way python will know that all the
# characters, even the escape characters are part of the string

directory = "C:\andy\n.txt"
print(directory)

directory = 'C:\andy\n.txt'
print(directory)

directory = r"C:\andy\n.txt"
print(directory)

directory = r'C:\andy\n.txt'
print(directory)
