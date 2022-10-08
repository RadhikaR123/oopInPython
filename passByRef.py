''' we can also pass a class's object as a perameter of a func, rhis is called pass by reference'''


class Customer:
    def __init__(self, name):
        self.name = name

def greet(customer_name):
    print("hello", customer_name.name)


cust = Customer("Radhika")
greet(cust)