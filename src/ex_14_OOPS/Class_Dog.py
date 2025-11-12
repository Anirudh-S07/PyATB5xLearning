class Dog:
    # Attribute
    name = None
    breed = None
    height = None

    # Behavior

    def bark(self):
        print("Barking")

    def sleep(self):
        print("Sleeping")

    def talk(self):
        pass


# Object Ref
krypto = Dog()  # IT is very important that you put () at the end because if not it is just assigning
# a different name to the class

krypto.name = "Krypto"

print(krypto.name)
krypto.sleep()



