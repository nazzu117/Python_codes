""" Distructor:- When ever a object gets removed, distructer will be executed automatically 
Distructor all ways defined by using  __del__  
Distructor will excuted automatically when ever a object gets removed, we no need to call

"""

class sample:
    def __init__(self):
        print("Constructor called...@@")
    def __del__(self):
        print("Distructor called....@@")

# s1=sample()  ## RC=1
# # s2=sample()  ## RC=1
# s3=sample()  ## RC=1
# print(s3)
# s3=sample()  ## If same ref.var used, the RC of the previous s3 decreases by 1 
#              ## RC=0,(If same varible used RC decreases i.e, 0)
#              ## Previous object s3 removed and distructor got executed and then new s3 object created 
# print(s3)

####################################################################################

# class test:
#     def __init__(self):
#         print("Constrictor called..")
#     def __del__(self):
#         print("Distructor called...")
# t1=test()  ## RC=1
# t2=t1      ## RC=2
# t3=t1      ## RC=3 All three variables pointing to same object,storing adress of same object ,so RC=3
# print(t1)
# print(t2)
# print(t3)

# t1=test()   ## Previous object RC decreased by 1 i.e, then it becomes Rc=2
#             ## previous t1 variable removed and new t1 variable created which will point to another object
#             ## so first object RC becomes 2 bcz one variable t1 removed 
# print(t1)   ## prints new object address 

# t2=test()   ## previous t1 variable removed and new t2 variable created which will point to another object
#             ## so first object RC becomes 2 bcz one variable t2 removed 
# print(t2)   ## prints new object address   

# t2=test()   ## previous t3 variable removed and new t3 variable created which will point to another object
#             ## so first object RC becomes 2 bcz one variable t3 removed 
# print(t2)   ## prints new object address   

################################################################################################################

""" del keyword is not for removing object,it is used to decrease the referance count by 1 
    when RC becomes 0 then garbage collector and distructer executed
"""

class test:
    def __init__(self):
        print("Constructor called...")
    def __del__(self):
        print("Distructer called...")
t1=test() ## RC=1
print(t1)
del t1   ## RC=0 Then garbage collector called and distructor executed and object executed
### print(t1)    ### NameError: name 't1' is not defined

# t2=test() ## RC=1
# print(t2)
# t3=t2  ## RC=2
# print(t3)
# del t2   ## RC decreases to 1  RC=1
# print(t2)
# print(t3)   ## Object still avilable and it's adress is stored in t3 variable 
# del t3      ## RC decreass to 0 ,destructer executed and removes objected
# print(t3)  ## object not avilable

#Q)if object R.C=3 then how ref variables?------------------------------->3
#Q)if 3 ref variables storing address of single object----->R.C=?-------->3


#Q)if there are 5 objects---------> 
#max no of times a constructor executes is--------------->5
#min no of times a constructor exectes is---------------->5
#max no of times a destructor executes is---------------->5
#Min no of times a destructor executes is --------------->0

###################################################################################################################

# x=1[10,2.5,True,10,"python"]
# print(x)  ## RC=1

# ## Removing float and int objects
# del x[1]    ## RC of float object become zero ,so float object removed 
# print(x)    
# del x[0]    ## RC was 2 becomes 1
# print(x)
# del x[1]    ## RC was 1 becomes 0 ,int object removed
# print(x)

# del x
## print(x)

##############################################################################################################

# class test:
#     def __init__(self):
#         print("Constructor called ")
#     def __del__(self):
#         print("Distructor called ")
# t1=test()
# t2=test()
# t3=test()
# print(t1)
# print(t2)
# print(t3)

# x=[t1,t2,t1,t3,t1]  ## RC of t1=4 ; RC of t2=2 ; RC of t3=2 ---> x[0]=t1,x[2]=t1,x[4]=t1

# del x[1]  ## RC of t2 decreases to 1
# print(t2)
# del t2    ## RC of t2 decreases to 0 , destructor call and onject removed
# ## print(t2)
# del x[0]  ## RC of t1 decreases to 3
# del x[0]  ## RC of t1 decreases to 2
# del x[1]  ## RC of t1 decreases to 1
# del t1    ## RC of t1 dectrases to 0 the distructer executed and t1 removed
# ## print(t1)

# print("\n")
# x.remove(t3)    ## RC of t3 becomes 1
# print(x)

# del t3         ## RC of t3 becomes 0

# del x         ## Removes list


###############################################################################################################################


# Using Constructor incrementing employees 
# Using Destructor decrementing employees

# class employee:
#     empcount=0
#     def __init__(self,x,y):
#         self.ename=x
#         self.salary=y
#         employee.empcount+=1
#     def __del__(self):
#         employee.empcount-=1
#     def displayemployee(self):
#         print("NAME:",self.ename,"SALARY:",self.salary)
        
# emp1=employee("Rohith",30000.00) #RC=1
# emp2=employee("Ajith",40000.00)  #Rc=1

# emp1.displayemployee()
# emp2.displayemployee()
# print("Total No of employees:",employee.empcount)
# del emp1 #Rc becomes 0 and destructor called and emp1 is removed.
# print("Total No of employees:",employee.empcount)
# del emp2 #Rc becomes 0 and destructor called and emp2 is removed.
# print("Total No of employees:",employee.empcount)



