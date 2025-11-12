class Dog:
    # Attribute
    name = None
    breed = None
    height = None

    # Constructor __init__() It will be automatically called when you create an Object
    # now
    def __init__(self, name, breed):
        print("I will be called")
        self.name = name  # Now from the constructor parameters you can assign the class attributes to the desired name
        self.breed = breed

    # Behavior

    def bark(self):
        print("Barking")

    def sleep(self):
        print(self.name, "is Sleeping")

    def talk(self):
        pass


chow_ref = Dog(name="Chow", breed="Reteiver")  # Can be given either way like this
Krypto_ref = Dog("Krypto", "Lab")  # Or like this

print(chow_ref.name)
print(Krypto_ref.name)
chow_ref.sleep()
Krypto_ref.sleep()

Dog("kas", "mass")  # here also an object is being created but there is no reference

