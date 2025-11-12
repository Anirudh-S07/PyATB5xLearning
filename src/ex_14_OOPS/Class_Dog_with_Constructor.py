class Dog:
    # Attribute
    name = "Chow"
    breed = None
    height = None

    # Constructor __init__() It will be automatically called when you create an Object
    def __init__(self):
        print("I will be called")

    # Behavior

    def bark(self):
        print("Barking")

    def sleep(self):
        print("Sleeping")

    def talk(self):
        pass


# Object Ref
chow_ref = Dog()  # At this point the object has been created, and immediately 'I will be called'
# will be printed as the constructor is being called automatically
mow_ref = Dog()   # At this point the object has been created, and immediately 'I will be called'
# will be printed as the constructor is being called automatically


print(chow_ref.name)  # will print Chow as it is already given in the class
print(mow_ref.name)   # will print Chow as it is already given in the class






