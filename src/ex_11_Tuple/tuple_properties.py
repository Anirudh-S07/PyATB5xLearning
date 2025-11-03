# Creating Empty Tuple
t = tuple()
print(t)

# Conversion Of List to Tuple
t1 = tuple(["pramod", "Ujsat", "Kravmaga"])
print(t1)

# Extracting elements from tuple
hero1 = ("Batman", "Bruce Wayne")
hero2 = ("Wonder Woman", "Diana Prince")
new_tuple = (hero1, hero2)
print(new_tuple)
print(new_tuple[0])  # ('Batman', 'Bruce Wayne')
print(new_tuple[0][0])  # Batman
print(new_tuple[0][1])  # Bruce Wayne
print(new_tuple[1][1])  # Diana Prince

# Finding if element is present in tuple
cities = ("Paris", "Delhi", "Cacoa")
print("Paris" in cities)  # True
print("Delhi" in cities)  # True
print("Yellow" in cities)  # False

# How to add things to a tuple
# You need to convert it into a list
cities = ("Paris", "Delhi", "Cacoa")  # need to add Hyd
# cities.append("Hyd")  # AttributeError: 'tuple' object has no attribute 'append'
list_cities = list(cities)
print(list_cities)
list_cities.append("Hyd")
cities = tuple(list_cities)
print(cities)


