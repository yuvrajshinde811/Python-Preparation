# Create student class that takes name & marks of 3 subjects as arguments in constructor.Then create a method to print the average.

# class Student():
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def average(self):
#         sum = 0
#         for i in self.marks:
#             sum += i
#         avg = sum / len(self.marks)
#         print(f"Hi, {self.name} your average score is {avg:.2f}")
        
# s1 = Student("Yuvi", [98, 70, 67])
# s1.name = "Patil"
# s1.average()


#Abstraction
# Create Account class with 2 attributes - balance & account no. Create methods for debit, credit & printing the balance.

# class Account():
#     def __init__(self, bal, acc):
#         self.account = acc
#         self.balance = bal
        
#     def debit(self, deb_ammount):
#         self.damt = deb_ammount
#         self.balance = self.balance - self.damt
#         print(f"Your account has debited : {self.damt}")
#         print(f"Your current balance is : {self.get_bal()}")
        
#     def credit(self, cre_ammount):
#         self.balance = self.balance + cre_ammount
#         print(f"Your account has credited : {cre_ammount}")
#         print(f"Your current balance is : {self.get_bal()}")
        
#     def get_bal(self):
#         return self.balance


# acc1 = Account(50000, 12345)
# acc1.credit(10000)



# Inheritance

# class Car():
#     @staticmethod
#     def start():
#         print("Car Started......")
        
#     @staticmethod
#     def stop():
#         print("Car Stopped.")
        
# class ToyotaCar(Car):
#     def __init__(self, name):
#         self.name = name
        
# car1 = ToyotaCar("Fortuner")
# car2 = ToyotaCar("Legender")

# print(car1.name)
# print(car1.start())
# print(car2.name)
# print(car2.stop())



# Super method - it is related to parent class. whenever we need to call the parent attribute like self.type, we use this method


# class Car():
#     def __init__(self, type):
#         self.type = type
        
#     @staticmethod
#     def start():
#         return "Car Started......" 
#         # print("Car Started......")
        
#     @staticmethod
#     def stop():
#         return "Car Stopped." 
#         # print("Car Stopped.")
        
# class ToyotaCar(Car):
#     def __init__(self, name, type): # need to add type in child class also
#         self.name = name
#         super().__init__(type) # we call constructor of super or parent class
        
# car1 = ToyotaCar("Fortuner", "Electric")
# car2 = ToyotaCar("Legender", "petrol")

# print("Car name is",car1.name)
# print("Car type is",car1.type)
# print("and",car1.start())

# print("Car name is",car2.name)
# print("Car type is",car2.type)
# print("and",car2.stop())


#decorators
# Getters
# setters

#Qs. Define a Circle class to create a circle with radius r using the constructor. Define an Area() method of the class which calculates the area of the circle. Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle.

# my ans 

# class Circle():
#     def __init__(self, radius):
#         self.radius = radius
        
#     def area(self):
#         return (22/7) * self.radius ** 2
        
#     def perimeter(self):
#         return 2 * (22/7) * self.radius
          
# c1 = Circle(10)
# print("Radius :", c1.radius)
# print("Area : ",c1.area())
# print("Perimeter : ",c1.perimeter())


# Qs. Create a class called Order which stores item & its price. Use Dunder function_gt ( ) to convey that: order1 > order2 if price of order1 > price of order2
# ans
# class Order():
#     def __init__(self, item, price):
#         self.item = item
#         self.price = price
#     def __gt__(self, other):
#         return self.price > other.price

# order1 = Order("chair", 5000)
# order2 = Order("Table", 10000)
# print("for order 1 : ",order1.item, "-",order1.price)
# print("for order 2 : ",order2.item, "-",order2.price)

# print(order1 > order2)


class BankAccount:
    def __init__(self, acc, bal):
        self.acc = acc
        self.bal = bal
    @property
    def CheckBal(self):
        return self.bal
    
a1 = BankAccount(1234, 50000)
print(a1.bal)

a1.bal = 60000
print(a1.bal)

