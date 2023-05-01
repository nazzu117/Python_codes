"""conversion of character to a number is called encoding, and the reverse process is decoding.
string is a sequence collection of a charector
each cheractor of a string is occured or ideantified by a unique index
strings can indicat by single or double coutes "",''
u can write 'hello' or "hello" """

# a="hello"
# print(a)
# print(type(a))

""" u can assign multiple stings at time """
# b= "Ramu is good and some times he is very bad boy,he can move and dance like dancing star"
# print(b)

""" trings slicing or indexing """
# a="Hyderabad is capital of Telanagana"
# print(len(a))
# print(a[0])
# print(a[2])
# print(a[-1])
# print(a[-10])
# print(a[0:11])
# print(a[5:14])
# print(a[-34:-10])
# print(a[-12:-1])
# print(a[0:12:2])
# print(a[-20:-1:2])
# print(a[::-1])
# print(a[:])
# print(a[::])
# print(a[12:0:-1])
# print(len(a))

""" Multiline string"""
# a=" hyderabad is the capital of telangana \
# there are so many IT companyees are located \
# im learning python to\
# became a Softwear employee "
# print(a)

# a=""" hyderabad is the capital of telangana 
# there are so many IT companyees are located 
# im learning python to
# became a Softwear employee """

# print(a)

# s = 'Hi\nHello'
# print(s)
#Let’s see how raw string helps us in treating backslash as a normal character.


# raw_s = r'Hi\nHello'
# print(raw_s)

""" String methods """
a="Hello world"

# print(a.upper())
# print(a.lower())
# print(a.replace("H","J"))
# print(a.replace("hellow","jai mahismathi"))
# print(a.split(" ,"))
# print(a[::-1])  #reversing the string 
# print(a *3)
# print("helloo" *4)

# txt="hyderabad is capital of telangana "
# print(txt.swapcase())  # changes the case upper to lower or lower to upper
# print(len(txt))
# txt= "       hyderabad is      surrounded by corona cases       so please be careful                 "
# b=txt.strip()
# print(b)
# print(len(b))
# x="hyderabad" in txt
# print(x)
# x1=" surr" not in txt 
# print(x)
# a1=""" nazzu is the great man all time right go head\n
# do what ever you want to do\n
# your are a crazy man rey dude"""
# print(a1)

# String concatination
# g="Hello"
# g1="nazzu"
# print(g+"  "+g1) 
# g2=g+" "+g1
# print(g2)
# x="heloo"
# y=10                  # its nbot possible bcz string and integer cannot conncatinate
# print(x+y)

""" Different was to concatination of str and int as follows """

# a=("hello")
# b=123
# print(a+str(b))

# ### using format@@@

# a = "Hello, I am in grade "
# b = 12
 
# print("{}{}".format(a, b))

# ## Using ‘%’ format specifier
# """While we can specify that both a and b are strings, 
# we can also use C-style format specifiers (%d, %s) to concatenate an integer with a string."""

# a = "Hello, I am in grade "
# b = 12
 
# print("%s%s" % (a, b))

# print("%s%s"%("HI","HELLO"))

# """Using f-strings
# We can use Python f-strings on Python 3.6 or above to concatenate an integer with a string."""

# a = "Hello, I am in grade "
# b = 12
# print(f"{a}{b}")

# """Printing the string using print()
# If we want to directly print the concatenated string, we can use print() to do the concatenation for us."""

# a = "Hello, I am in grade "
# b = 12
# print(a, b, sep="")

# stri="heloo world man abcd efgh ijk mnba"
# print(sorted(stri))


# #String formates we can add string and integer with this method:--
# age=25
# txt="hi..! iam nazeer and my age {}"
# print(txt.format(age))

# stg1="Hey"
# stg2="There"
# stg3="All"

# stg="{} {} {}".format(stg1,stg2,stg3)
# print(stg)

# quantity=10
# itemo=222
# price=5500
# tex="i want {} items of {} itemos for the price {}"
# print(tex.format(quantity,itemo,price)) 

# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
# print(myorder.format(quantity, itemno, price))


# string="heloo buddy how are you "
# print(string.upper())
# print(string.lower())
# print(string.index("h"))
# print(string.index("u"))
# print(string.find("d"))
# print(string.replace("buddy","nazzu"))

# n=" nazzu is tha fantastic man of all \"time\" in the nation is called safe right"
# n1=" nazzu is tha fantastic man of all time \\ in the nation is called safe right"
# n2=" nazzu is tha fantastic man of all time \n in the nation is called safe right"
# n3=" nazzu is tha fantastic man of all time  in the nation is called \r safe right "
# n4=" nazzu is tha fantastic man of all time\t in the nation is called safe right"
# print(n)
# print(n1)
# print(n2)
# print(n3)
# print(n4)


#Task--1

# a=input("Enter your string: ")
# b=input("Enter your charecter: ")


# count=0

# for i in a:
#     if b in a:
#         if i==b:  
#            count=count+1
# print(a.count(b))
# # print(count)

#  #Python Program to Replace all Occurrences of ‘a’ with $ in a String
# string=input("Enter the string: ")
# string=string.replace("A","$")
# string=string.replace("e","@")
# print("Modified string: ",string)

"""check weather two strings are anagram
An anagram of a string is another string that contains the same characters,
only the order of characters can be different. For example, “abcd” and “dabc” are an anagram of each other.
""" 



# s1=input("Enter the string: ")
# s2=input("Enter another string: ")

# if(sorted(s1)==sorted(s2)):
#     print("Yes anagram")
# else:
#     print("not anagarm")

# find no of vowels in a given string

# string=input("Enter the string: ")
# vowels=0

# for i in string:
#     if(i=="a" or i=="e" or i=="i" or i=="0" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U"):
#         vowels=vowels+1
# print("No of Vowels: ",vowels)

## find substring present in a given string

# n1=input("Enter the string: ")
# n2=input("Enter the sub string: ")

# if n2 in n1:
#     print("yes its there: ")
# else:
#     print("Try again")


## Python Program to Take in a String and Replace Every Blank Space with Hyphen
string=input("Enter string:")
string=string.replace(' ','-')
print("Modified string:")
print(string)



