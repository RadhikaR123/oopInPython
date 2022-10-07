# in this code we are creating a data type, that is fraction, using class

class Fraction:
    def __init__(self, n, d):
        self.numerator = n
        self.denominator = d

    #when we create an object and try to print it, automatically the __str__(magic method) gets executed
    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)

    '''when we want to add, subtract or perform any other operaton on two or more objects, 
    we can create the method like this..'''
    def __add__(self, other_obj):
        temp_num = self.numerator*other_obj.denominator + self.denominator* other_obj.numerator
        temp_den = self.denominator*other_obj.denominator
        return "{}/{}".format(temp_num,temp_den)


frc = Fraction(3,4)
frc1 = Fraction(5,6)
print(frc.__add__(frc1))



    