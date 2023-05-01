"""1.sets are set of collection which is unordered and unindexed and unique elements.
2.in python sets are written in curlry braces{}...
3.sets can contain any object means set allows both homgeneous{Same datatype} and heteronenious{Different datatypes} elements
      Homegeneous eg:- {10,20,11,44,55} or {"Python","Java","HYD","Hello"}
      Heterogeneous eg:- {12,4.5,4+6j,"python"}
4. Sets are unchangeable, meaning that we cannot change the items after the set has been created...
5.sets are unordered{Unordered means that the items in a set do not have a defined order.} 
  so we dont know in which ordered it will appired..
6. set were used where the order of data doesnt matter but the data elements to be unique.
7. You can't access items in a set by referring to an index, since sets are unordered the items has no index.
8. A set is an unordered collection of items. 
9. Every set element is unique (no duplicates) and must be immutable (cannot be changed)
10.we can perform mathemetical operations on sets objects lik,max,min,sorted.....
11.set within a set is not allowed bcz set allows only immutables.
12.in sets insertion is not pers erved i.e,the way they they are inserted in the same way they not stored and not displayed in the same manner

"""
# a={1,2,3,4,5,'abd',"bcd",7,6,"def"}     # create a set by 2 ways as showed
# b=set((2,3,4,'ssre',7,'srsrs'))
# print(a)
# print(type(a))
# print(b)
# print(type(b))
# # print(dir(a))
# c=set()
# print(c)
# print(dir(set))

# seet={"apple","heloo",[12,45,"apple"]}
# print(seet)                          # this will cause Error @@TypeError: unhashable type: 'list'

# a={}
# print(type(a))
##############################################################################################
""" creating set using set() function """
# a=set([1,2,3,4,5,6,1,12,4,10,5,6,11,12])
# print(a)
# print(len(a))
# print(type(a))
# s=set("python")
# print(s)
# print(len(s))
# b=set(("pythpon"))
# print(b)
# print(len(b))
# print(type(b))
# # c=set(1,2,3,4,5)    # this gives an error cz its expected one arguments 5 given
# # print(c)
# d=({"happy","Birth","day"})
# print(d)
# print(len(d))
# print(type(d))
# e={{1,2,3,4,5,6},{"hi","hello","Namaste"}}     ##TypeError: unhashable type: 'set'
# print(e)           ## set in side set is not allowed
######################################################################################################

# thisset = {"apple", "banana", "cherry"}
# print(thisset)
# thisset.update(["grape","mango","berry"])
# print(thisset)
# thisset.add("kalabanda")
# print(thisset)

# thisset = {"apple", "banana", "cherry"}
# thaiset={"kabalida","jammbalakadi","pamba"}
# for i in thisset:
#     print(i)
#     for j in thaiset:
#         print(j)
        
######################################################################################
# thisset = {"apple", "banana", "cherry"}
# if "banana" in thisset:
#     print("yes banana is in the set")
# else:
#     print("no banana avilable in the set check the set please")

# thatset={"kalada","balada","malada"}  # give's bulian values
# print("balada" in thatset)
# print(len(thatset))
# thatset.remove("kalada")
# print(thatset)
# thatset.discard("malada")  # remove and discard are both same use to remove item
# print(thatset)
# thatset.pop()    # pop will remove last item...Sets are unordered, so when using the pop() method, you will not know which item that gets removed
# thatset.clear()
# print(thatset)
# del thatset
# print(thatset)

# 1. Join two sets there are several ways to join 2 sets

# set1={"hii","heloo","hru","hdud"}
# set2={2,5,9,6}
# set3=set1.union(set2)
# print(set3)

# se1={1,2,3,4,1}
# se2={9,6,7,8,4}
# print(se1.union(se2))

# set1={"hii","heloo","hru","hdud"}
# set2={2,5,9,6}
# set1.update(set2)
# print(set1)

# thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
# print(thisset)

# sss=set([2,3,4,5,4])
# print(sss)

# my_set = {1.0, "Hello", (1, 2, 3)}
# print(my_set)

# sett={1,2,3,2,3,4,6,8,2,9,1,9,0,4}
# print(sett)            # sets do not allows duplicates.

