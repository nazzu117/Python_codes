""" Files Handling:- what is the file actually: They are named locations to store data on our divice

All programming process data in the RAM, but RAM is Volatile,
once execution is finished,The data will be removed.

---> Programming languages are good for Processing
---> Programming languages are bad for storage. 
--->Python programme are processed with ram and after processing they can be stored in any of the following
    EX: 1) Files--->.txt,.csv,.xls,.pdf,.xml,.json
        2) Databases-->oracle,mysql,DB2
        3) NoSQL--->cassandra,mongoDB,HBase,
Python can easly connect with the file and databases to store and retrive the data.


we have CRUD operations i.e, Create,Read,Update,Delete
python file handling system 1.we creat a file
                            2.we opean a file
                            3.we work on file
                            4.we close the file
"""
# python have some builtin functions
# file handling operations are important in web applications
# 1. opeaning
# 2. read and write
# 3. create
# 4. append

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists

"""
open(): open function is a pre-defined function used to open a file
At the time of openening a file,we need to specify the mode of the file.
mode indicates for what pupose you are opening the file.
The various modes are
        Mode               Description
    1.  'r'------------> opens a file for reading data(default mode)
    2.  'w'------------> opens a file to write data into a file.
                         It creates a new file and writes if the file
                         doesnot exist.
                         if file already exists then it
                         truncates(removes) and writes.
    3.  'a'------------> opens a file to append data at the
                         end of the file.
                         if file doesnt exist it creates a new file and appends
                         if file already exist,it appends the data.
    4.  't'------------> opens a file in text mode.
    5.  'b'------------>opens a file in binary mode.
    6.  'w+'------------>opens a file to write and read data of a file.
                         The previous data in the file will be deleted.
    7.  'r+'------------>opens a file to read and write data into a file.
                         The previous data in the file will not be deleted.
                         The File pointer will be at the beginning of file.
    8.  'a+'------------>opens a file to append and read data of a file.
                         The file pointer will be at the end of the file.
                         
---------------------------------------------------------------------------------------------------
read mode: for reading data from a file, we have 3 methods

1.read()      :It reads the entire file
2.readline()  :It reads a particular line
3.readlines() :It reads all the lines of a file and creates a list
               Each line will be treated as a element of a list.


"""

# two ways to open a file

# #opening a file and reading
# f=open("demo1.txt",mode="r") #whenever we call open fn,it internally creates a file object
# print(f.read())
# f.close()
# #if we use f.close(),then  object which is created is going to be deleted.
# #print(f.read())
#-----------------------------------------------------------------------------------------------------------------
"""Reading a python file"""

# f=open("fileprblms.py",mode="r")
# print(f.read())
# ####################################################################################################

# #f=open('demo1.txt',mode='r')  #reading txt file
# #f=open('C:/python630am/string3.py',mode='r')   #reading a python file
# #f=open('C:/python1/sample.java',mode='r')     #reading java file
# f=open('F:/emp1.csv',mode='r')                #reading csv file
# #f=open('F:/emp.xlsx',mode='r')                #cannot read this excel file
# print(f.read())

# f.close()
#####################################################################################################

# file_data=open("sample.txt","r")  # use this method if file is in the same folder ie,. u r python folder file.py
# print(file_data)                  # in this type we have to close the file after reading 
# file_data.close()                  # by using this u can close the file after completion of your work
# print(file_data.closed)            # use this syntax to check whether the file is close r not.


# data_=open("C:/Users/nazeer/Contacts/text.txt.txt","r")
# print(data_)
####################################################################################################
#openining and Reading multiple files

# f1=open('sample.txt',mode='r')
# print(f1.read())
# f1.close()

# print("\n")

# f2=open('fileprblms.py',mode='r')
# print(f2.read())

# print("\n")

# # f3=open('C:/python1/sample.java',mode='r')
# # print(f3.read())

# print("\n")

# f4=open('F:/comma.csv',mode='r')
# print(f4.read())

# print("\n")

# for p in f4:
#     print(p)

##############################################################################################################

#Reading multiple files at a time

# f1=open("sample.txt",mode="r")            #reading a .txt file

# # f2=open("C:/data/sample.java","r")       #reading a java file
# f3=open("fileprblms.py")       #reading a python file
# f4=open("excsv.csv","r")
# '''
# print(f1.read())                         
# print(f2.read())
# print(f3.read())
# print(f4.read())'''

# x=[f1,f3,f4]

