#1.
"""A function is a block of code which only runs when it is called.
You can pass data as parameters, into a function.A function can return data as a result."""
#2.                                    
"""
   Functions are a convenient way to divide your code into useful blocks, 
Allowing us to order our code, make it more readable, reuse it and save some time.
Also functions are a key way to define interfaces so programmers can share their code.
Furthermore, it avoids repetition and makes the code reusable. """
#3
"""
    Python provide us various inbuilt functions like range() or print(). Although, the user can create its functions,
which can be called user-defined functions."""
#4
"""
There are mainly two types of functions.
User-define functions - The user-defined functions are those define by the user to perform the specific task.
Built-in functions - The built-in functions are those functions that are pre-defined in Python.  """
#4
""" function can be called asmany time as we want[Multiple times..] """

# def display():
#    print("Display is the function and i just now called ")
   

# def myfun():
#    print("heloo alian good evening")``
# myfun()

# def myname():
#     print("heloo nazeer well come back")
# myname()

# def sum(a,b):
#    c=a+b
#    d=a-b
#    print(c)
#    print(d)
# sum(4,6)
# sum(56,44)
# sum(656,66)
# sum("hii","Ram")

# def hyd():
#     print("Hello Hyderabad...!!")
    
# def bng():
#     print("Hello Banglore...!!")
    
# def dei():
#     print("Hello Delhi...!!") 
# def kol():
#     print("Hello Kolkatta.!!")
#     bng()
# dei()
# kol()

## we can call function multiple times...@@@@@@
# def hello():
#     print("Happy Birth day...!!")
# def namaste():
#     print("Happy NewYear...!!")
#     hello()
# hello()
# hello()
# hello()
# hello()
########################################################################################################

"""GLOBAL AND LOCAL VARIABLES:- """
#  Global variables are the one that are defined and declared outside a function and we need to 
#  use them inside a function.

# def my_fun():
#    x=10
#    print("Value inside the function: ",x)
# x=20
# my_fun()
# print("Value outside the function: ",x)
########################################################################################################
# global variable
# a=10
# b=20
# def add():
#     c=a+b
#     print(c)
# add()
########################################################################################################
# a = 15
# # function to change a global value
# def change():
#     # increment value of a by 5
#     a = a + 5 
#     print(a)
  
# change()   ## UnboundLocalError: local variable 'a' referenced before assignment
##########################################################################################################
# a=12
# def change():
#     global a
#     a=a+10
#     print("Value inside =",a)
# print("Value outside =",a)
# change()
# print("Value outside =",a)
#############################################################################################################

# def add():
#     x=15
#     def change():
#         global x
#         x=20
#         print(x)
#     print("Before making change..",x)
#     print("Making changes...")
#     change()
#     print("After making change..",x)
# add()
# print("Value of x=",x)
###############################################################################################################


# # Python program to illustrate functions
# # can be passed as arguments to other functions
# def shout(text):
#     return text.upper()
  
# def whisper(text):
#     return text.lower()
  
# def greet(func):
#     # storing the function in a variable
#     greeting = func("""Hi, I am created by a function
#                     passed as an argument.""")
#     print (greeting) 
  
# greet(shout)
# greet(whisper)


"""If a variable with same name is defined inside the scope of function as well then it 
will print the value given inside the function only and not the global value."""

# def abc():
#    a="hai"
#    print(a)
# a="hello"  
# print(a)
# abc()
# print("--------------------------------------------------------------------------")
# def f():
# 	print(s)

# 	# This program will NOT show error
	# if we comment below line.
# 	s = "Me too."
# 	print(s)
# #Global scope
# s = "I love Geeksforgeeks"
# f()
# print(s)
# print("---------------------------------------------------------------------------------------")
# ## This function modifies the global variable 's'
# def f():
# 	global s
# 	print(s)
# 	s = "Look for Geeksforgeeks Python Section"
# 	print(s)

## Global Scope
# s = "Python is great!"        # it wont gets printed
# f()
# print(s)
# print("---------------------------------------------------------------------------------------")

