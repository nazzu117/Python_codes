"""  Inheritance: Using the properties one class into another class
We can use properties one class propreties another in 2 ways

1.Has-A relationship
2.Is-A relationship

1.Has-A relationship: using class name or ref_variable name we use properties of 
                      one class or module to another class or module.
2.Is-A relationship : without class name or ref_variable name or module name 
                      we can use one class into another class 

                      Is-A relation in python is implemented by inheritance 

"""

## Programe to illustrate Has-A relation (using class and ref_var name) without inheritance

# class A:
#     a=10
#     def __init__(self):
#         self.y=20
#     def m1(self):
#         print("From m1.....@@@")
# class B:
#     z=30
#     def m2(self):
#         print(A.a)    ## Accessing SV of another class using class name 
#         a1=A()        ## object creation statement
#         print(a1.y)   ## Accessing another class NSV using object name
#         a1.m1()       ## Accessing another class method using ref_var(object) without using self
#         print(B.z)
#         sum1=A.a+B.z+a1.y
#         print("Sum1= ",sum1)
# b1=B()
# b1.m2()   


# class x:
#     a=10
#     def __init__(self):
#         self.b=20
#         print("I'm constructor....@@")
#     def m1(self):
#         print("I'm method 1 from class x....@@")
# class y:
#     c=30
#     def m2(self):
#         print("I'm from method 2 from class y....@@")
#     def display(self):
#         self.d=40
#         print(x.a)      ## Accessing SV from class using class name
#         self.x1=x()     ##  creating ref_var of x, here self.x1 is NSV which can accessing NSV of class using ref_ver
#         print(self.x1.b)
#         print(self.x1)
#         print(y.c)      ## Accessing SV of class y
#         print(self.d)   ## Accessing NSV of class x
#         ## We can't access NSV of class x using self bcz,self stores adress of current class object,so to access 
#         # m1() of class x ,create object of class x and using that ref_variable we can access m1()
#         self.x1.m1()

""" Within the same class accesing properties """

# class A:
#     x=10
#     def __init__(self):
#         self.y=20
#         print("Base class constructor...$$$ ")
#     def m1(self):
#         print("From method 1....")
#     def m2(self):
#         print("From method 2....")
#         print(A.x)      ## Accessing SV using class
#         print(self.y)   ## Accessing NSV using self
#         self.m1()       ## Accesing method using self 
# a1=A()
# a1.m1()
# a1.m2()
