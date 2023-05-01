""" Constructor: constructor is special kind of method which is used to initialize the NSV of the class at 
                 the time of creation of "object"

Properties of constructor:-

1.constructors are used to initialize NAV's of class during object creation only
2.Constructor executed automatically when ever object created but for normal method we need to call
3.for one object,constructor will be executed only once ,bcz only once we initialize
4.constructor should always defind with the name of  __init__

Syntax:

def __init__(self,parameters):
    ...........................
    ...........................
    ...........................
    ...........................
    ...........................

:::: Difference between method and constructor ::::


           Methods                             Constructors
1.Method name can be any name              1.Constructor name should be __init__()
2.Methods are used to represent            2.Constructors are used to initialize
  the Bussiness logics to                    the Non-static variables of a class
  perform the operations
3.Method will be executed whenever         3.Constructor will be executed automatically
  we make a method call using object         whenever we create a object.
4.with respect to one object               4.with respect to one object, 
  one method can be called for               a constuctor will be executed only once.
  'n' no of times.



Constructors are of two types:-

1.Default constructor       : A constructor without parameters()
2.parameterized constructor : A constructor with parameters(self,parameters)


"""
## ::: DEFAULT CONSTRUCTOR :::

# class sample:
#     """ CONSTRUCTOR  """
#     def __init__(self):   ## Constructor
#         print("Constructor of sample class...::: ")
#         self.x=10
#         self.y=20
#         print("Hello World...@@")
#     def display(self):   ## Method
#         print("Method of sample class")
#         print(self.x)
#         print(self.y)
# ## End of the class 
# s1=sample()    ##  whenever object created ,immediately constructor executed automatically
# print(s1)
# print(s1.x,type(s1.x))
# print(s1.y)
# s1.display()
# s1.display()     ## Method calls multiple times
# print("\n\n")

# s2=sample()
# print(s2)
# print(s2.x,type(s2.x))
# print(s1.y)
# s2.display()
# s2.display()

""" In this programme as there are two objects,so constructor excuted for two times,
if there are 'n' no of objects then constructor excuted 'n' no of times
"""

########################################################################################################



""" Programme to find volume of a cube using constructor """

# class cube:
#     def __init__(self):
#         self.length=int(input("Enter the length cof cube :"))
#         self.width=int(input("Enter the wudth of the cube :"))
#         self.height=int(input("Enter height of the cube :"))
#     def compute(self):
#         self.volume=self.length*self.width*self.height
#         print("Volume of Cube = ",self.volume)
# c1=cube()     ## constructor excuted automatically
# print(c1)
# c1.compute()
# print(c1.volume)
# print("Enter values of secound cube::: ")
# c2=cube()
# c2.compute()

##############################################################################################################

""" modifying non-static variables """

# class sample:
#     def __init__(self):
#         self.x=10
#         self.y=20
#     def m1(self):
#         self.x=self.x+30 #modifying NSV
#         self.y=self.y+40
#         print(self.x)
#         print(self.y)
# s1=sample()            # constructor executed automatically,
#                        # means NSV's are created and initialized

# print(s1.x) #x=10
# print(s1.y) #y=20
# s1.m1()  #  x=40 y=60
# s1.m1()  #  x=70 y=100

# s2=sample()  #constructor executes for 2nd time
# print(s2.x) #x=10
# print(s2.y) #y=20
# s2.m1()      #x=40 y=60
# s2.m1()      #x=70 y=100

############################################################################################################


# class student:
#     def __init__(self):
#         self.name=input("Enter student name:")
#         self.rollno=int(input("Enter student rollno:"))
#         self.branch=input("Enter student branch:")
#         self.rank=int(input("Enter rank:"))
#     def display(self):
#         print("NAME:",self.name)
#         print("ROLLNO:",self.rollno)
#         print("BRANCH:",self.branch)
#         print("RANK:",self.rank)
        
# print("Enter student1 details:")
# s1=student()
# # print(s1.name)
# s1.display()

# print("Enter student2 details:")
# s2=student()
# s2.display()
# print(s2.name)

""" Drawback of defacult constructor """

