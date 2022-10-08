#  Method overriding

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
phone1.buy()