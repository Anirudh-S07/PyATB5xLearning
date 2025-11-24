# Multilevel Inheritance
# GF -> F -> Son

# Multilevel Inheritance

class GrandFather:
    gold = "2KG"

    def bhk1(self):
        print("1 BHK")


class Father(GrandFather):
    diamond = "22 karat"

    def bhk2(self):
        print("2BHK")


class Son(Father):
    btc = "1BTC"

    def bhk3(self):
        print("3BHK")


son_object = Son()
print(son_object.gold)  # From GrandFather Class
son_object.bhk1()  # From GrandFather Class
son_object.bhk2()  # From Father Class
print(son_object.diamond)  # From Father Class
print(son_object.btc)  # From Self
son_object.bhk3()  # From Self

father_object = Father()
print(father_object.gold)  # From GrandFather Class
father_object.bhk1()  # From GrandFather Class
father_object.bhk2()  # From Father Class
print(father_object.diamond)  # From Father Class

