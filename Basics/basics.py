# print(1==1)
# print(5>7)
# print(5!=4)
# x=10
# x="code"
# x=51
# print(x)
# a="nazzu"
# b="bhai"
# print(a+" "+ b)


# import math
# print(math.pi)
# print(math.e)

"""
This is a Python Program to exchange the values of two numbers without using a temporary variable.
The program takes both the values from the user and swaps them without using temporary variable."""

a=int(input("Enter the value:"))
b=int(input("Enter the value:"))
a,b=b,a # swaping
print("a:",a)
print("b:",b)

""" OR """

# a=int(input("Enter value of first variable: "))
# b=int(input("Enter value of second variable: "))
# a=a+b
# b=a-b
# a=a-b
# print("a is:",a," b is:",b) 

""" Swaping three varibles """
x=int(input("Enter the x value: "))
y=int(input("Enter the y value: "))
z=int(input("Enter the z value: "))

print('The value of x is {}'.format(x))
print('The value of y is {}'.format(y))
print('The value of z is {}'.format(z))


temp_var=x
x=y
y=z
z=temp_var

print('The value of x is {}'.format(x))
print('The value of y is {}'.format(y))
print('The value of z is {}'.format(z))
