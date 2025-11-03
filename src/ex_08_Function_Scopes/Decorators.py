def add_extra_security(func):  # func this name can be anything just using func and wrapper are industry standards
    def wrapper():  # wrapper name can be anything just match with the return name using wrapper is industry standards
        print("1. Before the function is called.")
        print("2.Add Helmet,Dashcam, gloves, knee guards, licence and RC")
        func()  # it should just match the parameter name
        print("3.After the function is called.")
        print("4.Secure Driving, Leave all the items")
    return wrapper()


@add_extra_security  # the moment you put this the function above is getting called
def drive_scooty():
    print("Normal Function!")
    print("I am driving Scooty")


# @add_extra_security this cannot be used or called like this as decorator needs a def() or @another_decorator


def new_decorator(func):
    def wrapper():  # wrapper name can be anything just match with the return name using wrapper is industry standards
        print("1. Before the fsgfsgwegtunction is called.")
        print("2.Add Helmet,wsfsgvsdDashcam, gloves, knee guards, licence and RC")
        func()
        print("3.After the fssgfsgunction is called.")
        print("4.Secure Driving, Leave all the itemsrrggvrvrv")
    return wrapper


@new_decorator
def drive_ola_scooty():
    print("ola")


# @new_decorator
# def sample(): if given like this you will get TypeError: new_decorator() takes 0 positional arguments but 1 was given
#     print("this is new") if you don't put the func() in the wrapper
#
# here since we are only returning the wrapper function rather than calling it as we did in the above we will not be
# able to print , In order to print we must call the function as in the wrapper there is execution of the func that is
# func()

drive_ola_scooty()
