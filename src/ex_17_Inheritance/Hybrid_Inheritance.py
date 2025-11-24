# Hybrid Inheritance
# multiple types of inheritance, single, multiple, multilevel, heirarchical

class A:
    def methodA(self):
        return "Method A"


class B(A):
    def methodB(self):
        return "Method B"


class C(A):
    def methodC(self):
        return "Method C"


class D(B, C):
    def methodD(self):
        return "Method D"


d = D()
print(d.methodA())  # Could access from both B and C since both have A
print(d.methodB())  # Could access from both B
print(d.methodC())  # Could access from both C
print(d.methodD())  # Self
