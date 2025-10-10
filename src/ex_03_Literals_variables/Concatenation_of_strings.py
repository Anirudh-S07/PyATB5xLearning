name = "This is a line"
name = name + str(1)  # - possible
# *****INTERVIEW QUESTION*****
# name = name + 1  # not possible as it is adding str->name with int->1 TypeError: can only concatenate str (not "int") to str

FName = "Aloha"
LName = "Katrsa"

full_name = FName+LName
print(full_name)
full_name = FName+" "+LName
print(full_name)
