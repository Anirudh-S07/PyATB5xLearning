class XYZ:
    def f1(self):
        try:
            a = int(input("Enter a number \n"))
        except Exception as e:
            print(e, "please enter a value in int")
        else:
            print(a)
        finally:
            print("I will be executed anyhow")


obj = XYZ()
obj.f1()
