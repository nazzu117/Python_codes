"""1.tuples are collection which is ORDERED and  UNCHANGABLE and indicated by () it is immutable
2. Tuple can contain any object means tuple allows both homgeneous(Same datatype) and heteronenious(Different datatypes) elements
      Homegeneous eg:- (10,20,11,44,55) or ("Python","Java","HYD","Hello")
      Heterogeneous eg:- (12,4.5,4+6j,"python")
3.tuple allows duplicate elements
4.in tuple insertion is preseverd ,i.e,the order in which elements are inserted in the same order they stored and displayed 
5.tuple allows duplicate elements eg:- [12,12,12,34,55,90,11,12,34]
tuples use mostly in security level bcz we cannot change the values bcz its immutable...
A tuple in Python is similar to a list. The difference between the two is that we cannot change the elements 
of a tuple once it is assigned whereas we can change the elements of a list
10.tuple can also be created by tuple() function
() is not mandentary..
Tuples are used to store multiple items in a single variable.

"""
# thistuple=()
# print(thistuple,len(thistuple),type(thistuple))

# thistuple=("banana","mango","apple","grape","guvva","jamun")  ## Homgeneous
# print(thistuple,type(thistuple),id(thistuple),len(thistuple))

# x=(10,15.5,"Python",3+1j)   ## Hetrogeneous tuple
# print(x,type(x),id(x),len(x))

# x=10,20,30,40
# print(x,type(x),id(x),len(x))     ## if () not there it will be tuple only by default

# citie="Hyderabad","Pune","Banglore","Mumbai","Delhi","Kolkata"
# print(citie,type(citie),id(x),len(citie))

# thistuple = ("apple",)
# print(type(thistuple))

#NOT a tuple
# thistuple = ("apple")
# print(type(thistuple))

# w=("python")                  ## this is not tuple single element takes as string only
# print(w,type(w),len(w))

# w=("python",)
# print(w,type(w),len(w))           ## this will takes as tuple

# w=(10)
# print(w,type(w))           ## same not a tuple
# w=(10,)
# print(w,type(w),len(w))

# x=([10,20,30,40,50])
# print(x,type(x),id(x),len(x))     ## this will takes as list only bcz its assumes as one member 

# x=([1,2,3,4,5],[5,4,3,2,1])
# print(x,type(x),id(x),len(x))
###############################################################################################################
""" Creation of tuple using tuple function  """
# x=tuple()
# print(x,type(x),id(x),len(x))
# x=tuple("Python")
# print(x,type(x),id(x),len(x))
# ##x=tuple("python","java")
# ##print(x,type(x),id(x),len(x))      ## Error bcz tuple function takes one element 2 given
# ##x=tuple(10)
# ##print(x,type(x),id(x),len(x))        ## Error bcz int is not iterable type
# x=tuple(["mumbai","Hyderabad"])
# print(x,type(x),id(x),len(x))
# ##x=tuple((10,20,2,3,,20,45))
# ##print(x,type(x),id(x),len(x))
# x=tuple({10,20,"Namaste","Rayudugaru"})
# print(x,type(x),id(x),len(x))        ## observe the output it's unordered
##############################################################################################################
""" Tuple slicing """
# thistuple=("banana","mango","apple","grape","guvva","jamun") 

# print(thistuple[0])
# print(thistuple[2:4])
# print(thistuple[1:5:2])
# print(thistuple[-1])
# print(thistuple[-5:-2])
# print(thistuple[-5:-3:-2])
# print(len(thistuple))
# ##print(thistuple[20])     ## IndexError: tuple index out of range
# print(thistuple[::])
# print(thistuple[0:20])    # this will prints hole list
# print(thistuple[::])
# print(thistuple[::2])
# print(thistuple[::-1])

###############################################################################################################

# tp=(12,[5,5],9,[4,6,8])
# tp[3][2]=90
# ###tp[2]=34    # it will give Error cz 'tuple' object does not support item assignment
# tp[1][1]=25   #However, item of mutable element can be changed
# print(tp)

# Once a tuple is created, you cannot change its values. Tuples are unchangeable, 
# or immutable as it also called.

# But there is a workaround. You can convert the tuple into a list, change the list,
#  and convert the list back into a tuple
# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)
# print(x)

# x=(9,10,5,66,12)
# y=list(x)
# y[3]=444
# x=tuple(y)
# print(y)z    

# my_tuple = (3, 4.6, "dog")
# print(my_tuple)   # Output: 3, 4.6, "dog" 

# # tuple unpacking is also possible
# a, b, c = my_tuple

# print(a)      # 3
# print(b)      # 4.6 
# print(c)      # dog 

# tuuple=("banana","hello","sapota")
# for x in tuuple:
#     print(x)
# print(len(tuuple))

# my_tuple=("hello",1,"bell","dell","HP")
# if "dell" in my_tuple:
#     print("dell is present and your aswome @@@@")


