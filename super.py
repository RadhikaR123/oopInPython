'''super(), keyword is used to fetch or inherit parent class attribute or method or constructor'''


class Phone:
    def __init__(self, price):
        self.price = price
        print(self.price)

    def buy(self):
        print(self.price)
        print("I am buying with the price {}, inside phone class..".format(self.price))


class Smartphone(Phone):
    def buy(self):
        super().__init__(20,000)
        super().buy()
        print("I am inside child class, buying with the price {}".format(self.price))

obj = Smartphone("pri")
obj.buy()
print(obj.price)