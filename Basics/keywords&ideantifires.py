# keywords are the reserved words in python 
# We cannot use a keyword as a variable name, function name or any other identifier.
# They are used to define the syntax and structure of the Python language.

# In Python, keywords are case sensitive.
# Except True , False , None ,all are in lowercase 

"""There are 33 keywords in Python 3.7. This number can vary slightly over the course of time.
All the keywords except 'True', 'False' & 'None' are in lowercase and they must be written as they are. 
The list of all the keywords is given below.

False	await	else	import	  pass
None	break	except	in	      raise
True	class	finally	is     	  return
and	   continue	for	    lambda	  try
as	    def	    from	nonlocal  while
assert 	del	    global	not	      with
async	elif	if	    or	      yield   

"""
# The above keywords may get altered in different versions of Python. 
# Some extra might get added or some might be removed. 
# You can always get the list of keywords in your current version by typing the following in the prompt.

# import keyword
# print(keyword.kwlist)

# import keyword
# for i in keyword.kwlist:
#     print(i)
#     print(len(i))

# print((keyword.kwlist))
# print(len(keyword.kwlist))

## Expected output= As on date 28-04-2021
"""
['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 
'await', 'break', 'class', 'continue', 'def', 'del',   
'elif', 'else', 'except', 'finally', 'for', 'from', 
'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 
'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']  """


## Some examples 

# print(1==1)
# print(2>3)
# print(True or False)
# print(True and False)

### True and False in python is same as 1 and 0. This can be justified with the following example:

# print(True==1)    # True
# print(False==0)   # True
# print(True==0)    # False
# print(False==1)   # False

## None is a special constant in Python that represents the absence of a value or a null value.
## We must take special care that None does not imply 
# False, 0 or any empty list, dictionary, string etc. For example:

# print(None==0)   #False
# print(None==1)   #False
# x=None
# y=None
# print(x==y)      #True
"""
# assert
At this point we can note that,
 syntax

assert condition, message"""
#a=4
#assert a>5   # a value smaller than 5 that will leads to  AssertionError
#############################################################################################################
""" Identifiers: 
The identifier is a name used to identify a variable, function, 
class, module, etc. The identifier is a combination of character digits and 
underscore. The identifier should start with a character or Underscore then use digit. 
The characters are A-Z or a-z,a UnderScore ( _ ) and digit (0-9). 
we should not use special characters ( #, @, $, %, ! ) in identifiers.

Examples of valid identifiers:

var1
_var1
_1_var
var_1

Examples of invalid identifiers

!var1
1var
1_var
var#1
"""

## Multi-line statement
"""In Python, the end of a statement is marked by a newline character. 
But we can make a statement extend over multiple lines with the line continuation character (\). For example: """

a = 1 + 2 + 3 + \
    4 + 5 + 6 + \
    7 + 8 + 9
"""This is an explicit line continuation. In Python, line continuation is 
implied inside parentheses ( ), brackets [ ], and braces { }. For instance, 
we can implement the above multi-line statement as:"""

a = (1 + 2 + 3 +
    4 + 5 + 6 +
    7 + 8 + 9)
print(a)
"""Here, the surrounding parentheses ( ) do the line continuation implicitly. 
Same is the case with [ ] and { }. For example: """

colors = ['red',
          'blue',
          'green']

print(colors)
"""We can also put multiple statements in a single line using semicolons, as follows: """

a = 1; b = 2; c = 3
print(a)
print(b)
print(c)
print(a,b,c)
