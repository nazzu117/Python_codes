"""
1. List is a collection which is ordered and changeable. Allows duplicate members
2. List can contain any object means list allows both homgeneous[Same datatype] and heteronenious[Different datatypes] elements
      Homegeneous eg:- [10,20,11,44,55] or ["Python","Java","HYD","Hello"]
      Heterogeneous eg:- [12,4.5,4+6j,"python"]
3. List can grow and shrink automatically
4. List are dynamic that simply means,there is no limit of objects we can store/add to the list
5. In Python lists are written with square brackets []
6. list allows duplicate elements eg:- [12,12,12,34,55,90,11,12,34]
7. in list insertion is preseverd ,i.e,the order in which elements are inserted in the same order they stored and displayed 
8. List is one of the most frequently used and very versatile data types used in Python.
9. List is mutable that means changes and modifications are allwed but elements of list either mutable or immutable
10. List can also be created by list() function

"""
# how to creat a list  
# empty list 

# my_list = []
# print(my_list)
# print(type(my_list))
# print(id(my_list))

# list of integers

my_list = [1,2,3,5,7,8,9,12,5]
print(my_list)
print(my_list[0],type(my_list[1]),id(my_list))
# print("Length= ",len(my_list))
# print("Sum= ",sum(my_list))
# print("Max",max(my_list))
# print("Min=",min(my_list))
# avg=(sum(my_list))/len(my_list)
# print("Avg= ",avg)
# print(sorted(my_list))
# print(sorted(my_list,reverse=True))
# print(my_list[::-1])

# for i in reversed(sorted(my_list)):
#     print(i,end=" ")
    
"""Reversing a list using reverse() """
# def Reverse(lst):
#     lst.reverse()
#     return lst
      
# lst = [10, 11, 12, 13, 14, 15]
# print(Reverse(lst))

""" list with mixed data types """

# my_list = [1, "Hello", 3.4,4+8j]
# print(my_list)

"""A list can also have another list as an item. This is called a nested list."""

# nested list
# my_list = ["mouse", [8, 4, 6], ['a']]
# print(my_list)

# mylist=["Apple","Banana","Cherry","Berry","Mango","Tango"]
# print(mylist)
"""                                       ...LIST METHODS...                               """
# print(mylist[0])
# print(mylist[0:4])
# print(mylist[0:5:2])
# print(mylist[-5:-3])      # -3 excluded and -5 included
# print(mylist[:])
# print(mylist[:5]) #This example returns the items from the beginning to till the numer
# print(mylist[4:]) #By leaving out the end value, the range will go on to the end of the list:
# mylist.append("kanana")
# print(mylist)
# print(mylist[:])
# print(mylist[ : ])         # Threee are same
# print(mylist)
#------------------------------------------------------------------------------------------------------------------------  
# a=[1,3,5,7,9,11,13,15,17,19];print(a[1:5],a[3:17],len(a))    #[3, 5, 7, 9] [7, 9, 11, 13, 15, 17, 19]
# x=[12,2,3,4,2,3,3,3,32,3,3,3,3,3]
# print(len(x))
# print(x[2:45])
# x="Ravana samharam"
# print(x[0:33])
# #NOTE: in list index u can use any number even grater element will prints to last one
#----------------------------------------------------------------------------------------------------------------------
# Heterogeneous listt
x=[12,"Nazeer","Basha",3.5,5+6j]
# print(x,type(x),id(x))
# print(len(x))
# print(x[2][1])
# print(x[1][4])
# for i in x:
#     print(i)
# for i in x:
#     print("Hello") 

# colors = ['red', 'blue', 'green']
# print(colors[0])    ## red
# print(colors[2])   ## green
# print(len(colors))  ## 3 
         

# will work on some list adresses
# x=[10,20,30,40,50,60]
# y=[10,20,30,40,50,60]
# print(x[0],type(x[0]),id(x[0]))
# print(y[0],type(y[0]),id(y[0]))
# print(x[3],type(x[3]),id(x[3]))
# print(y[3],type(y[3]),id(y[3]))
##-----------------------------------------------------------------------------------------------------------------

# Different ways to create a list
# by using list function ie.,

# x=list();print(x,type(x),id(x),len(x))
# x=list("Python");print(x,type(x),id(x),len(x))
# #x=list("Python","Java");print(x,len(x))        ## TypeError: list expected at most 1 argument, got 2 i.e,.list function accepts only one arguments
# # Should be of iterable type like str,list,tuple,set
# # x=list(10); print(x)   # same error,  TypeError: 'int' object is not iterable
# x=list(["Python","Java","Ruby"]);print(x,type(x),len(x))
# x=list([10,3,4,65,9,2,5]); print(x,type(x))
# x=list(["Python","Java"]);print(x,len(x))
# X=list({10,3,4,6,4,6});print(x,len(x))
# X=((12,20,5,8,22));print(x,len(x))
# thislist1 = list(("apple", "banana", "cherry")) # note the double round-brackets
# print(thislist1)

