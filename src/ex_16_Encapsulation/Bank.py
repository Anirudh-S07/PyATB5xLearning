class Bank:
    def __init__(self, account_number, balance, account_holder_name):
        self.__account_number = account_number  # private
        self.account_holder_name = account_holder_name  # public
        self.balance = balance

    def check_account_name(self):
        return self.account_holder_name

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def show_account_number(self, is_auth):
        if is_auth == 1234:
            return self.__account_number
        else:
            return "Not allowed"

    def show_if_eligible(self, is_auth):  # to access the private method do this call from public function
        if is_auth == 1234:
            return self.__credit_check()
        else:
            return "Not allowed"

    def __credit_check(self):    # This is a private method can be accessed by only class
        if self.balance > 200000:
            return "Credit card can be processed"
        else:
            return "No credit card for you"


icici = Bank(1234567890, 456756, "anshu")
print(icici.deposit(345))
print(icici.check_account_name())
print(icici.show_account_number(1234))
print(icici.show_if_eligible(1234))









