class user:
    def login(self):
        print("login")

    def register(self):
        print("register")

class student(user):
    def enroll(self):
        print("enroll")

stu1 = student()
stu1.login()

# _____________________________________________________________

# inheriting the rpivate or hidden member or attribute of parents class

class Phone:
    def __init__(self, price, brand):
        self.price = price
        self.__brand = brand

    def buy(self):
        print("its parents class buy method")

class Smartphone(Phone):
    def buy(self):
        print("this is child class buying method")

phone1 = Smartphone(20000, "apple")
print(phone1.__brand)

'''conclusiion:- We cant inherit the private member of parent class'''