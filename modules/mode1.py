""" Type of import: there are two types of importes are there
1.Normal import:- Here when we import a property from a module then it is mandetory the we need to specifi the
                 module name before the property name 
                 Ex: mode1.x , mode1.add ,mode1.display()
                     math.pi ....

2.from import:- here no need to specifi the module name before the prapertyname , we can directly import the property

"""

# print(help('modules'))

# import is the keyword for loading the module

# user defined modules

# import module_2
# d=444
# print("a=",module_2.a)
# print("b=",module_2.b)
# print("c=",module_2.c)
# print("d=",d)
# print(module_2.add(2,33))
# print(module_2.mul(67,55))
# print(module_2.div(45,9))
# print(module_2.sub(66,55))

# import mod1 
# z=mod1.x+y
# print("x=",x)
# print("y=",y)
# mod1.sum()
# def show():
#    print("Namaste...!!!")
   
   
# show()

# 2nd way of importing module

# from module_2 import *  # everything from module will imported 
# from module_2 import add,sub   # required functionality will be imported from the module.

# print(a)
# print(b)
# print(add(44,9898))
# print(sub(5,4))
# print(mul(5,7))
# print(div(99,9))


# when we have created same file names that will only consider the in a particular path ie
   # 1. current working folder of the file
   # 2. where python is installed
   # 3.where enviroment variable path is presented
# following syntax is to check the total paths python will considere

# import sys
# print(sys.path)

# if we want to add a different path follow the below syntax
# sys.path.append("add a specifi path here like C:/users/download")
# print(sys.path)


# we can import module with short name or any other names like you wish

# import module_2 as m2 

# print(m2.add(10,20))

# import module_2
# print(module_2.add(123,456))
# print(module_2.sub(321,123))
# import module_2
# print(module_2.sub(200,100))


#if our module changed during the course of the program, we would have to reload it. keyword reload()

# import imp
# # # this code got excuted
# import mmmmm
# imp.reload(mmmmm)

# import module_2
# print(dir(module_2))