""" Tuples are unchangeable, so you cannot remove items from it, but you can delete the tuple completely:
#The del keyword can delete the tuple completely: """

# thistuple = ("apple", "banana", "cherry")
# del thistuple
# print(thistuple) #this will raise an error because the tuple no longer exists already deleted

""" Merging """
#Join Two Tuples
#To join two or more tuples you can use the + operator:
# Join two tuples:

# tuple1 = ("a", "b" , "c")
# tuple2 = (1, 2, 3)

# tuple3 = tuple1 + tuple2
# print(tuple3)

# x=(10,20,30);y=(40,50,60);z=([1,2,3])  
# z=x+y
# print(z,type(z),len(z))
# z1=x+y+z
# print(z1,type(z1),len(z1))   ## con't add look at z it's list

# fruits = ("apple", "banana", "cherry")
# mytuple = fruits * 2
# print(mytuple)

# print(dir(tuple))

# tuple1=(1,4,6,4,6,"nazzu",5,1,7,8,6,"nazzu")
# print(tuple1.count("nazzu"))
# print(tuple1.count(0))

# cricket=tuple([("bat","ball","stumps","helmet"),("wickert","caught","bowles","LBW","runout")])

# print(cricket[0][3])
# print(cricket[1][4])
# print(cricket[1][1])
# print(cricket[0][0])
# print(cricket[1][3])
# print(type(cricket))

# print((23,4,5,88)+(12,"python","Gabber"))
############################################################################################################
# x=(80,20,30,99,40,50,10,45)
# print(x,type(x),len(x))
# print(sum(x))
# print(max(x))
# print(min(x))
# print(sorted(x))
# print(reversed(x))
# print(x[::-1])
# print(sorted(x[::-1]))
# print(sorted(x[::-1],reverse=True))
## getting one by one value from the reveresed object using for loop

# for p in reversed(x):
#       print(p,end=" ")
# print("\n")
# for q in reversed(sorted(x)):
#       print(q,end=" ")
#############################################################################################################
# Tuple with in the tuple
# india=(("Kohli",145),("Rohit",112),("Dohni",50),("Dhawan",80),("Rishab",102),("KL Rahul",88))
# for i in india:
#       print(i)
# print(india)
# for a,b in india:
#       print("Player= ",a)
#       print("Scored= ",b)
##############################################################################################################
""" list as a tuple element """ 
# x=((1,2,3,4,5),(11,12,13,14,15),(20,21,22,23,24,25),[30,31,32,33,34,35,"pyhon"])
# print(x,type(x),len(x))
# print(x[0][2])
# ##x[0][2]=200    ## TypeError: 'tuple' object does not support item assignment
# ##print(x)
# x[3][0]="Hyderabad"      ## ['Hyderabad', 31, 32, 33, 34, 35, 'pyhon']
# print(x)                 ## This is valid bcz we are miodifing list element
# ##x[3]="Corona secound wave is high"    ## TypeError: 'tuple' object does not support item assignment
# ##print(x)   ## observe carefully x[3] is tuple element x[3][0 or 1 2 3 ] are list elements 

""" tuple as list element """
# x=[[1,2,3,4,5],[11,12,13,14,15],[20,21,22,23,24,25],(30,31,32,33,34,35,"pyhon")]
# print(x,type(x),len(x))
# x[0][3]="IPL is suspended due to corona "
# x[1][1]=000
# print(x)
# ##x[3][1]="Royal Challengers Banglore"   ## TypeError: 'tuple' object does not support item assignment
# ##print(x)    ## obeserve that we are accesing tuple element it's not posssible
# x[3]=["Indian Premium League"]
# print(x)        ## this is possible bcz we are accsing list element x[3] is list element but  not x[3][0,1,2,3....]
#####################################################################################################
""" Type casting """
# x=[10,2,12,5,8,1,0,88] 
# y=tuple(x);print(y),type(y)    ## List to tuple
# x=(10,2,12,5,8,1,0,88)   
# y=list(x);print(y),type(y)    ## tuple to list
# x="Hyderabad";print(x),type(x),len(x)
# y=tuple(x);print(y),type(y)     ## String to tuple
##x=10
##y=list(x);print(y),type(y)     ## TypeError: 'int' object is not iterable

## but in other way
# y=[x]
# print(y)


""" Unpacking a Tuple """ 
## When we create a tuple, we normally assign values to it. This is called "packing" a tuple:

# fruits = ("apple", "banana", "cherry")   # packing a tuple
# print(fruits)
# fruits = ("apple", "banana", "cherry")   ## tuple unpacking
# (green,yellow,red)=fruits
# print(green)
# print(yellow)
# print(red)

""" Using Asterisk*
If the number of variables is less than the number of values, you
can add an * to the variable name and the values will be assigned to the variable as a list:
# """
# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# (green, yellow, *red) = fruits
# print(green)
# print(yellow)
# print(red)

# fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
# (green, *tropic, red) = fruits
# print(green)
# print(tropic)
# print(red)