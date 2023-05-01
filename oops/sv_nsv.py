# class sample:
#      """ Samle Class """
#      x=20                       ## Static variables
#      y=40
#      def display(self):       ## A method shouls self have perameter
#                               ## which ever object calls this function then the object adress stored by self
#         print("x=",sample.x)
#         print("y=",sample.y)
#      def show(self):              ## all methods can accessed by static variable
#         print("x=",sample.x) 
#         print("y=",sample.y)
# ## End of the class
# ## To access the class members create a object ie, syntax as follows
# ## objectname=classname()
# s1=sample()                ## this is the object creation statement here internally a object gets created  and it's
# #                            ## adress stored in variable called as a referance variable (s1)
# # ## A method is always calling using object
# s1.display()
# s1.show()
# # ## Accessing static variable from outside the class using classname
# print(sample.x)
# print(sample.y)

""" # Defining multiple methods with in the class
   # Modifing the value of static variables using a method """ 

# class test:
#    x=10    # Static variable
#    y=20    # Static variable
#    def m1(self):
#       print(test.x) # SV accesing using classname
#       print(test.y)
#       ## modifing the values of x and y
#       test.x=30
#       test.y=40
#    def m2(self):
#       print(test.x) # this changes will afficted in other methods also
#       print(test.y)
# ## End of the class 
# t1=test()   ## obj creation statement here internally object is created and it's adress stored by a refereance variable ie, t1
# t1.m2()
# t1.m1()    ## prints x and y values and modifyes the values  
# t1.m2()    ## prints the modified values
# t1.m1()
# # ## static variables are no way related to objects
# # ## static variables always takes the modified values

# # """ NOTE:- if you modifie static variable then the changes will be reflected in the methods and always 
# # modified or updated static variable value will consider  """
# print("-----------------------------------------")
# t2=test()   ## Creating another object
# t2.m2()
# t2.m1()
# # # ## modifing sv from outside of class
# test.x=50
# test.y=60
# print("x=",test.x)
# print("y=",test.y)
# t1.m2()
# t1.m1()
# t1.m2()

#################################################################################################################
""" creating multiple objects """

# class test:
#    """ sample class """
#    x=100
#    y=200
#    def m1(self):
#       test.x=test.x+10
#       test.y=test.y+20
#       print(test.x)
#       print(test.y)
#    def m2(self):
#       test.x=test.x+30
#       test.y=test.y+40
#       print(test.x)
#       print(test.y)
# # End of the class
# t1=test()   ## creating object
# t1.m1()     ## x=110,y=220 print's
# t1.m2()     ## adds 30,40  modifies and prints 
# print("---------------------")
# t2=test()
# t2.m1()   
# t2.m2()

""" 1. Working with static,local,global variables
## Global variables----> Definds outside function
## Local Variables-----> Definds within the methods and within the class
## Static Variable-----> Defines inside the class and outside the methods

"""
# r=30
# class demo:
#    x=10   # SV
#    y=20   # SV
#    print(x)
#    print(y)
#    print(r)
#    def compute(self,p,q):
#       self.p=p
#       self.q=q
#       ## Modifing Global variable
#       global r
#       r=40
#       z=p+q+r     ## p,q,r are the local variables ,here some of local and global variables
#       w=demo.x+demo.y    ## some of stativ variable
#       print("z=",z)
#       print("r=",r)
#       print("w=",w)
# # ## End of the class 
# d1=demo()   ## object creation statement
# d1.compute(10,20)
# print(r)              ## global variable
# ### print(p,q,z,w)    ## local variables can't access without class name ex: demo.x,demo.y
# print(demo.x,demo.y)
# d2=demo()
# d2.compute(60,70)

#################################################################################################################

""" illustrating non static variable """
# class sum:
#    a=10
#    def display(self):   ## Here each object adress passed to self
#       self.x=10
#       self.y=20
#       print("x=",self.x)
#       print("y=",self.y)
#       print("a=",sum.a)
#       print("sum=",self.x+self.y+sum.a)
#       print(self)
# # ## End of the class
# s1=sum()   ## Creating referance variable which stores address of object.
# print(s1)  ## Prints indrect address of object s1
# s1.display()  #using object accessing class members
# #              #here s1 address is stored in the self of display and using
# #              #that self address we are initializing the NSVs.
# print(s1.x)  ## accessing the NSV outside of the class using object
# print(id(s1.x))
# print(s1.y)
# print(id(s1.y))
# s1.x=123
# print(s1.x)
# print(id(s1.x))
# print("--------------------------------")
# s2=sum()
# print(s2)
# s2.display()
# print(s2.x)
# print(id(s2.x))

# s2.x=40
# print(s2.x)
# print(id(s2.x))

# print(s1.x)
# print(s2.x)
# print(s1.y)
# print(s2.y)
# print("sum=",s1.x+s2.x)

# print(s2.x)
# print(s2.y)
# print("sum=",s2.x+s2.y)

#############################################################################################################

# class sample:
#    """ class to compute sum """
#    a=10   #SV
#    def display(self,p,q):
#       r=70          ## Local Variable
#       self.x=20     ## NSV
#       self.y=30
#       print("p=",p)
#       print("q=",q)
#       print("r=",r)
#    def show(self):
#       print("a=",sample.a)
#       print("x=",self.x)
#       print("y=",self.y)
#       print("sum=",self.x+self.y)
# ## end of the class
# s1=sample()
# print(s1)
# s1.display(100,200)    ## s1 address will be stored in self of display
#                        ##using this self only we are initializing x and y to 100 and 200
# s1.show()
# print(sample.a)   #accessing SV from outside the class

