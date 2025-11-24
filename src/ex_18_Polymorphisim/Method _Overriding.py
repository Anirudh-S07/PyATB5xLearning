class Father:
    def home(self):
        print("1BHK")


class Pramod(Father):
    def home(self):
        print("2BHK")


p = Pramod()
p.home()   # will override the

f = Father()
f.home()