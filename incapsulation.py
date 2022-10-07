'''We use incapsulation to restrict object or user not to fetch or see or use private data'''

class Atm:
    def __init__(self):
        self.__pin = ""
        self.__balance = 0
        # self.menu()

    def create_pin(self):
        pin_input = input("please enter your pin:")
        self.__pin = pin_input
        print("your pin is created......")
        self.menu()
    
    def deposite(self):
        money_to_deposit = int(input("enter amount you want to deposite: "))
        self.__balance = self.__balance+ money_to_deposit
        self.menu()

    def withdraw(self):
        amount = int(input("enter amount to withdraw: "))
        if amount > self.__balance:
            print("insuffucient balance....")
        else:
            self.__balance = self.__balance- amount
            print("collect cash, amount remained is - {}".format(self.__balance))
        self.menu()
        

    def know_account_balance(self):
        print("your account balance is - {}".format(self.__balance))
        self.menu()

    def menu(self):
        choice= input('''please enter your choice:
        1. press 1 for create pin
        2. press 2 for deposit balance
        3. press 3 to withdraw money
        4. press 4 to know your balance
        5. press 5 to exit
         ''')
        if choice == "1":
            self.create_pin()
        elif choice == "2":
            self.deposite()
        elif choice == "3":
            self.withdraw()
        elif choice == "4":
            self.know_account_balance()
        else:
            pass
SBI = Atm()
print("welcome")
print(SBI.__balance)  #it will now give an error


