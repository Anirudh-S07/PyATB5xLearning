# Take input and create a class

class Person:

    def __init__(self):
        print("I will be called")
        self.name = input("Enter the name \n")
        self.age = input("Enter the age \n")
        self.phone_no = input("Enter the phone_no \n")
        self.occupation = input("Enter the occupation \n")

    def details_of_person(self):
        print(f"The name of the person is {self.name}, Age is {self.age}, occupation is {self.occupation} and phone "
              f"no is {self.phone_no}")


anand = Person()
anand.details_of_person()




