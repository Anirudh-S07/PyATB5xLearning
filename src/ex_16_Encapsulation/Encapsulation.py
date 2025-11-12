# Encapsulation
# Hide the data members(class variables, instance variables)
# by using only the methods

class Car:
    def __init__(self):
        self.password = "pramod"  # public instance variable any one can access
        self.__password_secure = 1234  # private instance variable no one can access one can create private variable
        # by putting __ in front of the variable name

    def change_password(self, password):
        self.password = password
        return self.password, self.__password_secure  # if you want to see the value do like this


volvo = Car()
print(volvo.password)
print(volvo.change_password("fred"))
print(volvo.__password_secure)  # AttributeError: 'Car' object has no attribute '__password_secure' cannot access
