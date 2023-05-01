"""
INHERTANCE:- 

1.one class getting properties from other class-> inheritance is powerful feature in object orient programe
It refers to defining a new class with little or no modification to an existing class. 
The new class is called derived (or child) class and the one from which it inherits is 
called the base (or parent) class.

                               [OR]

The concept of making avilable the properties of one class to another class is called inheritance

Inheritance is nothing but deriving a new class from exesting one.
The derived class will have the combined features of both exesting and new one.

The execting class is called a Base class or super class or parent class 
The new class is called as derived class or subclass or chaild class

Base class or super class is class from which new class can be created.
Derived class or subclass is a class that inherits or extends the properties of parent class.

                                 [OR]

A class which is extended by another class is known as super or parent class.
A class which is extending another class is called as subclass or  derived or child class. 


1.single inheritance
2.multiple inheritance
3.multilevel inheritance
4.hybrid inheritance
5.heirarical inheritance

"""

""" 1. single inheritance:a child/derived class inheriting the properties from base/parent class 
                          ---> A derived class and a parent class
"""

# class A:
#     def m1(self):
#         print("Printing from m1....")
# a1=A()
# a1.m1()
# print(A.__bases__)

"""
---> object class is base class for all the classes in python
---> here A is derived class with single base class(object class)
---> if a class is not exesting any class then object class is the base class """

"""  programme for a single inheritance """

# class A:
#     x=10
#     def m1(self):
        
#         print("x=",A.x)
# class B(A):
#     y=20
#     def m2(self):
#         z=B.x+B.y
#         print("y=",B.y)
#         print("z=",z)
# b1=B()
# b1.m1()
# b1.m2()
# print(A.__bases__)
# print(B.__bases__)

""" Both super class and sub class properties both can access """

# class A:
#     a=10
#     def m1(self):
#         self.b=20
#         print("Printing from method1 from class A")
# class B(A):
#     c=30
#     def m2(self):
#         self.d=40
#         print("Printing from method2 from class B")

# b1=B()
# b1.m1()
# b1.m2()
# print(b1.b)
# print(b1.d)
# print(B.a)
# print(B.c)


# class school:
#     sc_school="IIT Delhi"
#     sc_location="Delhi"
#     st_name="raman"
#     st_course="MBA"
#     def meth(self):
#         print(school.sc_name)
#         print(school.st_course)

# class student(school):
#     st_name="kamal"
#     st_course="Engineering"
#     st_location="Delhi"
#     def std(self):
#         self.st_city="Hyderbad"
#         print(self.st_city)
#         print("{0} is studying {1} in {2} {3}".format(self.st_name,self.st_course,self.st_location,self.sc_school))
        


# boj=student()
# boj.std()
# print(boj.st_course)
# print(boj.st_name)
# print(boj.st_city)

#-------------------------------------------------------------------------------------------------------------

"""2. multiple inheritance: A derived class with multiple base classes  """

"""  Performing intsum,floatsum,boolsum in deried class by taking features from multiple base classes  """

# class A:
#     x=10
#     y=20
#     def m1(self):
#         print("x=",A.x)
#         print("y=",A.y)
# class B:
#     a=12.4
#     b=5.8
#     def m2(self):
#         print("a=",B.a)
#         print("b=",B.b)
# class C:
#     p=True
#     q=False
#     def m3(self):
#         print("p=",C.p)
#         print("q=",C.q)
# class D(A,B,C):
#     def m4(self):
#         intsum=D.x+D.y
#         floatsum=D.a+D.b
#         boolsum=D.p+D.q
#         print("Intsum=",intsum)
#         print("Floatsum=",floatsum)
#         print("Boolsum=",boolsum)
# d1=D()
# d1.m1()
# d1.m2()
# d1.m3()
# d1.m4()

# print(A.__bases__)
# print(B.__bases__)
# print(C.__bases__)
# print(D.__bases__)

""" If the base classes have method with the same name and using deried class object if we access the method 
then which base class method will executed   """

# class A:
#     x=10
#     y=20
#     def m1(self):
#         print("printing Hello from method 1 in class A ")
#         print("x=",A.x)
#         print("y=",A.y)
# class B:
#     a=3.4
#     b=6.6
#     def m1(self):
#         print("printing Hello from method 1 in class B ")
#         print(B.a)
#         print(B.b)
#         print("a=",B.a)
#         print("b=",B.b)
# class C(A,B):
#     def m2(self):
#         intsum=C.x+C.y
#         floatsum=C.a+C.b
#         print("Integer sum=",intsum)
#         print("float sum=",floatsum)
# c1=C()
# c1.m1()   ## Here m1 of class A is executed bcz while inheriting class A inherting first i.e, we said C(A,B)
#           ## but if we say C(B,A) then m1 of class B executed

# c1.m2()



