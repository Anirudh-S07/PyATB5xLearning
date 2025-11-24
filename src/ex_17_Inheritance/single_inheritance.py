class Father:
    key = "2BHK"

    def car(self):
        return "Father has Car -> Alto", self.key


# Single Inheritance put the class you want to inherit from in the brackets
class Son1(Father):
    key2 = "3BHK"

    def suv(self):
        print("MG Hector, Black")
        print(self.key2)


father_obj = Father()
print(father_obj.car())

son1_obj = Son1()
son1_obj.suv()
print(son1_obj.car()) # inherited by Son1() from Father
print(son1_obj.key)





