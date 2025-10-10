r = float(input("please enter the radius"))
pi = 3.14
area = pi * pow(r, 2)  # pi*(r**2)
# To format the decimal in f string inside the variable put var :.2f
print(f"this is the area : {area:.2f}")
print(f"this is the area : {area:.87f}")
print(f"this is the area : {area:.879f}")

import math

area = math.pi * math.pow(r, 2)
print(f"this is the area : {area:.2f}")
