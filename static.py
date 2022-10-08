class Atm:
    #static variable
    counter = 1
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.sno = Atm.counter
        Atm.counter+=1
        # self.menu()

    def create_pin(self):
        pin_input = input("please enter your pin:")
        self.pin = pin_input
        print("your pin is created......")
        self.menu()
    
    def deposite(self):
        money_to_deposit = int(input("enter amount you want to deposite: "))
        self.balance = self.balance+ money_to_deposit
        self.menu()

    def withdraw(self):
        amount = int(input("enter amount to withdraw: "))
        if amount > self.balance:
            print("insuffucient balance....")
        else:
            self.balance = self.balance- amount
            print("collect cash, amount remained is - {}".format(self.balance))
        self.menu()
        

    def know_account_balance(self):
        print("your account balance is - {}".format(self.balance))
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
print(SBI.sno)
hdfc = Atm()
print(hdfc.sno)



