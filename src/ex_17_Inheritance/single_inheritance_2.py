class Parent:
    gold = "2kg"

    def BHK2(self):
        print("2BHK")


class Child(Parent):
    diamond = "Diamond"

    def BHK3(self):
        print("3BHK")


child_object = Child()
print(child_object.gold)
child_object.BHK2()
print(child_object.diamond)
child_object.BHK3()

father_object = Parent()
print(father_object.gold)
father_object.BHK2()
#  father_object.BHK3() Not possible since parent class cannot inherit from child class.