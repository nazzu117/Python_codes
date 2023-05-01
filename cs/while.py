# Loopings-- Excuting certain set of statements multiple number of times...
# while loop in python is used to iterate over a block of code as long as condition is true
# we generally use the loop when we dont know the no of times to itterate beforehand.
# Whole loop

# Syntax for defining while loop
"""
initialization
while(condition):
    stmt1
    stmt2
    stmt3
    stmt4
    increment/decrement  """

## All the stmts within the while loop should follow the indentation
## The stmts within the while loop will be executed untill the condition becomes False
## Once the condition becomes False then control comes out of while loop and executes the other stmts

# #program to print No's from 1 to 10
# x=1
# while(x<=10):
#     print(x)
#     x=x+1
# print("end")

#Program to print a msg for multiple times
# x=1
# while(x<=10):
#     print("Good Morning!!!")
#     x=x+1
# print("end")

#Program to find the sum of first 'n' numbers
# n=int(input("Enter value of n:"))
# sum=0
# x=1
# while(x<=n):
#     sum=sum+x
#     x=x+1
# print("sum=",sum)

#Infinite while loop

# while(True):
#     print("hello")

# a=70
# while a>50:
#     print(a,"is grater than 50")
#     a-=5

# s=100
# while s>20:
#     print("heloo Nazzu")
#     s-=5

# i=0
# while i<6:
#     print(i)
#     i+=1

# b=123
# while b<198:
#     print(b)
#     b+=10

#while-else:when while condition becomes false then ctrl goes to else block

# x=1
# while(x<=10):
#     print("Hello")
#     x=x+1
# else:
#     print("Good Morning")
# print("end")

#continue:It skips the current iteration and continues with the next iteration

# x=0
# while(x<10):
#     x=x+1
#     if(x==5):
#         continue
#         print("hi")
#     print(x,"hello")
# print("end")


# w=100
# while w>10:
#     w-=5
#     if w==35:
#         continue
#     print(w)
# else:
#     print("w is no /n longer exist")

#break: If break stmt is used in a loop then ctrl comes out of that loop and stmts after
#       break are not executed

# x=1
# while(True):
#     print("hello")
#     if(x==5):
#         break
#         print("hi")
#     x=x+1
# print("End")

# k=1
# while k<9:
#     k+=1
#     if k==3:
#         break
#     print(k)
 
#while-else and break

# x=1
# while(True):
#     print("hello")
#     if(x==5):
#         break
#         print("hi")
#     x=x+1
# else:
#     print("Good Morning!!!")
# print("end")

#Note: Stmts after break are not executed even the else block


#Break and continue:
# while(True):
#     username=input("Enter the username:")
#     if(username!="vijay"):
#         continue
#     password=input("Hello....Vijay!!!...please enter ur Password:")
#     if(password=="python"):
#         break
# print("LOGIN SUCCESSFULL!!!")
    
#pass stmt:

# x=10
# y=5

# if(x>y):
#     pass
# else:
#     pass


#Nested while loop.....

# i=int(input("Enter a number"))
# while i<10:
#     while i==5:
#         print(i)
#         i=i+1

# i=0
# j=5
# while i<6:
#     while j>0:
#         print(i,j)    # Nested while loop which contains whilw loop inside a while...
#         i+=1
#         j-=1
        
# a=3
# while a<5:
#     print("hii")
#     a+=1

# i=0
# j=2
# while i<5:
#     while j>0:
#         print(i,j)
#         i+=1
        # j-=1

# i=1
# sum=0
# while i<=10:
#     if i%2==0:
#         sum=sum+i
#     i+=1
# print(sum)
        
# val=int(input("Enter Multiple of 7: "))
# while val%7!=0:
#     val = int(input("Enter Multiple of 7: "))
# else:
#     print("id is multiple of 7",val)

""" print a multiplication table"""
# number=int(input("Enter the number:"))
# count=1
# while count>=10:
#     product=number*count
#     print(number,"x",count,"=",product)
#     count+=1

""" print a multiplication table in reverse like 10x10=100....."""

# number=int(input("Enter the number:"))
# count=10
# while count>=1:
#     product=number*count
#     print(number,"x",count,"=",product)
#     count-=1

""" Python Program to Reverse a Given Numbe """
# n=int(input("Enter the number:"))
# rev=0
# while (n>0):
#         dig=n%10
#         rev=rev*10+dig
#         n=n//10
# print("Reverse number :",rev)

""" A simple ATM transation """
# count=0
# while count<=2:
#     pin = int(input("Enter Pin:- "))
# #     acc_type=input("Enter Account Type:-")
# #     amount = int(input("Enter the amount:-"))
#     if pin==1234:
#         acc_type=input("Enter Account Type:-")
#         if acc_type=="saving":
#             amount = int(input("Enter the amount:-"))
#             print(amount,"is being debited from your account!")
#             break
#         else:
#             print("Account Type Doesnot Match!!")
#             count=count+1
#             continue
#     else:
#         print("Incorrect PIN!Try Again")
#         count=count+1
# else:
#     if count==4:
#         print("Transaction Successful!")
#     else:
#         print("Tried More time! Account Blocked")



"""
#While loop Assignments:

1)Program to reverse a Given no
  x=123
  The reversed no is-------->321

2)Program to compute the digital sum of a number
  x=354
  The digital sum=3+5+4 =12

3)Program to check whether a given no is a armstrong no or not?
  x=153
  If the sum of the cubes of the digits of the number is equal to the given no then
  it is an armstrong number.

4)Program to check whether a given no is a palindrome or not?
 x=151 is a pallindeome
 If we reverse a no ,we need to get the same no

 ii)Program to check wheter a given string is a palindrome or not
 x="madam"
 x="dad"
 x="mom"
 x="racecar"
 x="malayalam"

5)Program to check whether a given no is a unique no or not
  n=1089  is a unique no
  Take any no(n) and multiply with highest digit(9),we get a result and reverse the result
                                             we need to get the same no then it is a unique no
         n=1089*9------->9801------->reverse it------>1089 if we get the same no then it is
                                                      a unique no
         

6)Program to find the factorial of a given no
  n=5
  The Factorial is 5*4*3*2*1=120

7)Program to check whether a given no is a strong no or not
  n=145 is a strong no
    1!+4!+5!
    1+24+120
   =145 equal to the given no
   If the sum of the factorials of the digits of a number is equal to the given no
   then it is a strong no

8)Program to check whether a given no is a perfect no or not?
   n=6 is a perfect no
   The factors of  6 is--->3+2+1==6
   IF the sum of the factors of a number is equal to the given no then it is a perfect no

9)Program to check whether a given no is a prime no or not?

10)Program to check whether a given no is a Even no or not.
  

"""














   































 












 
 
