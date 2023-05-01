""" STATEMENTS:--
--> Single line statements:
# python statements are Instructions that a Python interpreter can execute are called statements. For example:"""
## a=1

""" Multiple line statements:-
In Python, the end of a statement is marked by a newline character.
But we can make a statement extend over multiple lines with the line continuation character "\". For example: 
"""

# a=1+2+3+4+\
# 5+6+7+8+\
# 9+10+11+12+13
# print(a)

# b=(1+2+3+4+
# 6+3+5+7+5+
# 22+33+4)
# print(b)

# c=["apple",
# "banana",
# "Mango"]
# print(c)


# """ We can also put multiple statements in a single line using semicolons, as follows:"""
# a=1;b=2;c=3
# print(a,b,c)


a=1
b=2
c=3
d=4
s="heloo"
k=33


""" Docstring:- Docstrings appear right after the definition of a function, class, or a module.
This separates docstrings from multiline comments using triple quotes.

The docstrings are associated with the object as their __doc__ attribute.
"""
def double(num):
    "Function to double the value"    # dock string[documentation strings]
    return 2*num
print(double.__doc__)