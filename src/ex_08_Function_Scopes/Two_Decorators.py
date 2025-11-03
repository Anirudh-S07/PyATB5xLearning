def decorator1(func):
    def wrapper():  # wrapper name can be anything just match with the return name using wrapper is industry standards
        print("1. 112421412Before the fsgfsgwegtunction is called.")
        print("22414124124.Add Helmet,wsfsgvsdDashcam, gloves, knee guards, licence and RC")
        func()
        print("312412412412.After the fssgfsgunction is called.")
        print("42142153546457.Secure Driving, Leave all the itemsrrggvrvrv")

    return wrapper  # if you use wrapper() it wont work as it is executing rather that calling see below


def decorator2(func):
    def wrapper():  # wrapper name can be anything just match with the return name using wrapper is industry standards
        print("Before the  is called.")
        print("Add Helmet,Dashcam, gloves, knee guards, licence and RC")
        func()
        print("3.After the function is called.")
        print("4.Secure Driving, Leave all the items")

    return wrapper


@decorator1
@decorator2
def sample2():
    print("This is sample 2")


sample2()

"""

In Python, use return func when you want to give back the function itself to be called later (like in decorators or 
closures), and use return func() when you want to call it immediately and return its result. Think of return func as 
handing someone a tool, and return func() as using the tool yourself and giving them the finished product. Example:

def outer():
    def inner():
        return "Hello"
    return inner     # returns function (can be called later)
# usage:
say_hello = outer()
print(say_hello())   # prints "Hello"

def outer2():
    def inner():
        return "Hello"
    return inner()   # calls inner immediately
print(outer2())       # prints "Hello"


👉 Rule of thumb:
If you want deferred execution (decorators, callbacks) → return func
If you want the immediate result → return func()

"""
