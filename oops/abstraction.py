"""Abstraction :- The concept of hinding properties of one class from the other class or outside class is called abstraction
---> EX: S.V can be accessed outside of the class using class name, but if we want to restrict this in order to hide the properties of
          a class we go with abstraction.
          using __ before property name .
          EX: __x=75

"""

# class sample:
#     __x=20      ##now x is hidden and can accessed with in the class only
#     y=700
#     print(__x)
#     print(y)
#     def display(self):
#         print(sample.__x,type(sample.__x))
#         print(sample.y,type(sample.y))
# ## End of the class
# s1=sample()
# s1.display()
# print(sample.y)
# print(sample.__x)  ## can't be accessed outside of class ## AttributeError: type object 'sample' has no attribute '__x'


## Hiding SV and NSV

# class sample:
#     __name="Nazzu"
#     def display(self):
#         self.__age=26
#         print(sample.__name)
#         print(self.__age)
# s1=sample()
# s1.display()
# # print(sample.__name)    # AttributeError: type object 'sample' has no attribute '__name'
# # print(s1.__age)  


# class sample:
#     __x=12300
#     def __display(self):
#         self.__y=220
#         print("x=",sample.__x)
#         print("y=",self.__y)
#     def show(self):
#         print("x=",sample.__x)
#         print("y=",self.__y)
# #End of the class
# s1=sample()
# # s1.__display   ## AttributeError: 'sample' object has no attribute '__display'
# s1.show()
# # ##print(__x)
# # ##print(__y)



# class sample:
#     __x=100
#     def display(self):
#         self.__y=120   ## Hiding NSV
#         print(sample.__x)
#         print(self.__y)
#         self.display2()
#     def display2(self):
#         self.z=sample.__x+self.__y
#         print("z=",self.z)
#         self.display3()
#     def __display3(self):      ## Hiding a method
#         self.a=50
#         print("a=",self.a)
# s1=sample()
# s1.display()
# s1.siaplat2()
# ##s1.display3()     
# print(s1.a)
# ## print(sample.__x)
# ## print(s1.__y)
# print(s1.z)
# print(s1.a)
            

# class sample:
#     hname=input("Enter Husband name: ")
#     wname=input("Enter Wife name: ")
#     hage=int(input("Enter Husband age: "))
#     __wage=int(input("Enter Wife age: "))
#     __sal=float(input("Enter Salary: "))
# s1=sample()
# print("Hname: ",sample.hname)
# print("Wname: ",sample.wname)
# print("Hage: ",sample.hage)
# # print("Wife age: ",sample.__wage)  ## AttributeError: type object 'sample' has no attribute '__wage'
# print("Salary: ",sample.__sal)       ## AttributeError: type object 'sample' has no attribute '__sal'


""" Class and function  """

# class sample:
#     x=10
#     y=20
#     print(x)
#     print(y)
#     z=x+y
#     print(z)
# print(sample.x)
# print(sample.y)

# def test():
#     a=30
#     b=40
#     print(a)
#     print(b)

## Without a function call a function cannot executed 
## NOTE:- SV no way related to object,so even without object u can access static variable 



""" DIGITAL LLYNC   """


# Data hiding --> providing the restrections to acess attribute or methods
#1.public attributes or methods : those variable have does not any restricton wheather inside or out side of class
#2.Pravite atri or metnods--> cannot accesed outside of class __huty

# objectname._classname.__attributename  private

# class student:
#     std_name="Suresh"
#     __std_mail="suresh@gmail.com"
#     def student_data(self):  # public method
#         return "{} mail i'd is {}".format(self.std_name,self.__std_mail)
#     def __std_data(self):    # pravite method
#         return "method is pravite"
#     def sample(self):
#         return self.__std_data()

# obj=student

# print(obj._student__std_mail)

# print(obj.std_name)
# print(obj.__std_mail)
# print(obj.sample())


# class student:
#     def __init__(self):
#         self.name="ravi"
#         self.age=25
#         self.__course="python"
#
#     def std(self):
#         return "heloo world"
#
# obj=student()
#
# print(obj.std())
# print(obj._student__course)    # syntax to use pravite variables is object._classname__attributename

# class super:
#     def __init__(self,a,b):
#         self.__a=a
#         self.__b=b
        
#     def __sup(self):
#         return "{}".format((self.__a,self.__b))

#     def hi(self):
#         return self.__sup
    

# obj=super(12,10)
# print(obj.hi())
# print(obj._super__a)
# print(obj._super__b)
# print(obj._super__sup())