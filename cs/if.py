"""#set of statement that will excuted based upon condition
for loop excutes set of statements for collection object
 #if statement
 #if-else
 #if elif-else.

indentation is more imp--- block of statement will be written using indetation"""

""""
#Flow Control stmts:

-Every Python stmt executes only once from top to bottom
-In order to execute or not to execute set of stmts,we go for flow control stmts
 #or
- To execute set of stmts for repeated no of times or for multiple times ,we go for
  loops or control structures

 Flow Control stmts are divided into 2 parts
 1.Condition    : An Expression which returns a boolean value
 2.Block/Clause : set of stmts following the same space indentation

Various flow-control stmts or control strctures are:
    1.if
    2.if-else
    3.elif
    4.for loop
    5.while loop
    6.while-else
    7.break
    8.continue
    9.pass
Syntax for defining if-else:

if(condition):
    stmt1
    stmt2------------>Block1
    stmt3
    stmt4
else:
    stmt5
    stmt6------------>Block2
    stmt7
    stmt8

If the condition is True then stmts within if-block(Block1) will be executed
If the condition is False then the stmts within else-block(Block2) will be executed.

Nested Blocks: Blocks within a block

if(condition):
    stmt1
    stmt2
    stmt3
    if(condition):
        stmt4
        stmt5
        stmt6
    else:
        stmt7
        stmt8
        stmt9
    stmt10
    stmt11
    stmt12
else:
    stmt13
    stmt14

"""

# a=50
# if a>46:
#     print(a,"is grater than 44")

## Short hand if:-

# a,b=101,15
# if a>b: print("a is grater than b")

# score=int(input("Enter the Marks: "))
# if score>=35:
#     print("Hey you passed the examination: ")
#     print("Congratulation on your achivement @ @ @ @ ")
# if score<35:
#     print("Idiot your faild in the examination: ")
#     print("Go and pay the supplementary fee ")


# a,b=111,123
# print(a) if a>b else print("no not")

# a = 330
# b = 330
# print("A") if a > b else print("a equels to b") if a == b else print("B")


# score=int(input("Enter the Marks: "))

# if score >100 or score<0:
#     print("Score is invalid:::")
# elif score>=35:
#     print("Hey you passed the examination: ")
#     print("Congratulation on your achivement @ @ @ @ ")
# else:
#     print("Idiot your faild in the examination: ")
#     print("Go and pay the supplementary fee ")

# number=int(input("Enter the number: "))

# if number>0:
#     print(number,"is positive number")
# elif number==0:
#     print(number,"its zero",number)
# else:
#     print(number,"its a negative number: ")

# emp_id=int(input("enter emp id:"))
# if emp_id==100 or emp_id==101:
#    print("punch successfull come in Buddy")
# else:
#     print("punch unsuccessfull you ediot Get-out")
      

# a=200
# b=55
# if a>b:
#      print(" a is grater than b")
# elif a==b:
#      print("a is equals to than b")
# else:
#       print("b is grater than a")

# a = 200
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")
# else:
#   print("a is greater than b")

""" python programe to find given squre or not
Take values of length and breadth of a rectangle from user and check if it is square or not.
"""
# length=int(input("Enter Length: "))
# breadth=int(input("Enter Breadth: "))

# if length==breadth:
#     print("Yes,it's Squire [] ")
# else:
#     print("No it's not squre : ")

# s=45
# g=66
# r=900
# if s<g and s==g:
#     print("there is  no problem in the country ")
# elif r>g or g>s:
#     print("the nation not in trouble")


# a = 200
# b = 33
# c = 500
# if a > b and c > a:                            # And
#   print("Both conditions are True")

# a = 200
# b = 33
# c = 500
# if a > b or a > c:                             # Or
#   print("At least one of the conditions is True")


# x=100
# if x>99:
#     print("x is bigger thab 99")
#     if x>150:
#         print("its also bigger than 150")
#     else:
#         print("the grat thing is to be the nation")

# num=+0
# if num>0:
#     print("positive number")
# elif num==0:
#     print("its zero")                # if , elif , else 
# else:
#     print("negative number")

# numb=-20
# if numb>0:
#     if numb==0:
#         print("its zero")
#     else:    
#         print("positive number")       # Nested if
# else:
#     print("negative number")

# marks=int(input("Enter the marks: "))

# if marks>=70:
#     print("distnction")
# elif marks>=60:
#         print("you passed in the first class")
# elif marks>=35:
#         print("you just passed")
# else:
#     print("your faild man be ready for supplementry")


# sub1=int(input("Enter marks of the first subject: "))
# sub2=int(input("Enter marks of the second subject: "))
# sub3=int(input("Enter marks of the third subject: "))
# sub4=int(input("Enter marks of the fourth subject: "))
# sub5=int(input("Enter marks of the fifth subject: "))
# avg=(sub1+sub2+sub3+sub4+sub5)/5
# if(avg>=90):
#     print("Grade: A")
# elif(avg>=80 and avg<90):
#     print("Grade: B")
# elif(avg>=70 and avg<80):
#     print("Grade: C")
# elif(avg>=60 and avg<70):
#     print("Grade: D")
# else:
#     print("Grade: FAIL")
      



