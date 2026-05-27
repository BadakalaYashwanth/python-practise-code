# Creating class
class BankAccount:

    # Constructor
    def __init__(self, account_holder, balance):

        # Public variable
        self.account_holder = account_holder

        # Private variable
        self.__balance = balance


    # Public method
    def check_balance(self):

        print("\nAccount Holder:", self.account_holder)

        print("Current Balance:", self.__balance)


    # Public method with condition
    def withdraw(self, amount):

        # Condition statement
        if amount <= self.__balance:

            self.__balance -= amount

            print("\nWithdrawal Successful")

            print("Remaining Balance:", self.__balance)

        else:

            print("\nInsufficient Balance")


# Creating object
user = BankAccount("Yaswanth", 50000)


# Calling methods
user.check_balance()

user.withdraw(10000)