# set=([1,2,3,4])   # we can make set from list 
# print(set)
# set={}
# print(type(set))

# threset={"kallada","ballada"}
# threset.discard("ballada")

# # x=threset.pop()
# # print(x)
# print(threset)

# my_set = set("HelloWorld")
# my_set=set("123456789")
# print(my_set)


# # initialize A and B   set UNION
# A = {1, 2, 3, 4, 5}
# B = {4, 5, 6, 7, 8}

# # use | operator
# # Output: {1, 2, 3, 4, 5, 6, 7, 8}
# print(A | B)

# # initialize A and B    #set INTERSECTION
# A = {1, 2, 3, 4, 5}
# B = {4, 5, 6, 7, 8}

# # use & operator      #set DIFFERENCE
# # Output: {4,5}
# print(A & B)

# # initialize A and B
# A = {1, 2, 3, 4, 5}
# B = {4, 5, 6, 7, 8}

# # use - operator on A
# # Output: {1, 2, 3}
# print(A - B)


# # initialize A and B         #SYMENTRIC DIFFERENCE
# A = {1, 2, 3, 4, 5}
# B = {4, 5, 6, 7, 8}

# # use ^ operator
# # Output: {1, 2, 3, 6, 7, 8}
# print(A ^ B)


# A = {1, 2, 3, 4, 5,"bac"}
# B = {4, 5, 1, 6, 7, 8,"bac"}
# C = {1,2,99,0,85,"bac"}
# print(A.union(B,C))
# print(A|B|C)
# print(A|B)
# print(A&B&C)
# print(A.intersection(B,C))
# print(A^B)
# print(A.difference(B,C))
# print(A-B-C)


# a={"heloo","marakala",2,8,5,"jamalakda"}
# b=frozenset(a)
# # print(b)
# b.add(6)
# print(b)            # this will through a error frozenset is immutable u cannot add elements
                    
################################################################################################# 
###################################################################################################
""" Searching for an element in set """
# x={10,20,30,40,50,40,10,90,100,50}
# print(x,id(x))
# print(20 in x)
# print(200 in x)
# print(10 not in x)
""" Working with set adresses
Note: ---> Mutable objects with same content -->Mutable objects will be created 
      ---> Immutable objects with same content -->one object will be created 
"""

# x={10,20,30,40,50}
# y={10,20,30,40,50}
# print(y,id(y))
# print(x is y)   # compares the address of the set 
# print(x is not y)
# print(x==y)        # compares the contenet set object

# x={10,20,30,40,60}
# print(x,id(x))
# print(x is x)
# print(x==x)

# x=set(("python"))
# y=set(("python"))
# print("x=",x)
# print("x=",x)
# print("y=",y)
# print("y=",y)
# print(x is y)
# print(x==y)

# a={1,2,3,4,5}
# print(a)
# b={1,2,3,4,5}
# print(b)
# print(a is b)
# print(a==b)

# m=20
# print(m,type(m))

# p=100,200,300,400
# print(p)
# print(type(p))

# x={1,2,3,4,5}
# a,b,c,d,e=x
# print(a,b,c,d,e)
# print(e)
# m=[10,20,30,40,50]
# x1,x2,x3,x4,x5=m
# print(x1,x2,x3,x4,x5)
# print(type(m))

# s1=10;s2=20;s3=30;s4=60;s5=70
# p=s1,s2,s3,s4,s5
# print(p,type(p))

# s1,s2,s3,s4=1,2,8,9
# print(s1,type(s1))
# print(s2,type(s2))
# print(s3,type(s3))
# print(s4,type(s4))

# s1,s2,s3,s4,s5=[1,2,8.8,9,12]
# print(s1,s2,s3,s4,s5)
# print(s1,type(s1))
# print(s2,type(s2))
# print(s3,type(s3))

# s1=s2=s3=s4=s5=[1,2,8.8,9,12]
# print(s1,s2,s3,s4,s5)
# print(s1,s2,s3,s4,s5)
# print(s1,type(s1),len(s1))
# print(s2,type(s2),len(s2))
# print(s3,type(s3))

# x={[10,20,30],[40,50,60],[70,80,90]}
# print(x)             ## TypeError: unhashable type: 'list' bcz we can't have list as set elements


