"""
Polymarphism:- Ability to take more or one form
poly     ---> Many
Morphism ---> Forms or Functionalitys or Logics

Ex:- Deposite ----> Cash or DD or Cheque

Defination: The concept of defining multiple functionalites or logics to perform an operation is known as polimerphism

Types of polymerphisms:

1.Static Polymerphism or compile-time ploymerphism:
   Ex- Method overloading 
       but method overloading is not supported by python 

2.Dynamic polymerphism or run-time polymerphism:
   Ex:- Method Overriding


Method Overloading: Defing 2 or more methods with same name but with different no of arguments or type of arguments

ex: def m1(a,b,c):
        .........
        .........
    def m1(x,y):
        ........
        ........
    def m1(p):
        ........
        ........

"""

# class A:
#     def add(self,x,*y):
#         if(x=="int"):
#             result=0      ## Initial result is 0
#         if(x=="str"):
#             result=" "    ## Initial result is null 
#         for p in y:
#             result=result+p
#         print(result)
#     """def add(self,a):
#         print(a)   """
# a1=A()
# a1.add("int",10,20,30)   ## Performs addition
# a1.add("str","web","technologies")  ## perform concatination
# ### a1.add(12)

"""
Here there is no method overloading or polymerphism because here no multiple methods ,here only one method
performing multiple tasks but in method overloading we define multiple methods
"""

""" Method Overriding: The concept of defining a method with same name and same number parameters in both super and 
                       sub class method is called method overriding

"""

# class X:
#     def m1(self):
#         print("from base class....")

# class Y:
#     def m1(self):
#         print("From sub class...")
# y1=Y()
# y1.m1()   ## Here sub class method is called bcz super class method is overriding with sub class method, to execute
#           ## super class method also call super class
# x1=X()
# x1.m1() 

""" Method overriding is seen in only inheritance """

# class X:
#     def m1(self,a):
#         print("From base class....")
#         self.p=a
# class Y(X):
#     def m1(self):
#         print("From derived class...")
# y1=Y()
# # y1.m1(10)   ## Error bcz method overriding is happend which is not supported 
# y1.m1()

""" Example of method overriding """

# class RBI:
#     x=10
#     def minbalance(self):
#         minbal=0
#         print("Mon_Balance=",minbal)
# class HDFC(RBI):  
#     def minbalance(self):     ## Here min bal is 10000 ,i don't want RBI mibal rules ,so i don't want super class logic to execute
#         minbal=10000            ## so i overrde the method ,so subclass method got executed
#         print("Hdfc Min_balance=",minbal)
# class ICICI(RBI):
#     x=100
#     def minbalance(self):
#         minbal=5000
#         print("Icici Min_balance=",minbal)
# class SBI(RBI):
#     x=10              ## Here i don't want to override, i will follow RBI rules only ,so here i will execute  
#     pass              ## super class method is executed logic only 

# h1=HDFC()
# h1.minbalance()

# i1=ICICI()
# i1.minbalance()

# s1=SBI()
# s1.minbalance()

# print(SBI.x)
# print(RBI.x)
# print(ICICI.x)

"""
while developing web applications most of the classes are pre-defind classes,so we define a user-defined classs
which will extend pre defind classes and overriding the methods of pre defined class  """

# x=10
# print(x)
# print(type(x))

"""
class object:
    def __hash__(self):
        .............     ## generete hashcoad(Adress)
        .............     ## here it got the code to print hash coad value (adress)
        ............. 
class int(object):
    def __hash__(self):
        .............
        .............    ## here it won't print hash value ,bcz it is overridden with different coad 
        .............    ## Here the method also got coad to prent the content not the hash coad (Adress)
"""

""" Overriding the constructor """
# class X:
#     def __init__(self):
#         print("From the constructor of X...") 
# class Y(X):
#     def __init__(self):
#         print("from constructor of Y...")
# y1=Y()

# # ### if you want super class constructor to bexecuted,then create the supe`r class object
# x1=X()

##---------------------------------------------------------------------------------------------------------------------------------

# class X:
#     def __init__(self,a,b):
#         print("from constructor of x....")
#         self.x=a
#         self.y=b
#         print("x=",self.x)
#         print("y=",self.y)

# class Y(X):
#     def __init__(self):
#         print("from constructor of y ")


