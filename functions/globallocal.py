# a=10
# def hi():
#     b=20
#     print("Local:",b)
# hi()
# print("Global:",a)

# x="awesome"

# def my_function():
#     x="fantstic"
#     print("python is"+x)
# my_function()
# print("python is"+x)

# x="awesome"

# def my_function():
#     global x
#     print("python is "+x)
# my_function()


# a=30
# b=10
# c=33
# def add(a,b,c):
#     print("inside a+b:",a+b)
#     print("inside b+c:",b+c)
#     print("inside c+a:",c+a)

# add(40,45,50)
# print("outside a:",a)
# print("outside b:",b)
# print("outside c:",c)

# x=500             # here x is the global key so that u can use in both globally and locally
# def funct():
#     print(x)
# funct()

# def lol():          # using global keyword inside the function belongs to global scope:-
#     global x
#     x=400
#     # print(x)
# lol()
# print(x)

# x=600
# def lol():          
#     global x
#     x=400
#     print(x)
# lol()
# print(x)

#a=33
# def kol(b):
#     global a    # if u want to make variable global it shouldnt declared as parameter/argument
#     a=10
#     print(a+b)
# print(a)
# kol(3)
# print(a)


# n=10
# def fun1():
#     print(n)
# def fun2():
#     n=20
#     print(n)
#     fun1()
# fun2()

# a=33
# def kol():
#     global a    # if u want to make variable global it shouldn't declared as parameter/argument
#     global b
#     b=44
#     a=55
#     print(a+b)
#     print("in:",a)
#     print("in:",b)
# print(a)
# kol()
# print("out",a)
# print("out",b)

# a=10
# print(id(a))
# def something():
#     a=9
#     x=globals()['a']
#     print(id(a))
#     print("in",a)
# something()

# a=10
# print(id(a))
# def something():
#     a=9
#     x=globals()['a']
#     print(id(a))
#     print("in",a)
# something()

# print(bin(29))
#
# e="butter"
# def f(a):
#     print(a)+e
# f("bitter")

# x=1
# def cd():
#     global x
#     x=x+1
# cd()
# print(x)