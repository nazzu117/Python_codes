#with stmt:-

#The with statement can be used while opening a file, The Advantage of with stmt is
#It takes care of closing a file which is opened by it.
#with stmt follows space indentation

data='''
1.Python is Simple
2.python is user-friendly
3.Pyhon supports interactive mode
4.Python supports 89300 modules
5.Python has many built-in libraries
6.Python supports object-oriented programming
7.Python supports all major databases
8.Python is dynamic typed
9.python provides simple syntaxes
10.Python is extensible ''' 

# with open("sample.txt",mode="w") as f:
#     f.write(data) 

# with open("sample.txt",mode="r") as f1:
#     print(f1.read())   

#       #(or) reading using for loop
# with open("sample.txt",mode="r") as f2:
#     for line in f2:
#         print(line)


#-------------------------------------------------------------------------------------------------------


# #Program to read last 'n' lines from a file
# file1=input("Enter the file path:")
# n=int(input("Enter the value of n:")) #n--->last 'n' lines

# with open(file1) as f1:
#     print("Last",n,"lines are:")
#     for line in(f1.readlines()[-n:]):
#         print(line)

#########################################################################################################


#Reading first 'n' lines

# file1=input("Enter the file path:")
# n=int(input("Enter the value of n:")) #n--->last 'n' lines

# with open(file1) as f1:
#     print("First",n,"lines are:")
#     for line in(f1.readlines()[:n]):
#         print(line,end="")


##########################################################################################################

#Reading specific lines---->3rd and 5th line

# file1=input("Enter the file path:")

# with open(file1) as f1:
#     for line in(f1.readlines()[2:5:2]):
#         print(line,end="")


################################################################################################################

#Reading data from one file and writing data to other file

#I-method

# f=open("demo1.txt","r")
# x=f.readlines()
# f.close()

# f1=open("demo2.txt","w")
# for p in x:
#     f1.write(p)
# f1.close()         ## HEre we need to close the file then only operation performed

# f2=open("demo2.txt","r")
# print(f2.read)
# f2.close()
""""
## II-Method
## Using-read()
"""

f=open("demo1.txt","r")
x=f.read()
print(x,type(x))
f.close() 

f1=open("demo2.txt","w")
for p in x:
    f1.write(p)
f1.close()      #here we need to cloe the file then omly the operation will b perfored

f2=open("demo2.txt","r")
print(f2.read())
f2.close() 

########################################################################################################



f1=open("C:/python1130amm/str2.py","r")
x=f1.readlines()
f1.close()

#f2=open("demo3.py","w+")
f2=open("C:/python1130amm/demo.py","w+")
for line in x:
    f2.write(line)
f2.seek(0)
print(f2.read())
f2.close()

'''
f3=open("demo2.py","r")
print(f3.read())
f3.close()
'''

#Read 2 .py files and write into a single .py file

f=open("C:/python1130amm/lists/3 List functions.py","r")
x=f.read()
print(x,type(x))
f.close()

f1=open("C:/python1130amm/lists/7 list address.py","r")
y=f1.read()
print(y,type(y))
f1.close()

f2=open("merge.py","w")
for p in x:
    f2.write(p)
for q in y:
    f2.write(q)
f2.close()      #here we need to cloe the file then omly the operation will b perfored

f3=open("merge.py","r")
print(f3.read())
f3.close()
