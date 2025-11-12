class Calculator:
    a = None
    b = None     # This is optional even if you create

    def __init__(self):
        print("DC")

    def sum(self, *args):
        total = 0
        for num in args:
            total += num
        return total

    def diff(self, *args):
        total = args[0]
        for num in args[1:]:
            total -= num
        return total

    def mul(self, *args):
        total = args[0]
        for num in args[1:]:
            total *= num
        return total

    def div(self, a, b):
        total = a / b
        return total


my_calc = Calculator()
a = float(input("Enter the Value of a in numbers: "))
b = float(input("Enter the Value of b in numbers: "))
c = float(input("Enter the Value of c in numbers: "))

print(my_calc.sum(a, b, c, 123), my_calc.diff(a, b, c, 120), my_calc.mul(a, b, c, 100), my_calc.div(a, c))