# class sample:
#   def __init__(self):
#     self.x=0
#     self.y=0
#     # print(self.x)
#     # print(self.y)
# s1=sample()
# print(s1.x)    ## printing default values of x and y
# print(s1.y)
# s1.x=10
# s1.y=20   ## Modifing x and y values 
# print(s1.x)
# print(s1.y)

# s2=sample()
# print(s2.x)    ## ## printing default values of x and y
# print(s2.y)

# print("\n\n\n")
# s2.x=30
# s2.y=40
# print(s2.x)
# print(s2.y)

## Here the problem is for every object s1,s2,s3......Sn initilly initilised with default values x=0 and y=0 
## and then later assigned or modified with some values but initilly i want 10,20 for s1 and 30,40 for s2
## so in this case we go for parametrized constructor......


## Disadvantage of default constructor......@@@@ 


# class student:
#   def __init__(self):
#     self.name="Ajay"
#     self.age=26
# s1=student()
# print(s1.name)
# print(s1.age)

# s1.name="Bandi Sanjay"
# s1.age=45
# print(s1.name)
# print(s1.age)

# s2=student()
# print(s2.name)   ## prints default values
# print(s2.age)
# s2.name="Sumanth Asween"
# s2.age=35
# print(s2.name)
# print(s2.age)

#Here evertime the constructor is initializing the NSV's with same values, but i want different values for 
#each object during object creation only,then go for parameterized constructor,which specifies
#different values for each object.

""" PARAMETERIZED CONSTRUCTOR :-A constructor with parameters is called parameterized constructor
# NOTE: In parameterize constructor,how many arguments provided those many NSV's to be defined """

# class student:
#   def __init__(self,name,age):
#     self.stdname=name
#     self.stdage=age
#     # self.display()
#   def display(self):
#     print("Name:",self.stdname)
#     print("Age:",self.stdage)
# s1=student("Ajay",26)
# s1.display()
# s2=student("Miller",25)
# s2.display()
# s3=student("Don Bosch",55)
# s3.display()

## NOTE: When Ever object created, it is initilize NSV's with different values

""" Parameterized constructor which contailns parameters   """

# class test:
#   def __init__(self,a,b):
#     self.x=a
#     self.y=b
#   def m1(self,p,q):
#     r=p+q   ## Local variable sum
#     s=self.x+self.y   ## Sum of NSV's
#     print("r=",r)
#     print("s=",s)
# t1=test(10,20)
# print(t1.x)
# print(t1.y)
# t1.m1(10,20)

# t2=test(100,200)
# print(t2.x)
# print(t2.y)
# t2.m1(111,222)

# t3=test(1000,2000)
# print(t3.x)
# print(t3.y)
# t3.m1(400,500)

""" Customer Application """

# class customer:
#     """customer Application"""
#     bankname="SBI"  #static variable
#     def __init__(self,custname,accno,addr,bal): 
#    #how many constructor parameters are defined,those many NSV's should be defined
#         
#         self.custname=custname
#         self.accno=accno
#         self.addr=addr
#         self.bal=bal
#     #operations
#     def deposit(self,depositamt):
#         self.bal=self.bal+depositamt
        
#     def withdraw(self,withdrawamt):
#         self.bal=self.bal-withdrawamt
        
#     def balenq(self):
#         print("Balance:",self.bal)
        
#     def display(self):
#         print("Customer Name:",self.custname)
#         print("Account No:",self.accno)
#         print("Address:",self.addr)
#         print("Balance:",self.bal)
# #end of the class
        
# c1=customer("scott",5230143,"Ameerpet",60000.00)
# c1.deposit(20000.00)
# c1.withdraw(10000.00)
# c1.balenq()
# c1.deposit(30000.00)
# c1.withdraw(20000.00)
# c1.display()
# print(c1.custname)
# print("Bank name:",customer.bankname)

# print("\n\n\n")
# c2=customer("Blake",6230143,"Chennai",40000.00)
# c2.deposit(20000.00)
# c2.withdraw(10000.00)
# c2.balenq()
# c2.deposit(30000.00)
# c2.withdraw(20000.00)
# c2.display()
# print("Bank name:",customer.bankname) 

