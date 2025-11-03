# Tuple
# Collection of Items
# Syntax ()
# Immutable

my_tuple = (1, 4, "t", 5, 8, 9, True)
# my_tuple[3] = 65  # Type Error Tuples don't support item assignment

shopping_list = ["bread", "butter", "Jam"]
shopping_list[1] = "milk"
print(shopping_list)

# Rule of Tuple
my_tuple = ("tta.com", "sdet.live")
print(my_tuple)
my_api_list = list(my_tuple)
print(my_api_list)
# my_tuple[0] = "abc.com"  # Type Error Tuples don't support item assignment

# Real Case, In automation where we use tuples
API_URLs = ("https://awesomeqa.com/", "https://courses.thetestingacademy.com/courses", "https://www.sdetclub.com/")
print(API_URLs[2])
print(API_URLs[1])
