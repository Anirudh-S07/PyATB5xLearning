class LowBalanceException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)
        # If you want to create a custom exception you have to inherit the exception class in your class and pass the
        # message in its constructor and call the constructor of the Exception class and pass the message as well


balance = 100
withdraw = int(input("enter the amount you want to withdraw"))


if withdraw > balance:
    raise LowBalanceException("Balance is low")
else:
    print(balance - withdraw, "remaining balance")

