class Home:
    def __init__(self):
        self.public_var = "father"
        self.__private_var = "Child"

    def mom(self):
        return self.__private_var, self.__wife()

    def __wife(self):
        return "Private Wife"


ref1 = Home()
print(ref1.public_var)
# print(ref1.__private_var)  # Not possible since it is private __
print(ref1.mom())  # this is the way if you want to access

