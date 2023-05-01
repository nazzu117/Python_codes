""" 
Built-in attribute of a class:- For each and every class in python,some attributes are going to added automatically
                                by the python interpreter.
                                The attribute which are added by interpreter called built-in attributes

Built-in Attricutes of a class are: 

--> __bases__: Every class by default extends object class ,
               so object class is super class for every object

--> __doc__: For printing Doc String
             if no doc string prints None

--> __name__: for display class name 

--> __module__: For module information

--> __dict__: About Dictionary

"""
## Programme to illustrating bult-in attributes

# class test:
#     """SAMPLE CLASS FOR BUILT-IN ATTRIBUTES """
#     x=10
#     y=20
#     def m1(self):
#         print(self.x)
#         print(self.y)

# t=test()
# t.m1()
# print(test.__bases__)
# print(test.__doc__)
# print(test.__name__)
# print(test.__module__)
# print(test.__dict__)


"""    
NOTE:- We can add attrebute to the class and can also to add to the object at the same time removing attrebutes
from static and non static variable 
---> We add static variable ----- to class
---> we add NSV to  ---- to object

"""

## Adding attributes to class and object
## Adding SV and NSV to class and object explicitly
## Adding static variables to the class excipitly
## Adding non static variables to the object excipitly

# class sample:
#     a=10
#     def display(self):
#         self.b=20
# s1=sample()

# # printing static variable from outside of class
# print("A=",sample.a)
# # Adding one more static variable to the class from outside of the class
# sample.c=30
# print("C=",sample.c)
# ## printing NSV's from outside of the class
# s1.display()
# print("B=",s1.b)
# ## Adding one more non static variable to the class from outside of the class
# s1.d=40
# print("D=",s1.d)

""" creating onemore object"""

# s2=sample()
# s2.display()
# print("B=",s2.b)
### print("D".s2.d)  can't print d bcz its new object can't access previous object 
### Addiing one more NSV to object s2

# s2.e=200
# print("E=",s2.e)

## Static variable of class -----> a=10,c=30
## NSV's of the class -----------> b=20,d=40,e=200

## object s1 can access -----> b,d
## class  s2 can access -----> b,e

""" Removing attributes from the class and object """
## Removing attributes from the class and object using del keyword

# del sample.a
# print("A=",sample.a)     ## Error : AttributeError: type object 'sample' has no attribute 'a'

## Removing NSV's from the object
# del s1.d
# print("D=",s1.d)     ## AttributeError: 'sample' object has no attribute 'd'

# del s2.e 
# print("E=",s2.e)

## NOTE:- del only delets SV and NSV only not object

"""
Removing Attributes from the class
Removing Attrebutes from the object

EX:-  
         del test.a 
         del t1.b
del:del keyword is used to decrese referance count of the object
 
Rferance Count:- No of variables pointing to an object will gives the referance count   (OR)
                 No of variables storing the adress of the object will give the referance 

"""
## Ex1:
# class sample:
#     pass
# s1=sample()    ## Here the s1 variable pointing to an object ,so R.C=1
# del s1         ## Here it means it decreses referance count by 1 so R.C=0
"""
Then that object is removed automatically by the garbage collector 
whenever object going to be delete, then distructer is called i.e, when RC becomes 0

"""
## EX2:

# class test:
#     pass
# t1=test()
# t2=t1      ## Here 2 variables t1 and t2 are pointing same object so R.C=2
           ## Here t1 and t2 are storing adress of the same variable

## NOTE:- 
## No of variables = No of objects ------  FALSE
## RefCount= No of variables pointing to a object ----- TRUE
## RefCount= No of objects ----- TRUE



# class hello:
#     s=10
#     k=33
#     def meth(self):
#         self.x=1000
#         print(self.x)
# h=hello()
# del h
# h.meth()