# a = 1
# # Uses global because there is no local 'a'
# def f():
# 	print('Inside f() : ', a)
# # Variable 'a' is redefined as a local
# def g():
# 	a = 2
# 	print('Inside g() : ', a)
# # Uses global keyword to modify global 'a'
# def h():
# 	global a
# 	a = 3
# 	print('Inside h() : ', a)
# # Global scope
# print('global : ',a)
# f()
# print('global : ',a)
# g()
# print('global : ',a)
# h()
# print('global : ',a)

# a=25
# globals()['a']=25
# print(a)

###########################################################################################################

#def funn(fname):
#     print(fname+ " "+ "reddy")

# funn("Sumanth")
# funn("indrasena")
# funn("samarashimha")
# funn("narayana")

"""printing a docstring """

# def n(name):
#     """ HI IAM A DOCSTRING """  #docstring
#     print(name)
# print(n.__doc__)
# n("nazeer")
# ## look at docstring for inbult function print()
# print(print.__doc__)



# def dock():
    
#     """"This is to chinking the printing of 
#       dock string inside the function """
#     return None
# dock()
# print("Printing using __doc__: \n",dock.__doc__)

# print("Printing using help :",)
# help(dock)


# def my_function(arg1):
#     """
#     Summary line.
  
#     Extended description of function.
  
#     Parameters:
#     arg1 (int): Description of arg1
  
#     Returns:
#     int: Description of return value
#     """
  
#     return arg1
  
# print(my_function.__doc__)
##########################################################################################################
 
# print(dir(print))

""" From a function's perspective:
A parameter:- is the variable listed inside the parentheses in the function definition.
An argument:- is the value that is sent to the function when it is called."""

""" There are 5 ways to pass the arguments/parameters in the functions are :
1.positional/non default Arguments
2.Default Arguments
3.Keyword Arguments
4.Arberetry Arguments
5.Arberetry kryword Arguments

"Arguments can be of any datatype" 
----- 1. positional:-- values can be given based on position  
Parameters defined inside the function defination and Arguments passed at function call  
"""

# def details(username,password):
#    print("username:",username)
#    print("password:",password)
#    print('{} is the username and {}is the password'.format(username,password))
# # details("nazeer","nazeer123")
# details(input("Enter username:"),input("Enter password: "))
# # details("Rama","Rama123")

## when it comes to positional arguments parameters should equals to arguments 
 
# def names(fname,lname):
#     print("First name is:",fname)
#     print("Last name is:",lname)
#     print("Iam {} {}".format(fname,lname))
# names("Rama","Devi")
# names(input("Enter the first name:"),input("Enter the secound:"))

# def item(sweet):
#     print("My favourit sweet is ",sweet)
#     print("my favourite sweet is {}".format(sweet))
# item("Gulab Jamun")

#def my_function(fname, lname):
#  print(fname + " " + lname)           ## this give error

# my_function("Emil")    ## TypeError: my_function() missing 1 required positional argument: 'lname'



"""
---2.Default arguments----
providing a default value at the function delceration as parameter with some default values it's not necessary to specifie at the time of
functioncall,if not specified then the default value taken.
"""
# def my_function(country="norway"):
#     print("iam from " + country)

# my_function("india")
# my_function("USA")            ## if u r not provide any value it takes as norway.but here it will takes USA"
# my_function("Japan")
# my_function()            ## Default Argument 

# def details(username,password,country="INDIA"):
#    print("username:",username)
#    print("password:",password)
#    print("country:",country)
   
#    # print('{} is the username {} is the password and accesed from {}'.format(username,password,country))
# details("nazeer","nazeer123","USA")
# details("Rama","Rama123")

"""positiona arguments and default arguments   """
# def greet(name, msg="Good morning!"):
#     print("Hello", name + ',' + msg)

# greet("Kate")
# greet("Bruce", "How do you do?")
""" EX:- non-default and default arguments """

# def person(name="Nazeer",city):   ## SyntaxError: non-default argument follows default argument
#    print("my name is ",name)
#    print("Iam from ",city)
#    print("Iam Mr {} and i'm from{} ".format(name,city))
# person("pune")
# person("Nazeer")

### Note:- after default argument we cannot specify non-default argument


"""-----3. keyword arguments
You can also send arguments with the key = value syntax.
This way the order of the arguments does not matter.

"""