# class first:
#     course="Data Science"
#     def class_details(self):
#         print("{} is one of the trending course in the industry".format(self.course))
# class secound:
#     course="Django"
#     def course_details(self):
#         print("{} is good for python web developement".format(self.course))
# class third(secound,first):
#     # course="Python"
#     def course_details(self):
#         print("{} is trending programe language amoung all the languages".format(self.course))
    
# obj=third()
# print(obj.course)
# print(obj.course_details())

##---------------------------------------------------------------------------------------------------------

"""3.Multilevel inheritance:-Deriving a class from another deried class  """

# m=45
# class A:
#     x=20
#     y=30
#     print("m=",m)
#     def m1(self):
#         global m    ## forward declaration
#         m=55
#         print("m=",m)
#         print("x=",A.x)
#         print("y=",A.y)
# class B(A):
#     z=30
#     def m2(self):
#         global m 
#         m=60
#         total=B.x+B.y+B.z
#         print("m=",m)
#         print("z=",B.z)
#         print("Total=",total)
# class C(B):
#     def m3(self):
#         avg=(C.x+C.y+C.z)/3
#         print("Avg=",avg)
#         # print("Total",C.total)   
#         print("m=",m)

# c1=C()
# c1.m1()   
# c1.m2() 
# c1.m3() 
# # print("Total=",c1.total)    ## can't access total AttributeError: 'C' object has no attribute 'total'
# print("m=",m)

# print("\n\n\n")

# b1=B()
# b1.m1()
# b1.m2()

# a1=A()
# a1.m1()

# print(A.__bases__)
# print(B.__bases__)
# print(C.__bases__)




# class first:
#     course="Data Science"
#     def class_details(self):
#         return "{} is one of the trending course in the industry".format(self.course)
# class secound(first):
#     course="Django"
#     def course_details(self):
#         return "{} is good fof web developement".format(self.course)
# class third(secound):
#     # course="Python"
#     def course_details(self):
#         return "{} is trending programe language amoung all the languages".format(self.course)
    
# obj=third()
# print(obj.course)
# print(obj.course_details())

"""4. Hybrid inharitance--->combination of multipl and multilevel """


# class first:
#     course="Data Science"
#     def class_details(self):
#         return "{} is one of the trending course in the industry".format(self.course)
# class secound(first):
#     # course="Django"
#     def course_details(self):
#         return "{} is good fof web developement".format(self.course)
# class third:
#     # course="Python"
#     def course_details(self):
#         return "{} is trending programe language amoung all the languages".format(self.course)
    
# class fourth(third,secound):
#     # course="Devops"
#     def course_details(self):
#         return "{} is trending".format(self.course)

# obj=fourth()
# print(obj.course)
# print(obj.course_details())

"""  5. Hairarical inheritance--> 
Hierarchical Inheritence: A base class with multiple derived classes  """

# class Arith:
#     x=20
#     y=10
#     def m1(self):
#         print("x=",Arith.x)
#         print("y=",Arith.y)
        
# class Add(Arith):
#     def m2(self):
#         sum=Add.x+Add.y
#         print("sum=",sum)
        
# class Sub(Arith):
#     def m3(self):
#         diff=Sub.x-Sub.y
#         print("Diff=",diff)
        
# class Mul(Arith):
#     def m4(self):
#         prod=Mul.x*Mul.y
#         print("product=",prod)
        
# class Div(Arith):
#     def m5(self):
#         div=Div.x/Div.y
#         print("Division=",div)
# a1=Add()
# a1.m1()
# a1.m2()

# s1=Sub()
# s1.m3()

# m1=Mul()
# m1.m4()

# d1=Div()
# d1.m5()

# print(Div.__bases__)
# print(Mul.__bases__)
# print(Sub.__bases__)
# print(Add.__bases__)
# print(Arith.__bases__)




# class first:
#     course="Data Science"
#     def class_details(self):
#         return "{} is one of the trending course in the industry".format(self.course)
# class secound(first):
#     # course="Django"
#     def course_details(self):
#         return "{} is good fof web developement".format(self.course)
# class third(first):
#     # course="Python"
#     def course_details(self):
#         return "{} is trending programe language amoung all the languages".format(self.course)
    
# obj=third
# print(obj.course)
# print(obj.course)


# class employee():
# def __init__(self, name, age, salary):     //Hierarchical Inheritance
# self.name = name
# self.age = age
# self.salary = salary
 
# class childemployee1(employee):
# def __init__(self,name,age,salary):
# self.name = name
# self.age = age
# self.salary = salary
 
# class childemployee2(employee):
# def __init__(self, name, age, salary):
# self.name = name
# self.age = age
# self.salary = salary
# emp1 = employee('harshit',22,1000)
# emp2 = employee('arjun',23,2000)
 
# print(emp1.age)
# print(emp2.age)





# super() method

# class first:
#     course="Data Science"
#     def __init__(self):
#         print("heloo world")
#         def class_details(self):
#             print("{} is one of the trending course in the industry".format(self.course))
# class secound(first):
#     course="Django"
#     # def __init__(self):
#     #     print("jeloo world")
        
