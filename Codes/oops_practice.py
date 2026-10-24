# 🧪 OOP Practice Set — Level 1

# -------------------------------
# 🧩 Problem 1 — Employee Class
# -------------------------------

# Create a class Employee

# Attributes:
# - name
# - salary

# Methods:
# - increase_salary(percent) → increase salary by given percent
# - display() → print employee details (name and salary)

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def increase_salary(self, percentage):
        self.salary = self.salary + (self.salary * percentage / 100)
        
    def display(self):
        print(f"Name is - {self.name}")
        print("Basic salary - ", e1.salary)
        print(f"Incremented Salary is -{self.salary}")
        
e1 = Employee("yuvraj", 10000)
e1.increase_salary(10)
e1.display()


# -------------------------------
# 🧩 Problem 2 — Rectangle Class
# -------------------------------

# Create a class Rectangle

# Attributes:
# - length
# - width

# Methods:
# - area() → return area of rectangle
# - perimeter() → return perimeter
# - is_square() → return True if length == width, else False

class Rectangle:
    def __init__(self, length, width):
        self.len = length
        self.wid = width
    
    def area(self):
        return self.len * self.wid
    
    def perimeter(self):
        return 2 * self.len + 2 * self.wid
    
    def is_square(self):
        return self.len == self.wid
    
r1 = Rectangle(7 , 5)
print("Area -", r1.area())
print("Perimeter -", r1.perimeter())

if r1.is_square():
    print("its square")
else:
    print("its rectangke")



# -------------------------------
# 🧩 Problem 3 — BankAccount Class
# -------------------------------

# Create a class BankAccount

# Attribute:
# - _balance (protected)

# Requirements:
# - Getter → return balance using @property
# - Setter → update balance (only allow positive values)

# Methods:
# - deposit(amount) → add amount to balance
# - withdraw(amount) → subtract amount (check if enough balance)

class BankAccount:
    def __init__(self, balance):
        self._balance = balance
    
    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, value):
        if(value > 0):
            self._balance = value
        else:
            print("invalid value")
            
    def deposit(self, amount):
        self._balance = self._balance + amount
        return self._balance
    
    def withdraw(self, amount):
        if(amount > 0):
            self._balance = self._balance + amount
        return self._balance
            
a1 = BankAccount(5000)
print(a1.balance)

a1.balance = 10000
print(a1.balance)

a1.deposit(2000)
print(f"balance after deposit - {a1.deposit}") 