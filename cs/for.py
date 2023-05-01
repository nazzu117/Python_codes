# for loop is only works on sequence...
# for loop depands upon defination of datatypes...

# a="python is a programmeing language"
# for  i in a:
#     print(i,end="")

# b=[23,45,44.4,3.4,'python','nazzu']
# for i in b:
#     print(i)  

# for x in "Banana","Apple","Sapota":        # looping through "strings"
#     print(x, end="      ")

#To square each element of a list

# x=[10,20,30,40,50]

# for p in x:
#     print(p*p)

#######################################################################################################    
#Applying for loop on a string
# x="python"
# for p in x:
#     print(p)

# #Ex:2
# #printing each character for 3 times

# for p in x:
#     print(p*3)

# #Ex:3
# #Printing a msg for multiple times using for loop
# for p in x:
#     print("Good Morning!!!")
#######################################################################################################

#Program to find the sum of the list elements

# x=[10,20,30,40,50]
# sum=0
# for p in x:
#     sum=sum+p
# print("sum=",sum)

###########################################################################################################

#will work on range function

# for i in range(12,56): # it ill show the range between these numbers
#     print(i)

# for i in range(0,50,5): #(1,50,5) indicates that the variation between 1-50 as 5 , check out put...
#      print(i,end=",")   # end is used for result in same line like 1 2 3 4 5 6 ....

# for i in range(100,10,-1): # using -ve elemente for desinding order otherwise it move forwerd
#      print(i,end=" ")

# for i in range (0,100):
#     if i%6==0:
#         print(i,end=" " )

# def fun():
#     for i in range(22,23,24):       ## Nothing will print.
#         print(i)

#printing a msg for 100 times

# for p in range(100):
#     print("Good Morning!!!")

## printing message for 100 times
# num=0
# for i in range(101):
#     num=num+1                          ## know how many time it's printing
#     print(num,".","I Love You...")

#printing only odd No's from 0 to 100

# for p in range(1,101,2):
#     print(p)

#printing only even No's from 0 to 100

# for p in range(0,100,2):
#     print(p)

#Program to find the multipication table of a number

# n=int(input("Enter value of n:"))
# print("Multiplication Table is:")
# for p in range(1,11):
#     print(n,'x',p,'=',n*p)
#########################################################################################################
# for i in range(1,6):       
#     for j in range(1,6):
#         print(i,end=" ")
#     print()

# print("\n")
# #ex:2
# for i in range(1,6):       
#     for j in range(1,6):
#         print(j,end=" ")
#     print()

# print("\n")
# #Ex:3
# for i in range(1,6):       
#     for j in range(1,6):
#         print("*",end=" ")
#     print()



######################################################################################################

# Lets work on break statement

# l=["Apple","Banana","Graps","chagala","bagala","helooworld"]
# for i in l:
#     #print(i)
#     if i=="bagala":
#         break
# print(i)

# l=["Apple","Banana","Graps","chagala","bagala","helooworld"]
# for i in l:
#     if i=="Banana":
#         break
# print(i)

# l=["Apple","Banana","Graps","chagala","bagala","helooworld"]
# for i in l:
#     print(i)
#     if i=="bagala":
#         continue

# l=["Apple","Banana","Graps","chagala","bagala","helooworld"]
# for i in l:
#     if i=="Apple":
#         continue
#     print(i)

# for val in 'string':
#     if val=="i":
#        continue
#     print(val)

# print("the end")

# for i in range (0,600,10):
#     print(i,end=" ")


# for x in range (6):
#     print(x)
# else:
#     print("finally finished")

"""To force this function to output all the items, we can use the function list().

The following example will clarify this."""

# print(range(10))

# print(list(range(10)))

# print(list(range(2, 8)))

# print(list(range(2, 20, 3)))


# fruits=["apple","banana","mango"]
# natur=["big","sweet","tasty"]
# for i in fruits:
#     for j in natur:
#         print(i,j)


# 

# numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

# # variable to store the sum
# sum = 0
# # iterate over the list
# for val in numbers:
# 	sum = sum+val
# # Output: The sum is 48
# print("The sum is", sum)