##########################################################################################################
""" Nested list  """

#I want to create a matrix which looks like below:

matrix = [[0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4]]

# print(matrix)
# print(matrix[0],type(matrix[0]),id(matrix[0]))
# print(matrix[2],type(matrix[2]),id(matrix[2]))
# print(matrix[3],type(matrix[3]),id(matrix[3]))

# # printing all the sublists using for loop
# for i in matrix:
#       print(i)

# printing all the elements in each sub list

# for i in matrix:
#       for j in matrix:
#             print(j)

# combind all the sub lists into one

# matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
# mat=[]

# for i in matrix:
#       for j in i:
#             mat.append(j)
# print(mat)


# x=[[1,2,3,4,5,6],
# [12,13,14,15,16],
# [2,6,7,8,9,2,1,1]
# ]
# print(x)
# for j in x:
#       print(j)
##########################################################################################

""" Assicing the list elements """

# emps=[[101,"Nazeer","Manager",123459.88,"Developer"],
#       [102,"Jack","Assistent Engineer",71234.98,"Backend"],
#       [103,"Black","Engineer",60234.98,"Backend"]
# ]
# print(emps)
# print(emps[0])
# print(emps[2])
# print(emps[1][2])
# print(emps[0][2])

""" Now modifing list elements"""
# emps[0][3]=200000
# emps[0][2]="CEO"
# emps[1][3]=90000
# print(emps[0])
# print(emps[2])
#########################################################################################################
# x=[[1,2,3,4,5,6],
#    [12,13,14,15,16],
#    [2,6,7,8,9,2,1,1]
# ]
# print(x)
# x[0][3]="Python"
# x[2][4]=123
# x[1][4]="Raman"
# print(x)
# for i in x:
#       print(i)

# a=["apple ","banana","tunana","jainana"]  # change item value
# a[1]="sakragula"
# print(a)
#############################################################################################################

""" LIST METHODS """
##                                Add item : append
# x=[10,20,30,40]
# x.append(25)
# print(x)

# print(x.append(10))
# # x.append(12,13)       # Error bcz TypeError: list.append() takes exactly one argument (2 given)
# x.append([12,13])       # this is valid cz 

# x.extend((123,345))
# print(x)
# x.append("Nazeer")
# print(x)
# mylist=["ajay","ashok","shiva","prasad","suresh","shashi","nazeer","nazeer","nazeer"]
# mylist.append("bose")
# print(mylist)

# ## using for loop and append method appinding multiple values
# x=[10,20,30,40,50]
# for i in [12,13,14]:
#       x.append(i)
# print(x) 

# y=[12,3,4,5,6,9,7,0]
# z=[1,2,3,4,5,6,7]
# for i in z:
#       y.append(i)
# print(y)

# extend method() use to extend the elements of other list
# x=[10,12,"python","red",15+3j]
# y=["Nazzu",12,9,34.45]
# x.extend(y)
# print(x)

# thislist = ["apple", "banana", "cherry"]
# thislist.extend(["sambarrice","curdrice","lemonrice"])  # observe we added list as one 
# thatlist=[12,33,55,78,90]
# thislist.extend(thatlist)
# print(thislist)

# # thislist.extend("sambarrice","curdrice","lemonrice")    #TypeError: list.extend() takes exactly one argument (3 given)
# # print(thislist)

# mylist=["ajay","ashok","shiva","Srasad","suresh","shashi","nazeer","nazeer","nazeer"]
# mylist.extend(["sambarrice","curdrice","lemonrice"])
# print(mylist)



# list11=[1,2,3,4]
# list22=["a","b","c","d"]      # use extend method to combined lists
# list22.extend(list11)
# print(list22)

""" insert(index,value) for inserting elementys at desired position """

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2,"Sapota")
# print(thislist)
# thislist.insert(0,"berry")
# print(thislist)
# thislist = ["apple", "banana", "cherry"]  #add item at specific location : insert
# thislist.insert(2,"water apple")
# print(thislist)
# mylist=["ajay","ashok","shiva","Sprasad","suresh","shashi","nazeer","nazeer","nazeer"]
# mylist.insert(7,"samantha")
# mylist.insert(0,"hii")
# print(mylist)

""" pop(index): to remove specific item from lis if we won't mention index it will pop last element in the list """

# thislist.pop() # want to remove specific element :pop(index value),pop(2) etc....
# print(thislist)
#  mylist=["ajay","ashok","shiva","prasad","suresh","shashi","nazeer","nazeer","nazeer"]
# mylist.pop(3)
# print(mylist)
# print(len(mylist))
# thislist.remove("cherry")  # want to remove use:remove 
# print(thislist)

