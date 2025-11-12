class Person:
    # Attributes - What you have | Instance Variables | Data Variables | Properties
    id = None
    name = None
    age = None
    email = None
    height = None
    gender = None
    phone_no = None
    address = None

    # Behavior - What you can do ?

    def talk(self):  # NRNA(Non Returning non argument)

        print("I can talk")


# Create an object of the Class
# ObjectRef = ClassName() -> Object
geeta = Person()
geeta.name = "Geeta Sharma"
geeta.gender = "Female"