# def details(username,country="INDIA",password="nazeer123"):
#    print("username:",username)
#    print("password:",password)
#    print('{} is the username {} is the password and accesed from {}'.format(username,password,country))
# details(username="nazeer",password="nazeer123",country="USA")
# details(username="Rama",password="Rama123")

# def demo(name, age):
#    print(name + " is " + age + " years old")
# demo(name = "Steve", age = "35")     # 2 keyword arguments (In order)
# demo(age = "20", name = "Mohan")     # 2 keyword arguments (Not in order)
# demo("Bucky", age = "40")             # 1 positional and 1 keyword argument

## Keyword and nonkeyword argument's
""" Keyword Arguments:- during function call with parameter name passing value """
""" Non-keyword arguments:- during function call without parameter name passing value """

# def emp(eid,ename,salary,design,city="Hyderabad"):
#    print(eid,ename,salary,design,city)
#    print("Employee is {} Mr {} whose salary {} and he is working as {} in {}".format(eid,ename,salary,design,city))
# emp(1001,"Nazeer",75000,"Softwear Developer")  ## non keyword arguments..
# emp(salary=85000,design="Softwear Engineer",eid=1110,ename="Nazzu")
# emp("Miller",1199,"Engineer",88800)  ## valid but not recommand bcz loock at the order
# emp(1001,"Miller",75000,design="SE",city="Banglore") ## non-keyword and keyword
# ##emp(design="SE",city="Banglore",1001,"Miller",75000) 
# ## Note:- After keyword argument cannot specifie non keyword argument 



"""---4.Arberatery arguments or variable length arguments ----  *args
Python allows us to have the arbitrary number of arguments. 
This is especially useful when we are not sure in the advance that how many arguments, 
the function would require.
We define the arbitrary arguments while defining a function using the asterisk (*) sign. which is placed 
before the variable name that holdes multiple values which is of tuple type """

# def pepl(*names):
#    for i in pepl
#    print("heloo",names)
# pepl("nazeer","haseena","ussain","rama")

# def fruits(*names):
#    print(names)

#    for fruits in names:
#       print(names)
# fruits("Apple","Mango","Banana","Cherry","B-Berry")


# def trans(*a,name="Ramadevi"):
#     print(sum(a))
#     print('{} is debited from {} account.'.format(sum(a),name) )
# trans(123.4,5655.9000,5678.99,5454.4545)
# trans(6576.55,5565,554,900,444.224,6645)


# def greet(*names):
#     for name in names:
#         print("hello",name)
# greet("Nazzu","Rama","kamarthi","Nazeer")

# def names(first,*secound,):
#     print("first name "+first)
#     for names in secound:
#         print(names)
#     print("Last name "+secound[4])
# names("Ramesh","Suresh","Mahesh","Pavan","Suman","khelan")

# def display(name,*marks):
#    print(name)
#    print(marks)
#    x=1
#    for p in marks:
#       print(p)
#       print("Subject",x,":",p)
#       x=x+1
# display("Blake",90,80,98,89)

# def three(x,y,*z):
#    print(x,type(x))
#    print(y,type(y))
#    print(z,type(z))
# three(10,20,30)
# print("\n")
# three(10,20,30,40,50)
# print("\n")
# three(10,20)     ## () <class 'tuple'>
# print("\n")
# three(10,20,"Hello")
# print("\n")
# three(10,"Hi","Hello")
# print("\n")
# three(10,"Hi","Hello","Namaste")
# print("\n")
# three(10,20,30,[50,80,90])


# def note(*p,q,s):
#    print(p,type(p))
#    print(q,type(q))
#    print(s,type(s))

# note(12,90,15,20,65)  ## TypeError: note() missing 2 required keyword-only arguments: 
#'q' and 's' cz p will take all aruguments as tupel ,here q,s are missing
""" NOTE:- we can take arbitary argument as the first argument provided that we use default or ketwordargument """
""" TO OVERCOME ABOVE PROBLEM ASSIGN VALUES TO Q AND S USING KEYWORD ARGUMENTS OR DEFAULT ARGUMENTS """

# def note(*p,q,s=111):
#    print(q,type(q))
#    print(s,type(s))
#    print(p,type(p))

