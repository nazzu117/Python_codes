""" Lambda function or anonymous function:-
1. A function without any name is called lambda function 
2. Syntax for lambda function :- lambda Arguments : expression
3. if the function dosn't have any name then how will you call that function

   Assign that function to a variable and that variable behaves like the function name 
   and using that variable name we can call that function
"""
"""
In which situation we go for lambda function 
Ans:- when providing one function as parameter to another function,then we go for lambda() function

We use lambda functions when we require a nameless function for a short period of time.

def f1():
    ----------
    ----------
    ----------
    ----------
def f2():
    ----------
    ----------
    ----------
    ----------
f1(f2())

Insteed of all these we go for lambda function

"""
## Lambda function to square a function 

# f1=lambda x : x**2   ## Here f1 behave like a function name
# print(f1(10))
# print(f1(12))
# print(f1(100))

## The same task using normal function

# def mul(x):
#     z=x**2
#     return z
# print(mul(100000))

## NOTE:- lambda function can have any no of arguments but only one expression 

""" Add 10 to argument a, and return the result: """
# f2=lambda  x:x+10 
# print(f2(11))

# p=lambda x,y=20:x*y    ##Here x is non-default and y is default arguments
# print(p(12))
# print(p(12,10))        ## Non default arguments
# print(p(x=120,y=200))  ## Keyword arguments


"""Multiply argument a with argument b and return the result: """

# x = lambda a, b : a * b
# print(x(5, 6))

""" Lambda function to find a larger number amoung two """
# larger=lambda a,b: a if a>b else b
# print(larger(123,444))

## if we want to sort a list as alphabetical order see below example
# a=["Ramesh","suresh","naresh","mahesh","somesh","arunash","chendresh","bhanesh"]
# a.sort()
# print(a)

""" Same using lambda sorted accrding length of names"""
# a.sort(key=lambda x:len(x))
# print(a)


"""Summarize argument a, b, and c and return the result: """

# x = lambda a, b, c : a + b + c
# print(x(5, 6, 2))
"""
 Why Use Lambda Functions?
Say you have a function definition that takes one argument, 
and that argument will be multiplied with an unknown number: """

# def myfunc(n):
#   return lambda a : a * n
##############################################################################################################
# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(2)

# print(mydoubler(11))
##############################################################################################
## initialize variable 
# a,b,c=10,20,45
# # define lambda function
# expression=lambda a,b,c:b+c-c*a
# # print result
# print("Expression result is :",expression(a,b,c))
# print("Expression result is :",expression(a=5,b=45,c=30))












































