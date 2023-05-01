""" Garbage collector : Garbage collector is a pre-defined program or application or background thread which is 
                        is invoked by the python interpreter when ever any object referance count(RC) become Zero
                        at the time of execution of programme.
--> Grabage collector removes the un-used or un refernced objects from the memory location  
--> If any object referance count become zero, then we called that object as un-used or unreferanced object
--> Referance count is equals to the no of referance variables pointing to the object.

"""
#EX:-
# class test:
#     pass
# t1=test()
# t2=t1
# t3=t1   ## Here all three referance variables are storing the address(pointing) of same object so R.C=3
#         ## which is equals to no of ref variables (3)
# """ No of referance variables is not equals to no of objects """
# del t3    ## RC decreased by 1 i.e, RC=2 , object is not removed
# del t2    ## RC decreased by 1 i.e, RC=1 , object is not removed
# del t1    ## RC decreased by 1 i.e, RC=0 , object is removed by garbage collector 
"""
Whenever any object removed from the memory location, then the distructor of the class will be executed 
"""
# class test:
#     pass
# t1=test()  # RC=1
# print(t1)
# del t1    ## RC becomes 0,Garbage collector called and removed object.
# print(t1)
### -------------------------------------------------------------------------------------------------------------
# class sample:
#     pass
# s1=sample()  ## RC=1
# s2=sample()  ## RC=1
# print(s1)
# print(s2)

# del s1  ## RC becomes 0 and garbage collector called and removed object s1
# print(s1)
# del s2  ## RC becomes 0 and garbage collector called and removed object s1
# print(s2)

""" Removing attributes from a class and object
Removing Static v and NSV"s  """

# class sample:
#     x=10
#     y=20
#     def m1(self):
#         self.a=220
#         self.b=330
# s1=sample()  ## RC=1
# print(s1)
# print(sample.x)
# print(sample.y)
# ## Removing both static and nonstatic
# del sample.x  ## Removing attributes(SV) from class
# del sample.y  ## Removing attributes(SV) from class
# print(s1)
# print(sample.x)  ## AttributeError: type object 'sample' has no attribute 'x'
# print(sample.y)  ## AttributeError: type object 'sample' has no attribute 'y'

# s1.m1()
# print(s1.a)
# print(s1.b)
# ## Removing the NSV's
# del s1.a   ## ## Removing attributes(NSV) of object
# ##print(s1.a)
# print(s1)
# del s1.b
# ##print(s1.b)
# print(s1)

# s2=sample()     ## This execute perfectly
# print(s1.a)
# print(s1.b)