## functions are defined in python by def keyword
## function is a block of coad which perform a specific task 
## functions are not automatically excuted,to excute functions we need to make a function call
## function are excuted on demand by making function call
## we can make n no of function calles [Lazy evolution]
## all the statements within the function should follow the same space indentation
## in python we have two types of function inbult functions[print,id,type,etc...] and user defined functions
## even dock string should follow the indentation 
## main advantage of functions is code reusability 

""" function properties """

""" 1. Functions are called multiple times """

# def hello():
#     print("Happy Birth day...!!")
# def namaste():
#     print("Happy NewYear...!!")
#     hello()
# hello()
# hello()
# hello()
# namaste()

""" 2.the order in wich the functions are defined,need not be same while calling   """
def maths():
    print("Mathematics are easy to learn..!!!")
def english():
    print("English is good subject...!!!")
def science():
    print("I love to learn science...!!!")
def chemistry():
    print("Chemistry is little difcult to me...!!!")
chemistry()
science()
english()
maths()

""" a function can call another function """

# def hyd():
#     print("Hello Hyderabad...!!")
#     #hyd()     This cause unlimited recursion bcz it's the same function calling it self for unlimited times
# def bng():
#     print("Hello Banglore...!!")
#     hyd()
# def dei():
#     print("Hello Delhi...!!") 
# def kol():
#     print("Hello Kolkatta.!!")
#     bng()
# dei()
# kol()

"""A function can't call before it defined """

# display()    ## both not valid 
# show()
# def display():
#     print("Displaying something...!!! ")
# def show():
#     print("Showing something here.....!!!")

""" function with return type """
# def myfun():
#     x=10
#     y=20
#     z=x**y
#     return z
# a=myfun()
# print(a)

"""#2 function with arguments with out returntype  """

# def add(x,y):
#     z=x+y
#     print("z=",z)
# add(12,20)
# print(sum(12,30)) ## Here we get None bcz the function won't return nothing

## Note:- function are also used to assignments
""" function with arguments and with return type """

# def display(x,y):
#     z1=x+y
    
#     return z1
# display(30,50)  ## Whatever the function return is stored by function call 
# print(display(10,20))
# s=display(1000,5000)
# print(s)

"""QUESTION:- Can a function return multiple values """
# def avg(a,b,c):
#     tot=a+b+c
#     avg1=tot/3
#     return tot,avg1
# x=avg(12,10,34)
# print(x,type(x))
# print("Total=",x[0])
# print("Avg=",x[1])
# print(x[:])
# ## OR
# p,q=avg(12,10,34)
# print("Total=",p)
# print("Avg=",q)

""" the function without arguments and with return function """

# def show():
#     x=10;y=20
#     z=x+y
#     return z
# a=show()
# print(a)

# def display():
#     print("Good Morning...!!")
#     ##show()        we cannot call function before they defined
#     def show():
#         print("Good Evening..!!")
#     show()
# display()
# ##show()   NameError: name 'show' is not defined

""" #1.call-by-value
    #2.call-by-referance """
    # call by value:- is calling a function by providing some values
    # call by referance is calling by providing some referances

# def disp(x,y):
#     z=x+y
#     print(z)
# disp(12,33)   ## call-by-value

# def show(x,y):
#     z=x+y
#     print(z)
# a=10
# b=33
# show(a,b)

""" Local and Global Variables """
## Local Varialbe : are defined inside function and are accessed only with in the function
## Global Variable : 

# x=10                   ## Global Variable
# def compute():
#     y=20               ## Local Variable
#     print("x=",x)
#     print("y=",y)
# # ###compute()
# def show():
#     print("x=",x)
#     ##print("y=",y)
# compute()
# show()

""" Local and global variables with same name"""

# x=10
# def hi():
#     x=100
#     print(x)   ## Always given preferance local variable first
# def hllo():
#     print(x)
# hi()
# hllo()

""" Modifing the global variable within the function """
# x=200
# def disp():
#     global x  ## forward direction sats that the global variable value can be modified with later statements
#     x=12
#     print(x)
# def show():
#     print(x)
# disp()
# show()