# ### Printing NSV outside of class
# print(s1.x,type(s1.x),id(s1.x))
# print(s1.y)

# #modifying NSV from outside the class
# s1.x=25
# s1.y=35
# print(s1.x,type(s1.x),id(s1.x))
# print(s1.y)

# #modifying sv
# sample.a=15
# print(sample.a)

# #creating one more object

# s2=sample()
# print(s2)

# s2.display(4,5)
# s2.show()
# print(s2.x,type(s2.x),id(s2.x))
# print(s2.y)

#################################################################################################################

#program illustrating non-static variable(NSV)
# class emp:
#     company="Infosys"        #SV
#     def getdetails(self):
#         self.ename=input("Enter employee name:") #NSV's
#         self.eid=int(input("Enter empid:"))
#         self.esal=int(input("Enter empsal:"))
#         self.desig=input("Enter designation:")
#         print(self)
#     #Note: NSVs defined in a method can be accessed by all the other methods    
#     def putdetails(self):
#         print("Ename:",self.ename) 
#         print("Eid:",self.eid)
#         print("Esal:",self.esal)
#         print("Designation:",self.desig)
#         print("Company:",emp.company)
#         print(self)
# # #end of the class
# e1=emp()  #object creation stmt
# print(e1)
# e1.getdetails()
# e1.putdetails() 
## emp().getdetails()  #one more object creates


# e2=emp()
# e2.getdetails()
# e2.putdetails()
    
# print(e1.ename)
# print(e2.ename)

# e1.esal=55000
# e1.putdetails()

#################################################################################################################

"""program for modifying static and non-static variable """

# class sample:
#     a=4.5#static variable
#     b=2.6#static variable
#     def display(self):
#         self.x=10 #non-static variable
#         self.y=20 #non-static variable
#         print("x=",self.x) 
#         print("y=",self.y)
#         print("a=",sample.a)
#         print("b=",sample.b)
#         #modifying the values
#         self.x=self.x+50
#         self.y=self.y+60
#         sample.a=sample.a+70
#         sample.b=sample.b+80
#         print("x=",self.x) 
#         print("y=",self.y)
#         print("a=",sample.a)
#         print("b=",sample.b)
# #end of the class        
# s1=sample() #object creation stmt
# print(s1) #prints indirect address of object
# s1.display() #using object accessing class member x=10 y=20 a=4.5 b=2.6

# s2=sample() #creating 2nd object
# print(s2)
# s2.display()
# print(s2.x)
# print(s2.y)

#Note: For Non-static variables values will be re-initialized for every object
#      but for static variables it takes the old modified values ,here object to object it
#      wont be re-initialised.


###################################################################################################

""" Programme to customer application """

# class customer:
#     "CUSTOMER APPLICARION "
#     def getdetails(self):
#         self.customer_name=input("Enter The Name of the Customer: ")
#         self.customer_accNO=int(input("Enter the Customer ACC No: "))
#         self.customer_address=input("Enter The Address of the Customer: ")
#         self.customer_accBal=int(input("Enter Balance :"))
#     def putdetails(self):
#         print("Customer name is :",self.customer_name)
#         print("Customer Acc Number :",self.customer_accNO)
#         print("Customer Address :",self.customer_address)
#         print("Customer Acc Balance :",self.customer_accBal)
#     def deposit(self):
#         self.damout=int(input("Enter deposit Amount :"))
#         self.totalamount=self.customer_accBal+self.damout
#         print("Total Amount :",self.totalamount)
#     def withdrawl(self):
#         self.wamount=int(input("Enter the Withdrawl amount :"))
#         self.totalamount=self.customer_accBal-self.wamount
#         print("Total Amount After withdrew :",self.totalamount)

# c1=customer()
# c1.getdetails()
# c1.putdetails()
# c1.deposit()
# c1.withdrawl()
# print("Total Amount:",c1.totalamount)
# c1.withdrawl()
# print("Customer Name: ",c1.customer_name)
# print("Total amount: ",c1.totalamount)

#############################################################################################################
""" Programme to access static and Nonstatic variables from outside of class """

# class sampleclass:
#     a=22.2
#     b=33.3
#     def accessing(self):
#         self.x=120   ## NSV
#         self.y=220   ## NSV
# s1=sampleclass()     ## Here no NSV bcz values will be allocated when method excuted
# s1.accessing()       ## Now values allocated stored in an object indirect adresss stored in self
# print("a=",sampleclass.a) # SV accessed using class name
# print("b=",sampleclass.b)

# print(s1.x,type(s1.x))   ## NSV accessed using object name
# print(s1.y) ## If we excute these 2 statements s1.accessing() method we get error bcz values won't be allowed to x,y
            ## so call s.accessing() first.
            ## but without calling method ,i want NSV to initilize,then go for constructors
            ## to overcome this,allocate vales for NSVs during object creation only using constructor



""" Program illustrating all types of variables---->local,global,static and non-static """

x=10            #global variable
class test:
    y=20        #static variable   
    def display(self,p): #local variable
        self.z=p       #non-static   
        self.w=x+test.y+self.z+p
        print("x=",x)  #printing global variable
        print("p=",p)  #printing local variable
        print("y=",test.y) #printing static variable
        print("z=",self.z) #printing non-static variable
        print("w=",self.w) #printing non-static variable
#end of the class
t1=test()
t1.display(30)
print(x)
print(test.y)
print(t1.z)
print(t1.w)
# print(p)  # local variable cant be accessed


#Local variable can be accessed only by that method but NSV can be accessed by
#all the methods of a class and also by the other classes.