#     def course_details(self):
#         print("{} is good fof web developement".format(self.course))
#         super().__init__()
   
    
# obj=secound()
# print(obj.course)



## EX:=

# class A:
#     a=10
#     b=20
#     def m1(self):
#         pass
# class B(A):
#     c=30
#     d=40
#     def m2(self):
#         pass

## There are 2 variables (a,b) and 1 method (m1) in class A.
## There are 4 variables (a,b,c,d) and 2 methods (m1,m2) in class B.
## Class B extending the class A, means class be has combined feature of both the classes i.e, A,B
## Class B (sub class ) can access all the properties (a,b,m1) of super class A.

## ------------------------------------------------------------------------------------------------------
# class A:
#     a=10
#     b=20
#     def m1(self):
#         print("From the super class...@@")
#         self.x=234
#         print("a=",A.a)
#         print("b=",A.b)
#         print("x=",self.x)
# class B(A):
#     c=30
#     d=40
#     a=50
#     def m2(self):
#         print("From derived class....@@@")
#         B.a=B.a+5
#         print("a=",B.a)           ## Accessing a of class A
#         print("b=",B.b)           ## Accessing b of class A
#         print("c=",B.c)
#         print("d=",B.d)
#         print("a=",A.a)
#         self.e=B.a+B.b+B.c+B.d
#         print("e=",self.e)
#         print("\n\n")
#         self.m1()                ## Accesing method of class A
#         print("x=",self.x)

# b1=B()
# b1.m2()
# b1.m1()
# print(B.a)
# print(A.a)


""" 
---> Programe to illustrate inheritance
---> programe with global, local, static and NSV's
---> programe with function and method 
"""

# p=70          ## Global variable 
# def show1():
#     print("Function printing this message.... ")

# class A:
#     x=10
#     print(x)
#     def __init__(self):
#         self.y=20
#         print("Constructor of class A printing this message.... ")
#     def display1(self):
#         print("Printing from class A display1 method.... ")
#         print("p=",p)       ## global variable
#         show1()

# class B(A):          ## class B extracting class A
#     z=200
#     print("z=",z)
#     def display2(self):
#         print("printing from class B display2 method.... ")
#     def display3(self):
#         global p       ## forward declaration
#         print("x=",B.x) ## ## Accessing Sv x of class A using class name
#         print("y=",self.y) ## Accessing NSV y of class A using self
#         print("z=",B.z)
#         p=75
#         sum1=B.x+self.y+B.z    ## sum1 is local varible 
#         print("sum=",sum1)
#         print("p=",p)
#         self.display1()   ## Accessing method from class A using self
#         self.display2()   ## Accessing method from class B using self
#         show1()
# b1=B()
# b1.display3()  ## b1 address is stored in self of display3 ,here using self we can also
#                ## access super class properties such as y and diaplay1() bcz they are part of class B
# print(B.x)
# print(b1.y)
# ## print(sum1) ## local variable cant't aceesed from outside the method 
# print(p)

"""
When sub class object is created ,then first constructor of super class is executed 
"""
# class x:
#     def __init__(self):
#         print("printing base class __constructor__....@@@")
#     def m1(self):
#         print("printing from m1()......@@@")
# class y(x):
#     def m2(self):
#         print("printing from m2()....@@@")

# y1=y()
# y1.m1()
# y1.m2()

### --------------------------------------------------------------------------------------------------------------------

# class x:
#     def __init__(self):
#         print("printing base class __constructor__....@@@")
#     def m1(self):
#         print("printing from m1()......@@@")
# class y(x):
#     def __init__(self):
#         print("printing sub class __constructor__....@@@")
#     def m2(self):
#         print("printing from m2()....@@@")
# y1=y()
# print(y1)
# y1.m1()
# y1.m2()
# print(x.__name__)  ## To know the class name
# print(x.__bases__) ## To know the base class of x
# print(y.__bases__) ## To know the base class of y

"""
---> for each and every class in python by default object class is base class
---> if a class is not extending any class then by default it extends object class
---> if we have constructor in super class and sub class,if we create object of sub class,sub class constructor only executed
---> but in java both sub and super class constructor is executed  """

##---------------------------------------------------------------------------------------------------------------



"""
#object class:object class is the super class for every class in python.

#object class is a pre-defined(built-in)class,which is defined in __builtins__ module

#If a class is not extending any other class,then by default that class
#internally extends object class. """

class A:
    pass
class B(A):
    pass
class C(B):
    pass
class D:
    pass

print(B.__bases__) #to know the base class of B
print(A.__bases__) #to know the base class of A, by default i.e object class
print(C.__bases__)
print(D.__bases__)
#help(object)       #to know about object class
#print(dir(object)) #to know the properties of object class
#help(object.__hash__)# to know the hash value of object class








