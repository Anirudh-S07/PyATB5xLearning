# Multiple Inheritance

class Father:
    def father_money(self):
        return 5

    def home(self):                 # Same Name function
        return "This  is home of Father"


class Mother:
    def mother_money(self):
        return 4

    def home(self):                 # Same Name function
        return "This  is home of Mother"


class Son(Father, Mother):
    def print_info(self):
        print("Son")


son_obj = Son()
print(son_obj.father_money())  # from Father class
print(son_obj.mother_money())  # from Mother class
print(son_obj.print_info())  # from Self

# When you have the same name the class that you have inherited first will be called in this case
# Son (Father, Mother) so Father
print(son_obj.home())