# y1=Y()
# y2=Y(10,20)
# x1=X()

### constructor overloading is happend -------------> Error 


# class A:
#     def __init__(self):
#         self.x=10
#         print("print constructor of class A ..")
# class B(A):
#     def __init__(self):
#         self.y=20
#         print("print constructor from class B ...")
# a1=A()
# print(a1.x)
# b1=B()
# print(b1.y)

# print(b1.x)   ## invalid bcz constructor overridden ,here x is got initiallied 

# ## using derived class object accessing both base and derived class NSV's for that the solutions is by using super() method

"""  super(): This statement is used to call super method or constructor through sub class method or constructor """
# class A:
#     def __init__(self):
#         print("Constructor from class A ")
# class B(A):
#     def __init__(self):
#         super().__init__()                   ## Executes super class constructor
#         print("Constructor from class B ")
# b1=B()

## Here first super class constructor execute followed by sub class constructor 
## Here first base class logic execute then derived class executes \

##-----------------------------------------------------------------------------------------------------

""" Accessing NSV's of super class constructor from sub class constructor """

# class A:
#     def __init__(self):
#         self.x=10
#         print("From constructor A ")
#         print(self)
# class B(A):
#     def __init__(self):
#         super().__init__()
#         self.y=20
#         print("From constructor B")
#         print(self)
# b1=B()
# print(b1)
# print(b1.x)   ## Now it can be accessed 
# print(b1.y)

###-----------------------------------------------------------------------------------------------------------

""" Sub class method calling  super class method """


# class A:
#     def m1(self):
#         self.x=400
#         print("x=",self.x)
# class B(A):
#     def m1(self):
#         super().m1()
#         self.y=500
#         print("y=",self.y)
# b1=B()
# b1.m1()

"""
---> for overriding and executing only userdefined logic, no need of super 
---> but to execute pre-defined logic and user-defined logic we need super()
---> for executing only base class logic(predefined logic) ----> no overriding (or) no super stmt required
---> for executing only drived class logic(user defined logic) ---> overriding is required
---> for executing both base and derived class logic ----> super() statement is required 

"""



"""
class GenericSevent:
    def m1(self):
        ............
        ............
        ............
class Myservelent:
    super().m1()
    ...............
    ...............     Here executing Pre-Defined +
    ...............     and also executing userdefinding logic

Ex:- 
"""

# class A:
#     def m1(self):
#         print("From m1.......!!!"")
# a1=A()
"""
Here 2 objects are created ---> class A object and object class object 

object class object has 2 method 

1.__hash__(self)
2.__str__(self)

object class object __hash__() method, which returns the value, this hash value converted into hexadecimal by 
another method called __str__() method

so python interpreter called __str__() method and __str__() method calls __hash__() method and takes hashvalue and
converted into hexadecimal value
"""
# class X:
#     def m1(self):
#         print("From m1.......!!!")
# x1=X()
# print(x1)                ## Returns indirect adress in hexadecimal value
# print(x1.__str__())      ## it also Returns indirect adress in hexadecimal value
# print(x1.__hash__())     ## it Returns indirect adress in decimal value

""" Overriding the __str__() method  """

class X:
    def __str__(self):   ## Overriding the __str__() method of object class
        return "Hello..!!"
    def m1(self):
        print("From m1....!!")

x1=X()
print(x1)
print(x1.__str__())

x2=X()
print(x2)
print(x2.__str__())
x1.m1()

## Here all the object displaying or returing the same value
## 


""" Displaying the different values of different ojects ---> By using parameterised constructor 
i.e, Displaying dynamic content
object1--->one value 
object2--->another value

"""

# class X:
#     def __init__(self,a):
#         self.p=a
#     def __str__(self):
#         return self.p
# x1=X()
# print(x1)
# print(x1.__str__())

# x2=X("Pranay")
# print(x2)
# print(x2.__str__())


"""
Q) What happens internally whenever a derived class object is created ....?

Ans:- First creates object of base class followed by derived class, all the objects are stored in the same memory
      location this adress is taken by python interpreter and using object class __hash__() method generates 
      hash value(In-direct adress) which is converted into hexgadecimal format by __str__() method. This indirect
      adress is stored with in derived class ref.variable

      Thats why using derived class ref.variable we can access all the properties of and derived class

"""


