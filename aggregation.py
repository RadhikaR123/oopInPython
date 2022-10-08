

class Customer:
    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address

    def edit_profile(self, new_city, new_pin, new_state):
        self.address.city = new_city
        self.address.pincode= new_pin
        self.address.state = new_state

        print("my name is", self.name, "I live in", self.address.city, "pin code is", self.address.pincode)

class Address:
    def __init__(self, city, pincode, state):
        self.city = city
        self.pincode = pincode
        self.state = state

    
add = Address("Indore", 455336, "MP")
cust = Customer("Reena", "female", add)
cust.edit_profile(add.city, add.pincode, add.state)
    