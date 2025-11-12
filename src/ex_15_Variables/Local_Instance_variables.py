a = 10


class Person:
    b = 11  # instance variable

    def print_info(self):
        c = 20  # local variable
        print(c)  # If you want to access local variable you don't need self.
        print(self.b)  # If You want to access instance variable you have to use self
        global a  # If you want to access the a above then use this
        print(a)
        a = "hello"  # If you want to change the variable a then do this
        print(a)   # No wit will print Hello


obj1 = Person()
obj1.print_info()