# for p in x:
#     for q in p:
#         print(q)
#     print("\n")

##-----------------------------------------------------------------------------------------------
# f=open("sample.txt",mode="r") #whenever we call open fn,it internally creates a file object

# for p in f:
#     print(p)
# f.close()

#############################################################################################################
""" second way of reading a file 
in the secound method u no need to close the file it will automatically closes the file no need to close again """

# with open("sample.txt","r") as data_2:
#     print(data_2)
# print(data_2.closed)
# with open("C:/Users/nazeer/Desktop/Python/hloo.txt","r") as file_1:
#     print(file_1)                                        

################################################################################################################
# reading the file 3 ways to:-
# 1.read.       reads complete file at a time 
# 2.readline    reads only one  line i.e, 1st line
# 3.readlines. read all the lines in the file most commonly used 

# with open("C:/Users/nazeer/Pictures/text.txt","r") as data_2:
#     print(data_2.readline())
#     print(data_2.readlines())
#     print(data_2.readlines()[1])

# with open("sample1.txt","r") as data_2:
#     print(data_2.readlines())

##################################################################################
# f=open("sample.txt")
# print(f.tell())
# print(f.readline())
# print(f.tell())
# print(f.tell())
# print(f.readline())
# f.seek(5)
# print(f.readline())
# print(f.read(5))
# print(f.tell())
# print(f.readline())
# f.seek(17)
# print(f.readline())
# print(f.tell())
# f.seek(31)
# print(f.tell(),f.read())
# print(f.tell())

# f.seek(0)
# #applying for loop on the file object(f) and reading each line.
# for p in f:
#     print(p)
#################################################################################################################
""" Readlines(): """

# #readlines()

# f=open("sample.txt","r")
# x=f.readlines() # reads all the lines and stores in a list x with \n behaviour
# print(x,type(x))        # printing the list x

#printing each line seperately

# for p in x:
# #     print(p)
    
# f.close() # whenever we close a file, it will be used by
# #           #another person

# print(x[2])


#-----------------------------------------------------------------------------------------------------

# f=open("heloo.txt","r")
# x=f.readlines()
# print(x)

# # Read only employee names and salray
# for p in x:
#     # print(p.split(",")[1],p.split(",")[2])
#     print(p.split(",")[1:3])


#########################################################################################################
#                                        """ Write Data """

# 2.writing file...

# f=open("demo1.txt","w")

data=''' 1.Python is Simple
2.python is user-friendly
3.Python supports interactive mode
4.Python supports 89300 modules
5.Python has many built-in libraries
6.Python supports object-oriented programming
7.Python supports all major databases
8.Python is dynamic typed
9.python provides simple syntaxes
10.Python is extensible '''

# f.write(data)
# f.write("Hello\nHow are you\n man ")  #if file already exists,it truncates(removes) the data
#                                       #and writes the new data
# f.write("\n Hii...")  #if we wont close, we can not write into it  or delete it
#   # If we close the file then only we can see the data

# f1=open("demo.txt","r")   #here f1 is only for reading
# #f1=open("C:\python1030amm\demo1.txt","r")
# print(f1.read())    
# f1.close()

#-------------------------------------------------------------------------------------------------
# Creating a .csv file and writing data n to it

# f=open("hello.csv","w")
# f.write("Namste Hyderabad")
# f.write("\nNamste Bangalore")
# f.write("\nNamste Mumbai")
# #if file doesnt exist, it creates a new file and writes
# f.close()

# f=open("hello.csv","r")
# print(f.read())
# f.close()

#---------------------------------------------------------------------------------------------------
#writing into a python file
f=open("Test.py",mode="w")

f.write("x=[10,20,30,40,50]\n")
f.write("print(x)\n")
f.write("print('sum of list elements=',sum(x))")

                       #if file already exists, so it truncates(removes)

f.close()              #if file doesnt exist, it creates a new file and writes

f1=open("Test.py")
print(f1.read())    
f1.close()
#--------------------------------------------------------------------------------------------------
#writing into a python file
# f=open("Test2.py",mode="w")

# #entire python file data taken as string and write this string into the file
# data='''
# x=[10,20,30,40,50]
# print(x)
# print('sum of list elements=',sum(x))'''

# f.write(data)
#                        #if file already exists, so it truncates

# f.close()              #if file doesnt exist, it creates a new file and writes

# f1=open("Test2.py")
# print(f1.read())    
# f1.close()

