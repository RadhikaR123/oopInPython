#  Technically method overloading does not work in python but we can make it work by changing our code


# class Geometry:
#     def area(self,radius):
#         print("area of circle", 3.14*radius*radius)

#     def area(self, a,b):
#         print("area of rectangle", a*b)

# obj = Geometry()
# obj.area(2)

'''above code is valid for java, we can call both area method by passing the argument as required
this time the circle area will be executed, but it wont work for python'''


class Calculation:
    def area(self,a, b=0):
        if b==0:
            print("circle area", 3.14*a*a)

        else:
            print("rectangle area", a*b)

obj1 = Calculation()
obj1.area(3)
obj1.area(2,3)
