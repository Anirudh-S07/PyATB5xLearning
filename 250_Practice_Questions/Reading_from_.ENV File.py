import os

from dotenv import load_dotenv


class Car:

    def __init__(self, name, make, model):
        self.name = name
        self.make = make
        self.model = model

    def start_engine(self):
        print(f"Name {self.name} Make {self.make} Model {self.model} Started")


lambo = Car("Aventino", "Lamborghini", "Ve5")
lambo.start_engine()

mg_hector = Car("Hector", "Resta", "pokas")
mg_hector.start_engine()


# Web Automation
# Page - You are going to Automate

class VWOLoginPage:
    def __init__(self, email_arg, password_arg):
        self.email = email_arg
        self.password = password_arg

    def login_confirmation(self):
        if self.email == "pramod@gmail.com" and self.password == "Pass1234":
            return "Allowed, Login Success"
        else:
            return "Login Failed"


email = input("Enter the email: \n")  # We will read from test data file in Excel,CSV or ENV file in future

password = input("Enter the password: \n")

obj1 = VWOLoginPage(email, password)
print(obj1.login_confirmation())

# If you want to read from env file install pip install python-dotenv
# Create env file
# import os at the top
# from dotenv import load_dotenv at the top
# set the path in the parameter dotenv_path

load_dotenv(dotenv_path=r"../Project_Files/.env")

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

print(email, password)

load_from_env = VWOLoginPage(email, password)
print(load_from_env.login_confirmation())
