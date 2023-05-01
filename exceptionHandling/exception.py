"""Exceptionhandling ==> Handling the floow of errors.
There are 2 types of errors we have: 
                                    1.SyntaxErrors
                                    2.Run-Time Errors
1.Syntax-Errors: These Errors occures due to wrong syntaxes
Ex:- Missing colon,Wrong indentation...

           def function()                 # Syntax error bcz colon missing
           print("hello")                 # Wrong indntation
Python interpretor checks for syntax errors and then converts source coad to binary code(.pyc) and then this
converts bites code to machine code and execute.
If there are syntax errors then .pyc file won't be generated,
If .pyc file is not generated then the python file won't be executed """

# x,y=30,50
# if x>y                         # coloun missing 
# print("Hello",x)               # indetation error   These are syntax errors
# else:
#     print("Hello",y)


""" Run time errors """
# print "hello"              # SyntaxError: Missing parentheses in call to 'print'. Did you mean print("hello")?
# x=[10,20,30,40,50,60]
# print(x[9])              # IndexError:Index out of range
# print(x.remove(80))      # ValueError:list index out of range
# x=list("Apple","Mango")  # TypeError: list expected at most 1 argument, got 2
# print(y)                 # NameError: name 'y' is not defined
# y=(1,2,3,4,5,6,7,8)
# y[1]=66                  # TypeError: 'tuple' object does not support item assignment
# y.append(90)             # AttributeError: 'tuple' object has no attribute 'append'
# z={10,20,30,40,50,60}
# z.append(66)             # AttributeError: 'set' object has no attribute 'append'
# print("Python"+3)        # TypeError: can only concatenate str (not "int") to str

# a=10
# b=0
# print(a/b)               # ZeroDivisionError: division by zero

# f=open("text.txt","r")
# print(f)                 # FileNotFoundError: [Errno 2] No such file or directory: 'text.txt'
# In this way we have similer Errors 

# import os
# print(os.listdir("sample.txt"))  # NotADirectoryError: [WinError 267] The directory name is invalid: 'sample.txt'

# x=int(input("Enter the value of x: "))   # ValueError: invalid literal for int() with base 10: 'hello'
"""
--> When we get run-time error,programe execution terminated abnormaly
--> AbnormalTerminaton:- termination of the programe in the middle of the executon without executing upto last stmnt
--> for every runtime error,corresponding pre-defined python classes are avilable, 
    These classes are called as exception class 

--> Exceptions are the classes, which contain run time error representations
--> We can see all the pre-defined exceptons classes with in a module called as __builtins__

--> When ever we get run time error,run time error representation class object will be created automatically.
--> When ever this object is created,we say that exception is rised,we need to handle it with a code,otherwise abnormal termination

Two types of exceptions :-

---> Pre-defined exceptions[Built-in Exceptions]:- Rised automatically we need to handle it.
---> User-defined exceptions:- we need to rise and we need to handle
"""
# print(dir(__builtins__))

""" Exception-Handling:- The process of ideantifing rised exception object and handling it by assigning that exception 
                         to corrosponding run-time error representaion class is also known as 
                         Exception handling
we can implement exception handling in python using try and except block.
we need to follow indentation for both try and exception block.

1) try block syntax:
try:
    ............
    ............
    ............
    ............ for ideantifing rised exception 
    The statements which casus run time error are placed in try block
Ex:-

x=int(input("Enter x value: "))
y=int(input("Enter y value: "))
try:
    z=x/y
    print(z)
If the exception is rise in 1st statement of try block then controll will go to Except block without executing
remaining stmnts of try block.
2) Except block syntax:

except(Exception class name):
    ...........
    ...........
    ...........
    ...........
Except block assign the exception object to the corresponding run time error representation class 
we can also display user friendly error message in except block
except(ZeroDivisionError):  # Assigning exception object to corrosponding runtime error representation
    print("2nd no cannot be Zero")
"""
x=int(input("Enter x value: "))
y=int(input("Enter y value: "))
try:
    z=x/y               # stmnt which cause exception should kept in try block 
    print(z)
except(ZeroDivisionError):    # Exception object assigned to corrosponding
    print("2nd no cannot be Zero")  # We can display user friendly error message 



"""
try:- try block allows to try to write the statement when it critical statements/ critical statements 
allowed by try block

except:- except the the errors and runs the programe without giving ERROR'S

finally:- finally excute compulasury

"""
# a=23
# b="Python"

# try:
#     print(a/b)
# except Exception as e:
#     print(e)

# print("heloo world")


# lis=[23,45,90,"Nazeer",2+3j,66.98,56]

# for i in lis:
#     try:
#         if i%2==0:

#             print(i)
#     except Exception as e:
#         print("you moved to exception block",e)
#     else:
#         print("Got Error")


# while True:
# try:
#         user=int(input("Enter Number: "))
#         if user<0:
# raise ValueError("Please Enter Positive Number: ")
#         else:
#             print("user input %s", %user)
# except Exception as e:
#         print(e)    

