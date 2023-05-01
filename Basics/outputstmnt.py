## OUTPUT Statements:--
x=10
y=20
z=30
print(x)
print(y)
print(x,y)
print(x,y,sep=" ")
print(x,y,sep=",")
print(x,y,sep="@")
print(x,y,sep="$")
print(x,y,sep="\t")  ## 4 spaces
print(x,y,sep=":")
print(x,y,sep="-->")
print(x,y,sep="\n")
print(x,y,sep=" ")
print(x,y,z,sep=" ")
print(x,y,z,sep=",")
print(x,y,z,sep=":")
print(x,y)
print(z,x)
print("x:y:z",x,y,z)
print("Cherry","Nazzu","Roja","Prasad",sep=",")
print("Cherry","Nazzu","Roja","Prasad",sep="@")
print('\n')  ## Two blank spaces bcz one for normal print and one for \n
print("good",end=" ")
print("Morning")

print("good",end=" ")
print("Morning",end=" ")
print("Nazzu")
print("good",end="\t")
print("Morning",end="\t")
print("Nazzu")

## output formating:
x=10;y=20
print("The vale of x {} and value {} ".format(x,y))
print("I Love Eating {} and Playing {}".format("Chicken","Cricket"))
print("I Love Eating {0} and Playing {1}".format("Chicken","Cricket"))
print("I Love Eating {} and Playing {}".format("Butter","Ludo"))
print("Hello {Name} Good {Greeting}".format(Greeting="Morning",Name="Nazzu"))
print('Hello {name}, {greeting}'.format(greeting = 'Goodmorning', name = 'John'))
x = 12.3456789
print('The value of x is %3.2f' %x)
print('The value of x is %3.4f' %x)
print("-------------------------------")




empid = int(input("Enter the i'd of the employ:  "))
empname = input("Enter the name of the employ:  ")
empsalary = int(input("Enter the salary of the employ:  "))
empaddress = input("Enter the address of the employ:  ")

print(empid)
print(empname)
print(empsalary)
print(empaddress)
print("Mr {} who's employ i'd is {} , he is anual income is {} and He is from {}".format(empname,empid,empsalary,empaddress))

print("--------------------------------------")

emp_details={}
emp_details['empid'] = int(input("Enter i'd of the employ: "))
emp_details['empname'] = input("Enter name of the employ: ")
emp_details['empsalary'] = int(input("Enter salary of the employ: "))
emp_details['empadress'] = input("Enter adress of the employ: ")
print("\n")
print("Employ details: ")
print("empid: ",emp_details['empid'])
print("empname: ",emp_details['empname'])
print("empsalary: ",emp_details['empsalary'])
print("empaddress: ",emp_details['empadress'])
print("\n")
print("Mr {} who's employ i'd is {} , his is anual income is {} and He is from {}".format(emp_details['empname'],emp_details['empid'],emp_details['empsalary'],emp_details['empadress']))