#Area of arectangle

# class Rectangle():
#     def __init__(self,length,breadh):
#         self.length=length
#         self.breadh=breadh
#     def area(self):
#         return self.length*self.breadh

# l=int(input("Enter the length: "))
# b=int(input("Enter the breadth: "))

# obj=Rectangle(l,b)
# print("Area of Rectangle: ",obj.area())


# find the area of circle

# import math
# class Circle:
#     def __init__(self,r):
#         self.radius=r
#     def area(self):
#         return self.radius**2*math.pi
#     def perimeter(self):
#         return 2*math.pi*self.radius       # we can directly write pi value as 3.1415 insteed 
# mycircle=Circle(10)
# print(mycircle.area())
# print(mycircle.perimeter())


# # area of traingle:-

# class Traingle:
#     def __init__(self,b,h):
#         self.b=ab
#         self.h=h

#     def area(self):
#         return 1/2*a*b

# a=int(input("Enter b : "))
# b=int(input("Enter h : "))

# Area=Traingle(b,h)
# print(Area.area())


# Program that takes the string 
# from the user and prints the string using classes.

# class prepesd:
#     def __init__(self):
#         self.string=""

#     def get(self,string):
#         self.string=input("Enter the string: ")

#     def put(self):
#         print("string is: ")
#         print(self.string)

# obj=prepesd()
# obj.get("h")
# obj.put()

# Basic calculator using class

# class Calculator:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def add(self):
#         return self.a + self.b
#     def sub(self):
#         return self.a - self.b
#     def mul(self):
#         return self.a * self.b
#     def div(self):
#         return self.a / self.b

# a=int(input("Enter a: "))
# b=int(input("Enter b: "))

# obj=Calculator(a,b)

# choice=1

# while choice!=0:
#     print("0. Exit")
#     print("1. Addition: ")
#     print("2. Substraction: ")
#     print("3. Multiplication: ")
#     print("4. Division: ")
#     choice=int(input("Enter choice :"))

#     if choice==1:
#         print("Adition: ",obj.add())
#     elif choice==2:
#         print("Substraction: ",obj.sub())
#     elif choice==3:
#         print("Multiplication: ",obj.mul())
#     elif choice==4:
#         print("Division: ",obj.div())
#     elif choice==0:
#         print("Exiting....!! ")
#     else:
#         print("Invalid selection..!!: ")

# print()


# class BankAccount:
#     def __init__(self):
#         self.balance=0

#     def withdrew(self,amount):
#         self.balance -= amount
#         return self.balance

#     def deposite(self,amount):
#         self.balance += amount
#         return self.balance

# a=BankAccount()
# b=BankAccount()
# print(a.deposite(100))
# print(a.deposite(10000))
# print(a.withdrew(234))


""" Write a Python class to reverse a string word by word? """

# class py_solution:
#     def rec_words(self,a):
#         return " ".join(reversed(s.split()))
# r=py_solution
# print(r.rec_words("heloo world india"))
    

""" Write a Python class to get all possible unique subsets from a set of distinct integers."""

# class Subset:
#     def f1(self, s1):
#         return self.f2([], sorted(s1))

#     def f2(self, curr, s1):
#         if s1:
#             return self.f2(curr, s1[1:]) + self.f2(curr + [s1[0]], s1[1:])
#         return [curr]


# a = []
# n = int(input("Enter number of elements of list: "))
# for i in range(0, n):
#     b = int(input("Enter element: "))
#     a.append(b)
# print("Subsets: ")
# print(Subset().f1(a))