#-------------------------------------------------------------------------------------------------------
#writing into a python file to add 2 no's
# f=open("Test3.py",mode="w")
# f.write("x=30\ny=40\nprint(x+y)") #file already exists, so it truncates
#f.write("y=20 \n")
#f.write("print(x+y) \n")
# f.close()              #if file doesnt exist, it creates a new file and writes

# f1=open("Test3.py")
# print(f1.read())    
# f1.close()
#-----------------------------------------------------------------------------------------------------------
""" Accepting i/p from keyboard and writing into a file """

# f=open("emp.txt","w+")  # w+ it can write and read
# emp1=input("Enter the Emp details= ")
# f.write(emp1)
# f.seek(10)
# print(f.read())
# f.close()

# f1=open("emp.txt","r")
# print(f1.read())
# f1.close()

#-----------------------------------------------------------------------------------------------------------
# f=open("emp.txt","r+")  #r+ mode wont remove the previous data

# print(f.read())
# f.write(" Manager Hyderabad ")
# f.seek(0)
# print(f.read())

# f.close()


#append mode
f=open("sample.txt","a+")
x=input("New Employee Details: ")
f.write("\n")
f.write(x)
f.seek(0)
print(f.read())
f.close()
#------------------------------------------------------------------------------------------------------


# with open('C:/Users/nazeer/Desktop/Python/sample.txt',"w") as data_2:
#     data_2.write("this is sample file to check and the thing is good enough allthe time\n" )  # write allows only single line
#     data_2.write("secound line is to check for the learning purpose")
#     # data_2.writelines(["the manin thing of the country only is to\n", "determination and attitude is allthe time is importent isntit\n","padarapadra padara neaduku madulkkoni tankindai kadaraa"])
    # data_2.writelines(["hii how are you\n","where are you now\n","hope all is doing good"])


# 3.append   it is add the new content to the previous one.  if the file is not present it will create like write
#--> write 
# #--> writelines

# with open('C:/Users/nazeer/Desktop/Python/sample1.text',"a") as data_2:
#     data_2.write("this is sample file to check\n and the thing is good allthe time" )
#     data_2.writelines(["the manin thing of the country only is to\n", "determination and attitude is aallthe time is importent isntit\n","padarapadra padara neaduku madulkkoni tankindai kadaraa"])


# csv- comma saperated values in this we have
#--> Read mode
#--> Write mode


# with open("MyDetails.txt","x") as data:
#     print(data)
# with open("MyData.txt","w") as hello:
#     hello.writelines("My name is Nazeer \n Iam a independent men \n my mobile number is 7036260029")
# And finally we are at to delete the file for this we have to import the os module

import os

# if os.path.exists("MyDetails.txt"):
#     os.remove("MyDetails.txt")    ## it got deleted bcz it's present now it own't show
# else:
#     print(                          "The file doesn't Exist...!!!"
# os.remove("image.JPG")

## To remove the folder
# os.rmdir("for practice")   ## the folder gets removed yeyy


import csv

# with open("comma.csv","r") as file_data1:
    # csv.reader(file_data1)
    # csv_1=csv.reader(file_data1)
    # print(csv_1)      # here it wont give output
    # for i in csv_1:
    #     print(i)
    #     print(i[0])
    #     print(i[2])


# with open("excsv.csv","w") as file_data1:     # newnline="" is to remove the line gaps
#     csv_writer=csv.writer(file_data1)
#     csv_writer.writerow(["std_name","std_id","std_phnum"])
#     csv_writer.writerow(["Ramesh","1011","7799886655"])
#     csv_writer.writerow(["Suresh","1001","7764646445"])
#     csv_writer.writerows([["Ramesh","1011","7799886655"],["Suresh","1001","7764646445"],["Balesh","1121","8764866045"]])

# append is simelar to write 


# with open("comma.csv","a",newline="") as file_data1:     # newnline="" is to remove the line gaps
#     csv_writer=csv.writer(file_data1)
#     csv_writer.writerow(["std_name","std_id","std_phnum"])
#     csv_writer.writerow(["Ramesh","1011","7799886655"])
#     csv_writer.writerow(["Suresh","1001","7764646445"])
    # csv_writer.writerows([["Ramesh","1011","7799886655"],["Suresh","1001","7764646445"],["Balesh","1121","8764866045"]])


## we will work with some Jpg files

# x=open("myimage.JPG","rb")
# f1=open("image.JPG","wb")
# for i in x:
#     f1.write(i)
