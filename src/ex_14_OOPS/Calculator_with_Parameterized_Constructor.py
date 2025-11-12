class Calculator:
    def __init__(self, a, b):
        print("DC")
        self.a = a
        self.b = b

    def sum(self):

        return self.a + self.b

    def diff(self):

        return self.a - self.b

    def mul(self):

        return self.a * self.b

    def div(self):

        return self.a / self.b


a1 = float(input("Enter the Value of a in numbers: "))
b1 = float(input("Enter the Value of b in numbers: "))
c1 = float(input("Enter the Value of c in numbers: "))

my_calc = Calculator(a1, b1)

print(my_calc.sum(), my_calc.diff(), my_calc.mul(), my_calc.div())

