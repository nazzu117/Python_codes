"""
Operators in Python:

1.Arithmetic operators
2.Comparision Operators
3.Logical operators
4.Assignment operators
5.Identity operators
6.Membership operators
7.Bitwise operators 
  """


""" 1.Arithmetic operator(+,-,/,*,%,//,**) """
# a=10 
# b=15
# print("Addition:", (a+b))
# print("substraction:",a-b)
# print("Multiplication:" ,a*b) 
# print("Division:",a/b)
# print("Exponent:",a**b)
# print("Flordivision:" ,a//b)
# print("Modulus:",a%b)

# print(10/3)
# print(10//3)
# print(10%3)

# x=10
# result =x+10
# print(result)

# x=10
# result =x-10
# print(result)

# x=10
# result =x/10
# print(result)

# x=10
# result =x*10
# print(result)

# x=10
# result =x**10
# print(result)

# x=10
# result =x//10
# print(result)

# x=10
# result =x%10
# print(result)

"""2.Relational or comparision operators(==,!=,<,>,>=,<=)   output is bulian only (T,F) Boolian
comparisional operators are used to compare the content of two objects: """
# r=50
# u=60
# print(r>u)
# print(r<u)
# print(r==u)
# print(r!=u)
# print(r>=u)
# print(u>=r)
# print(r<=u)
# print(u<=r)



"""3.Logical operators(and,or,not) """

# # A       B      A and B    A or B       not A
# # ----------------------------------------------
# # T       F        F       T       T 
# # F       T        F       T       F 
# # T       T        T       F       F       F
# # F       F        F       T       T       T
# q=12
# f=4
# print(q>f and f>q)
# print(q>f or f<q)
# print(f==q and f!=q)
# print(q>f or q<f)
# print(f<=q or f>=q)
# print(not(q>f))

""" 4.Assignment operators(=,+=,-=,*=,/=,//=,%=,**=) """

# x=5
# x+=3
# print(x)
# x-=3
# print(x)
# x*=3
# print(x)
# x/=3
# print(x)
# x**=3
# print(x)
# x//=3
# print(x)
# x%=3
# print(x)0/.,m nbv


"""Identity Operators: These operators are used to compare the addresses of 2 objects

Identity operators are:
1.is
2.is not   """

#ex:1

# a=10
# b=20
# print(a,id(a))
# print(b,id(b))

# print(a is b)
# print(a == b)
# print(a is not b)

#ex:2
# x=10
# y=10
# print(x,id(x))
# print(y,id(y))
# print(x is y)
# print(x == y)
# print(x is not y)
# #ex:3
# x=[10,20,30,40,50]
# y=[10,20,30,40,50]

# print(x,id(x))
# print(y,id(y))

# print(x is y)
# print(x == y)
# print(x is not y)

# x[1]=25
# print(x,id(x))

""" 6.Membership operators(in,not in) """
# a="nazeer"
# print("n"and "r"in a)
# # # 6.Ideantity operators(is, is not)
# a=(1,2,3)
# b=(1,2,3)
# print(a is b)
# print(id(a))


""" 7.Bitwise operator(bitwise And(&),bitwiseOr(|),bitwiseXor(^),Right shift(>>),Lift shift(<<))  """

# # A         B       A&B      A|B       A^B
# # ---------------------------------------
# # 0         1        0       1         1
# # 1         0        0       1         1
# # 1         1        1       1         0
# # 0         0        0       0         0

# a=20
# b=4
# print(a&b) #bitwise AND 
# print(bin(4))
# print(bin(23))

# print(~60)
# print(bin(43))
# print(a^b)

# #Left shift (<<)
# print(int(0b101110))
# #Right shift(>>)


# print(bin(280))

###########################################################################################
# princple=float(input("Enter the Amount: "))
# Time=int(input("Enter the time required(years): "))
# rate=float(input("Enter the rate: "))
# simple_intrest=(princple*Time*rate)/100         #The formula: (amount*time*rate)/100 is used to compute simple interest
# print("The intrest is :" ,simple_intrest)

# find entered year is leap year or not

# year=int(input("Enter year: "))
# if(year%4==0 and year%100!=0 or year%400==0):
#     print("YES IT's Leap year")
# else:
#     print("Wired....@@")

#Take the Temperature in Celcius and Covert it to Farenheit

# celcius=int(input("Enter the value: "))
# Fahrenheit=(celcius*1.8)+32
# print("Converted in Fahrenheit :",Fahrenheit)