# #Creating list of customers
# customers=[]
# customers.append(customer("scott",5230143,"Ameerpet",60000.00))
# customers.append(customer("Blake",6230143,"Chennai",40000.00))

# for obj in customers:
#     print(obj.custname,obj.accno,obj.addr,obj.bal)



#Here if customer withdrawing more than available balance
#then he should be restricted by using exception handling
#i.e displaying "Insufficient funds"


""" Parameterized constructor , accepting values from constructor  """

#parameterized constructor, accepting vaues from keyboard

# class customer:
#     '''CUSTOMER APPLICATION'''
#     bankname="SBI"
#     def __init__(self,custname,custaccno,custaddr,cbal):
#         self.cname=custname
#         self.caccno=custaccno
#         self.caddr=custaddr
#         self.bal=cbal
#     def deposit(self,depositamt):
#         self.damt=depositamt
#         self.bal=self.bal+self.damt
#         print("After depositing",self.damt,"\t","BALANCE=",self.bal)
#     def withdraw(self,withdrawamt):
#         self.wamt=withdrawamt
#         self.bal=self.bal-self.wamt
#         print("After withdrawing",self.wamt,"\t","BALANCE=",self.bal)
#     def balanceenq(self):
#         print("BALANCE:",self.bal)
#     def display(self):
#         print("CUSTOMER NAME:",self.cname)
#         print("ACCOUNT NO:",self.caccno)
#         print("ADDRESS:",self.caddr)
#         print("BALANCE:",self.bal)
        

# print("Enter details of Customer:")
# name=input("Enter customer name:")
# accno=input("Enter Account no:")
# addr=input("enter Address:")

# c1=customer(name,accno,addr,30000)
# c1.withdraw(5000)
# c1.balanceenq()
# c1.deposit(10000)
# c1.display()

"""    Employee Application that perform all the operations like PF(),ES(),HRA(),Tax(),DA() """

# class employee:
#   """ Employee Application """
#   company="Infosys"
#   empcount=0
#   def __init__(self,empname,empid,empsal,design):
#     ## How many constructor perameter defined those many NSV's should defind
#     """Data-NSV's """
#     self.empname=empname
#     self.empid=empid
#     self.empsal=empsal
#     self.design=design
#     employee.empcount+=1
#     ## Operations
#   def da(self,daamt):                 ## Daily Allowances
#     self.empsal=self.empsal+daamt
#   def hra(self,hraamnt):              ## House Rent Allowance
#     self.empsal=self.empsal+hraamnt
#   def ta(self,taamt):                 ## Travelling Allowance
#     self.empsal=self.empsal+taamt
#   def pf(self,pfamnt):
#     self.empsal=self.empsal-pfamnt
#   def tax(self):
#     if ((self.empsal>250000) and (self.empsal<=500000)):
#       self.empsal=self.empsal-self.empsal*0.10
#       print("Employee salary after Tax deductions..= ",self.empsal)
#     elif ((self.empsal>500000) and (self.empsal<=1000000)):
#       self.empsal=self.empsal-self.empsal*0.15
#       print("Employee salary after Tax deductions..= ",self.empsal)
#     elif ((self.empsal>1000000)):
#       self.empsal=self.empsal-self.empsal*0.20
#       print("Employee salary after Tax deductions..= ",self.empsal)
#   def displayemployee(self):
#     print("Name Of The Employee",self.empname)
#     print("Id of the Employee =",self.empid)
#     print("Employee salary =",self.empsal)
#     print("Designation of the Employee =",self.design)

# # End of the class
# print("Company Name: ",employee.company)
# emp1=employee("Miller",10102,500000,"Manager")
# emp1.da(1500)
# emp1.hra(10000)
# emp1.ta(3000)
# emp1.pf(1200)
# emp1.displayemployee()
# emp1.tax()

# emp2=employee("Miller",10102,500000,"Manager")
# emp2.da(15000)
# emp2.hra(10000)
# emp2.ta(15000)
# emp2.pf(12000)
# emp2.displayemployee()
# emp2.tax()

# print("Total no of employees: ",employee.empcount)
# print("Company",employee.company)







    
        


              
              
    