# note(12,90,15,20,q=65)
# note(12,90,15,s=20,q=65)
# ##note(12,90,s=15,20,q=65)   ## SyntaxError: positional argument follows keyword argument

""" 5.Arberatery keyword arguments """
""" If you do not know how many keyword arguments that will be passed into your function, 
add two asterisk: ** before the parameter name in the function definition.

 """

# def myFun(arg1, **kwargs):  
#     for key, value in kwargs.items(): 
#         print ("%s == %s" %(key, value)) 
  
# # Driver code 
# myFun("Hi", first ='Geeks', mid ='for', last='Geeks')

# def year_trans(**a):
   #  print(a)
   #  print(a.values())
   #  print(a.keys())
   #  print(sum(a.values()))
#     total=0
#     for i in a:
#         total=total+(a[i])
#     print(total)

# year_trans(jan=55454,feb=11010,march=332322,apr=98000,jun=223233,jul=545454)


##     Using *args and **kwargs to call a function

# def myFun(arg1, arg2, arg3): 
#     print("arg1:", arg1) 
#     print("arg2:", arg2) 
#     print("arg3:", arg3) 
      
# # Now we can use *args or **kwargs to 
# # pass arguments to this function :  
# args = ("Geeks", "for", "Geeks") 
# myFun(*args) 
  
# kwargs = {"arg1" : "Geeks", "arg2" : "for", "arg3" : "Geeks"} 
# myFun(**kwargs) 


""" return statement """
# |x| = x if x is positive, and |x| = −x if x is negative, and |0| = 0.

# def absvlv(num):
#     if num>0:
#         return num
#     else:
#         return -num

# print(absvlv(int(input("Enter the number u want to check:"))))

# def abs_value(num):
#     if num>=0:
#         return num
#     else:
#         return -num
# print(abs_value(int(input("Enter value to check abs value:"))))
# print(abs_value(-9))
# print(abs_value(9))
# print(abs_value(-56))


# def add(a, b):
#     result = a + b
#     return result

# print(add(2, 2))



# def my_function(x):
#     return 5 * x

# print(my_function(5))
# print(my_function(7))
# print(my_function(9))
# print(my_function(11))



# def avg(n1,n2,n3):
#     return(n1+n2+n3)/3.0
# print("hello")
# result1=avg(10,20,30)
# result2=avg(3,4,2)
# result3=avg(7.4,3.9,5.7)

# print(result1)
# print(result2)
# print(result3)

# def get_even(numbers):
#    return [num for num in numbers if not num % 2]
# print(get_even([1, 2, 3, 4, 5, 6]))


# def find(the_string, search_this):
#    if search_this in the_string:
#       a = the_string.find(search_this)
#       # returns the unexpected 
#       return (search_this, "found at", str(a))
#    else:
#       # the correct output I am looking for
#       return (search_this + " was not found at " + the_string)

# print(find("qweabc","abc"))
# print(find("abcd", "xyz"))

# def print_greeting():
#     print("Hell Good Evening")
# print_greeting()
# def return_greeting():
#     return 5
# return_greeting() 

# def foo():
#     print("Hello from within foo")
#     return 2
# def bar():
#     return 10*foo()
# foo()
# bar()


""" Recursion: Recursion means the function calling it self """

#Advantages of Recursion:-

"""Recursive functions make the code look clean and elegant.
A complex task can be broken down into simpler sub-problems using recursion.
Sequence generation is easier with recursion than using some nested iteration. """

#Disadvantages of Recursion:-

"""
---> Sometimes the logic behind recursion is hard to follow through.
---> A lot of memory and time is taken through recursive calls which makes it expensive for use
---> Recursive calls are expensive (inefficient) as they take up a lot of memory and time.
---> Recursive functions are hard to debug."""


# factorial using recursion

# def factorial(a):
#     if a==0:
#         return 1
#     else:
#         return a*factorial(a-1)    #n*(n-1)(n-2)....
# print(factorial(6))


# import sys 
# sys.setrecursionlimit(2000)      ## increase recursion limit as required as follows
# print(sys.getrecursionlimit())   ## defaultli it gives 1000






# def hel(x):
#   print("Namaste....@@@")
#   print("Good Morning....@@@")
# def nam():
#   print("Super Women...@@@")
# hel(nam())