# Method Overloading
# Not supported directly but can be done if you give default parameters
class Dog:
    def bark(self):
        print("Dog is barking")

    def bark(self, breed="lab"):
        print(f"Dog with {breed} is barking")


dog = Dog()
dog.bark()
dog.bark("Chow")


class MathUtils:
    def add(self, a=0, b=0):
        return a + b

    def add(self, a=0, b=0, c=0):
        return a + b + c

    def add(self, a=0, b=0, c=0, d=0):
        return a + b + c + d


math = MathUtils()
op1 = math.add(1, 2)
op2 = math.add(1, 2, 3)
op3 = math.add(1, 2, 3, 4)

print(op1, op2, op3)
