class RestfulBooker:

    def __init__(self, name, *args):
        self.name = name
        self.list_of_api = []
        self.links = set()

        for arg in args:
            if isinstance(arg, (list, tuple, set)):
                self.list_of_api.extend(arg)
            else:
                self.list_of_api.append(arg)

    def print_apis(self):
        return self.list_of_api

    def print_set(self):
        self.links = set(self.list_of_api)
        return self.links


obj1 = RestfulBooker("Reddit", "https://github.com/PramodDutta/PyATB6xLearnings/tree/main",
                     "https://github.com/PramodDutta/PyATB6xLearnings/tree/main/src",
                     "https://github.com/PramodDutta/PyATB6xLearnings/tree/main/src/ex_01_Python_Basics",
                     "https://github.com/PramodDutta/PyATB6xLearnings/tree/main/src/ex_02_Keywords_Identifier_Variables",
                     "https://github.com/PramodDutta/PyATB6xLearnings/tree/main/src/ex_03_Literals_Variables",
                     "https://github.com/PramodDutta/PyATB6xLearnings/tree/main/src/ex_04_Operators",
                     "https://github.com/PramodDutta/PyATB6xLearnings/tree/main/src/ex_04_Operators"
                     )

print(obj1.print_apis())
print(obj1.print_set())


def take_inputs():
    result = []
    while True:
        user_input = input("Enter value (type 'end' to stop): ")
        if user_input.lower() == "end":
            break
        result.append(user_input)
    return result


obj2 = RestfulBooker("Youtube", take_inputs())

print(obj2.print_apis())
print(obj2.print_set())
