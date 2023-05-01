"""1.   Variables are containers for storing data values.

1.1  Unlike other programming languages, Python has no command for declaring a variable.
1.2  A variable is created the moment you first assign a value to it.
1.3 variables in python is case-sencitive
1.4 Never use special symbols like !, @, #, $, %, etc...
1.5 Don't start a variable name with a digit
1.6 You can think variable as a bag to store books in it and those books can be replaced at any time.
"""
## Example 1: Declaring and assigning value to a variable

# website = "Apple.com"
# print(website)

##Example2: changing the value of a variable
# website="Apple.com"
# print(website)
# ##changing the varable name;
# website="nasa.com"
# print(website)
# print(id(website))

# b=33
# e=33
# d=22 
# a=22
# f=22
# print(id(b))
# print(id(b))
# print(id(e))
# print(id(d))
# print(id(a))
# print(id(f))


# #Example 3:Assining Multiple values to variables
# x,y,z=["apple","Banana","califlower"]
# print(x,y,z)
# print(x)
# print(y)
# print(z)

# a,b,c=1,3.4,"heloo"
# print(a)
# print(b)
# print(c)
# print(a,b,c)

""" Swapig two variales """
# a=10
# b=20
# print(a)
# print(b)
# a,b=b,a
# print(a)
# print(b)

# a=b=c="kakinada kaja"
# print(a)
# print(b)
# print(c)
# print("a=",a,"b=",b,"c=",c)

# r="awesome"
# print("python is one of "+r+ " " +"language")    #or

# m="nazzu"
# g="is fantastic guy in the world and the nation is the mandatery of the same time"
# print(m+" "+g)

# e="Mathematics"
# d="is a subject"
# f=e+d
# print(f)

### calculate Body Mass Idex
# height=float(input("Enter height the person in Meters: "))
# weight=float(input("Enter height the person in kgs:"))
# a=weight/height**2
# if a>25 and a<=29.5:
#     print("Over weight",a)
# elif a<=25:
#     print("Normal weight",a)
# elif a<=18.5:
#     print("Less weight")
# elif a>30:
#     print("Obesity",a)
# else:
#     print("values not found")



""" Constants :-constants are variables whose value cannot changed later.
It is helpful to think of constants as containers that hold information which cannot be changed later
 CAPITAL letters use to declare the constants
1.Declaring and asssing a variable to constants:-

"""
# import constant
# print(constant.PI)
# print(constant.GRAVITY)

""" Literals: literals are raw data given to the variable or to constant there are few types of literals
1.numaric literals
2.String literals
3.boolian literals
4.Special literals like None
5.literals collection
"""
#1 numerac literals: Numeric Literals are immutable (unchangeable). Numeric literals can belong to 3 different numerical types: Integer, Float, and Complex.

# a = 0b1010 #Binary Literals
# b = 100 #Decimal Literal 
# c = 0o310 #Octal Literal
# d = 0x12c #Hexadecimal Literal

# #Float Literal
# float_1 = 10.5 
# float_2 = 1.5e2

# #Complex Literal 
# x = 3.14j

# print(a, b, c, d)
# print(float_1, float_2)
# print(x, x.imag, x.real)


# String literals
# A string literal is a sequence of characters surrounded by quotes. We can use both single, double, or triple quotes for a string. And, a character literal is a single character surrounded by single or double quotes.

# Example : How to use string literals in Python?
# strings = "This is Python"
# char = "C"
# multiline_str = """This is a multiline string with more than one line code."""
# unicode = u"\u00dcnic\u00f6de"
# raw_str = r"raw \n string"

# print(strings)
# print(char)
# print(multiline_str)
# print(unicode)
# print(raw_str)

#4.Boolean literals
#A Boolean literal can have any of the two values: True or False.

#Example: How to use boolean literals in Python?
# x = (1 == True)
# y = (1 == False)
# a = True + 4
# b = False + 10

# print("x is", x)
# print("y is", y)
# print("a:", a)
# print("b:", b)