""" Delete multiple elements from the list """

# x=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
# del x[4:12]
# print(x)

## remove(): removes a particular value
# mylist=["hii","heloo","namaste","bye","auper","hehe"]
# mylist.remove("hii")
# print(mylist)
# let=[10,20,30,20,40,20,50,20]
# let.remove(20)
# print(let)      ## Removes first occurance of 20
# llist=[10,20,30,45,65,34,5,7]
# for i in [20,45,65]:
#       llist.remove(i)
# print(llist)

## index() : to the indexing of particular element
# mylist=["ajay","ashok","shiva","prasad","suresh","shashi","nazeer","nazeer","nazeer"]
# print(mylist.index("nazeer"))
# print(mylist.count("nazeer"))
# mylist.reverse()
# print(mylist)
# my_list = [3, 8, 1, 6, 0, 8, 4]
# print(my_list.index(8))    # index value
# print(my_list.count(8))    # no of 8 present

# yourlist=["orey","sattiga","ittdippdde","attele"]
# del yourlist[1] # delete a specific item
# print(yourlist)
# del yourlist  # delete total list
# print(yourlist) # out put as error becz its already deleted/its empty now


# llist=["jamakaya","vankaya","bendakaya","kakarakaya",3,55,7]
# for i in llist:
#     print(i)

# theirlist=["neeli","aakasam","iddam","anukunna"]
# theirlist.clear()     ## clears the list and returns a empty list[]
# print(theirlist)
# theirlist.clear(1)   ## TypeError: list.clear() takes no arguments (1 given)
# print(theirlist)
                                #Adding lists
# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]
# list3=list1+list2
# print(list3)


# my_list = [1, 3, "Michele", [5, 6, 7]]
# for element in my_list:
#   print(element)

# a=["apple",2,5,"banana",["Divya","dama",6,8,5,3+8j],4,"nazzu"]
# print(a[4])
# print(len(a))                      
# print(a[4][0][0])             # Nested indexing
# print(a[4][0])

# odd = [1, 3, 5]
# print(odd + [9, 7, 5])

# my_list = [3, 8, 1, 6, 0, 8, 4]
# print(my_list.index(8))
# print(my_list.count(8))

# my_list.sort()
# print(my_list)

# my_list.reverse()
# print(my_list)

                                #List comprehensions

# when using list comprehensions, list can be built by leveraging any ITERABLE,incuding strings and tuples.
# Remember, every list comprehension written in loop,but every loop cant be rewritten in the form of list comprehension  
# every list comprehension in python includes three elements ECPRESSION < VARIABLE < ITERABLE

# thislist=["aakali","bakali","kakali","tukali"]
# for x in thislist:
#     print(x)

# mylist=["sambar","curd","curry","chicken"]       # copy list
# yourlist=mylist.copy()
# print(yourlist)
# print(mylist)

# thislist = ["apple", "banana", "cherry"]        # 2nd method for copy a list
# mylist = list(thislist)
# print(mylist)

# ourlist=["samja","varagmana","ninnu","chusi","aagagalana"]
# if "samja" in ourlist:
#     print("yes it is exist")

# list1=[1,2,3,4]
# list2=["a","b","c","d"]
# for x in list2:
#     list1.append(x)
# print(list1)
# print(list1+list2)


# print(["re"] * 3)
# print([20*5]+[10])

# nums = [1, 2, 3, 4]
# squares = [ n * n for n in nums ]      # output [1,4,9,16]
# print(squares)

# pow2 = [2 ** x for x in range(10)]
# print(pow2)

# pow1=[2**x for x in range(10,20)]
# print(pow1)

# pow2 = []                # similer code for above code
# for x in range(10):
#    pow2.append(2 ** x)

# num=[12,23,3,6,8,45,9]
# squr1=[n*n for n in num]
# squr2=[n*10 for n in num]
# squr3=[n**3 for n in num]
# print(squr1)
# print(squr2)
# print(squr3)



# llisrr=["ramesh","suresh","mahesh","somesh"]
# name=input("Enter name: ")
# if name in llisrr:
#     print("name is exist he is enrolled thank you")


# l=[12,1,34,6,4,8,90,22,18,3,30]
# # print(min(l))
# # print(max(l))
# # l.sort()
# # print(l)
# l.reverse
# print(l)

# hi=["heloo","below","bottom"]
# a=[x.upper() for x in hi]
# print(a)


# print(dir(list))

# list=[1,2,3,5,6,7,8,9]
# del list[-3:-6:-1]
# print(list)

# squares = [1, 4, 9, 16]
# sum = 0
# for x in squares:
#     sum+=x
# print(sum)

llist=[ [1, 2, 3, 4, 5],[11, 22, 33, 44, 55],[17, 18, 19, 20, 21] ]