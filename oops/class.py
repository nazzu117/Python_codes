"""
oops - object orient progrimming
python is not completle a objects oriented it supported procedural or functional
Python is a multi-paradigm programming language. Meaning, it supports different programming approach.
One of the popular approach to solve a programming problem is by creating objects.
This is known as Object-Oriented Programming (OOP).

1.Class 
2.Objects ---> 
3.Inheritance
4.Polymerphism

"""

# 1.class ---> Detailed explenation/ a blueprint of object
# 2.object --> an object is instance of a class(calling the class)--An object have two behaviours
# i) attributes eg: parrot is object = name age colour are attributes
# ii) Behaviour =singing and dancing are attributes
# if there is no class and instance variavles we can use @staticmethod , for instance variables we can use @methodclass

# the concept of python OOP's is reusability of code we call it as DRY-"don't repeat yourself"
"""
A class is a code template for creating objects. Objects have member variables and have behaviour 
associated with them. In python a class is created by the keyword class.
An object is created using the constructor of the class. This object will then be called the 
instance of the class. In Python we create instances in the following manner

"""

##simple example of definding a class

class emp_details:
    emp_id=101
    emp_name="Naveen"
    emp_age=29
    print("{} is id of the employee and his name {} his age is {}".format(emp_id,emp_name,emp_age)) # output without calling function
obj=emp_details()
print(obj.emp_id)
print(obj.emp_name)
print(obj.emp_age)  #or 
print(emp_details.emp_name)
print(emp_details.__dict__)


# class parent:
#     def __init__(self,name,iid,city):
#         self.name=name
#         self.iid=iid
#         self.city=city

#     def mymethod(self):
#         print("My name is " + self.name)
#         print("My iid is " + self.iid)
#         print("My city is " + self.city)

# obj = parent("Nazeer",'10001',"Hyderabad")
# print(obj.name)
# print(obj.mymethod())

# class Parrot:
#     # class attribute
#     species = "bird"

#     # instance attribute
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# # instantiate the Parrot class
# blu = Parrot("Blu", 10)
# woo = Parrot("Woo", 15)

# # access the class attributes
# print("Blu is a {}".format(blu.__class__.species))
# print("Woo is also a {}".format(woo.__class__.species))

# # access the instance attributes
# print("{} is {} years old".format( blu.name, blu.age))
# print("{} is {} years old".format( woo.name, woo.age))

# class car:
#     car_name="Audi"     # variables delclired  inside the class are called attributes 
#     car_price=3000
#     car_m_year=2020
#     def car_details(self):   # it's not a normal funtion it's a -->function inside a class is called as method 
#         return "{} price is {} and manufactured in {} very good model".format(self.car_name,self.car_price,self.car_m_year)

# brand=car()
# print(car.car_m_year)
# print(brand.car_price)
# print(brand.car_details())

# example for constructor--> calling the class is called constructor  __init__

# ___init__ calles automatically no need to call it externally

# class Employee:
#     def __init__(self,emp_name,emp_id):
#         self.emp_name=emp_name
#         self.emp_id=emp_id        
#         pass
#     def emp_details(self):
#         return "{} is {} that's it".format(self.emp_name,self.emp_id)

# obj=Employee("praveen",334)


# class Employee:
#     def __init__(self,emp_id,emp_name):
#         self.emp_id=emp_id
#         self.emp_name=emp_name

#         print(emp_id)
#         print(emp_name)
#         pass
#     def emp_details(self):
#         print("{} is for {}".format(self.emp_id,self.emp_name))
    

# emp=Employee(101,"Badara")
# emp=Employee(100,"xakraa")
# print(Employee(103,"raxara"))



# class Dog:
#     # class Attribute
#     # species="mammul"
#     # Initializer / Instance Attributes
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     # Instance method
#     def description(self):
#         return "{} is {} years old".format(self.name,self.age)
#     # Instance method
#     def speak(self,sound):
#         return "{} says {}".format(self.name,sound)

# mickey=Dog("Micky",5)
# # print(mickey.description())
# # print(mickey.speak("Boww Boww"))
# print(mickey.name)