# Write a program to find the frequency of each character in given string.

string = input("Enter the input string :")

char_count = dict()

# Logic building
# I/P - string
# O/P -> dict

for char in string:
    char_count[char] = char_count.get(char, 0) + 1
    # basically you are increasing the char count by 1 if it is first occurrence it will be 1
print(char_count)