# your_score=int(input("Enter marks: "))
# pass_score=60
# if your_score>=pass_score:
#     print("congratulations")
#     print("hey man you cleared your semister")
#     pass
# else:
#     print("bad luck ,all the very best")        

# Take two int values from user and print greatest among them.


# first=input("Enter the first value: ")
# secound=input("Enter the Secound value: ")
# if first > secound:
#     print("First is garter than secound value")
# elif secound> First:
#     print ("Secound is grater than first value")
# else:
#     print("Both are equal Thank you ....*****")

"""A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
Ask user for quantity
Suppose, one unit(Quantity) will cost 100.
Judge and print total cost for user."""

# quantity=int(input("Enter required quantity: "))
# if quantity*100 >1000:
#     print("Cost is",(quantity*100)-(0.1*quantity*100))
# else:
#     print("Cost is :",quantity*100)
"""
A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
Ask user for their salary and year of service and print the net bonus amount.
"""
# salary=int(input("Enter the Drawing salary: "))

# experiance=int(input("Enter year of experiance with the company: "))

# if experiance>5:
#     print("You are elegible to get bonouse: ",0.05*salary)
# else:
#     print("No bonouse...!!!!")

"""Take input of age of 3 people by user and determine oldest and youngest among them."""
# first=int(input("Enter age of 1st person"))
# second=int(input("Enter age of 2nd person"))
# third=int(input("Enter age of 3rd person"))
# if first >= second and first >= third:
#   print("Oldest is",first)
# elif second >= first and second >= third:
#   print("Oldest is",second)
# elif third >= first and third >= second:
#   print("Oldest is",third)
# else:
#   print("All are equal")	

""" Leape Year """

# currentYear = int(input("Enter the year:"))
# month = int(input('Enter the month: '))
# if ((currentYear % 4) == 0 and (currentYear % 100) != 0 or (currentYear % 400) == 0):
#     print ('Leap Year')
#     if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
#         print ('There are 31 days in this month')
#     elif (month == 4 or month == 6 or month == 9 or month == 11):
#         print('There are 30 days in this month')
#     elif (month == 2):
#         print('There are 29 days in this month')
#     else:
#         print('Invalid month')
# elif ((currentYear % 4) != 0 or (currentYear % 100) != 0 or (currentYear % 400) != 0):
#     print ('Non Leap Year')
#     if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
#         print ('There are 31 days in this month')
#     elif (month == 4 or month == 6 or month == 9 or month == 11):
#         print('There are 30 days in this month')
#     elif (month == 2):
#         print('There are 28 days in this month')
#     else:
#         print('Invalid month')
# else:
#     print('Invalid Year')


""" Program to accept marks of 5 subjects and compute the total and percentage and
    also compute the class or grade awarded  """

# s1=90 ; s2=80 ;s3=70 ;s4=60 ; s5=50
# tot=s1+s2+s3+s4+s5
# per=(tot/500)*100
# print("TOTAL=",tot)
# print("PERCENTAGE=",per)

# if(s1>=40 and s2>=40 and s3>=40 and s4>=40 and s5>=40):
#     print("DIVISION :",end=" ")
#     if(per>=70):
#          print("FIRST CLASS WITH DISTINCTION")
#     elif(per>=60):
#          print("FIRST CLASS")
#     elif(per>=50):
#          print("SECOND CLASS")
#     elif(per>=40):
#          print("THIRD CLASS")
# else:
#     print("FAIL")


"""
Write a program to display "Hello" if a number entered by user is a multiple of five , 
otherwise print "Bye".
"""
# number=int(input("Enter the number: "))
# if number%5==0:
#   print("Hello")
# else:
#   print("Bye")

"""
Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria :
             Unit                                                     Price  
First 100 units                                               no charge
Next 100 units                                              Rs 5 per unit
After 200 units                                             Rs 10 per unit
(For example if input unit is 350 than total bill amount is Rs2000)
"""

# units=int(input("Enter the units of power consumed: "))
# amount=0
# if units<=100:
#   print("Good no charge for consumption...Amount=",amount)
# elif units>100 and units<=200:
#   print("Charges are :",amount=((units-100)*5))
# else:
#   print("Charges are :",amount=((units-200)*10))

"""Write a program to display the last digit of a number.
(hint : any number % 10 will return the last digit)
"""
num=int(input("Enter any number"))
print("Last digit of number is ",num%10)

num=int(input("Enter any number"))
print("Last digit of number is ",num%100)  ## for laste 2 numbers

num=int(input("Enter any number"))
print("Last digit of number is ",num%1000)  ## for laste 3 numbers. .........
"""
Write a program to check whether the last digit of a number( entered by user ) is 
divisible by 3 or not. """

# num=int(input("Enter the number: "))
# ide=num%10
# if ide%3==0:
#   print("Last digit of number is divisible by 3 ")
# else:
#      print("Last digit of number is not divisible by 3 ")

""" Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included """
# nl=[]
# for x in range(1500, 2701):
#     if (x%7==0) and (x%5==0):
#         nl.append(str(x))
# print (','.join(nl))