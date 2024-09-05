class Bank:
    def __init__(self, account_number, balance):
        self.balance = balance
        self.__account_number = account_number

    def deposit(self, amount):
        self.balance = self.balance + amount

    def check_balance(self):
        print(self.balance)

    def show_me_account_number(self, is_auth):
        if is_auth == True:
            print(self.__account_number)
        else:
            print("Not Allowed!")

    def __internal_method(self):
        print("Private Method")
        print(self.__account_number)
        self.show_me_account_number()



icici = Bank(9876543210, 100)
# icici.__init__()
icici.deposit(100)
icici.check_balance()
icici.show_me_account_number(False)
icici.deposit(100)
icici.check_balance()
# icici.__internal_method() - Error
