
##                                                 RegEx functions :-

# re module defines maney functions
"""
The re module offers a set of functions that allowes us to search a string for a match 

   function                 Description
   
1. findall                returns a list containing all matches 
2. finditer               returns a iterator object
3. search                 returns a match object if there is a any match in the given string
4. sub                    replaces one or many matches with a string
5. match                  for matchings         

"""
# 1) findall():-
# EX1:- [] for a set of charactors 

import re
# str="Python supports dynamic datatype's"
# # find all lowercase alphabits between a-m
# x=re.findall("[a-m]",str)   ## returns all the characters avilable from a-m as list format check O/P
# print(x)
# print("\n")
# ## EX2:- \d any one digit
# ## find all the digital characeters from the given string

str="Virat kohli scored 145 runs out of 120 balls"
# x=re.findall("\d",str)   ## returns single digit charecters in a list format ['1', '4', '5', '1', '2', '0']
# print(x)

# x=re.findall("[0-9]",str)
# print(x)

# x=re.findall("\d{2}",str)  ##  returns double digit charecters in a list format ['14', '12']
# print(x)   ## or 

# x=re.findall("\d\d",str)
# print(x)  ## or 

# x=re.findall("[0-9][0-9]",str)  ## for two digit caharectors
# print(x)

# x=re.findall("[0-9]{2}",str)
# print(x)

# x=re.findall("\d{3}",str)    ## returns three digit charecters in a list format ['145','120']
# print(x)   ## or

# x=re.findall("[0-9][0-9][0-9]",str)
# print(x)

# x=re.findall("[0-9]{3}",str)
# print(x)

# x=re.findall("\d\d\d",str)
# print(x)

# x=re.findall("\d+",str)    ## for all digits
# print(x) 

# x=re.findall("\d[0-9]{2}",str)
# print(x)

""" Check if the string has any two-digit numbers, from 00 to 59: """

# txt = "8 times before 11:45 AM"
# x = re.findall("[0-9][0-9]", txt)
# print(x)
# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")

#######################################################################################################################
# ## Ex3:-   ^ ----> Starts with

# str="hello world "           ## check if the str start with 'hello'
# x=re.findall("^hello",str)  ## returns the word in list format i.e, ['hello']
# print(x)                    ## if not present returns empty list []

# x=re.findall("^hello",str)
# print(x,type(x),len(x),id(x))
# if(x):
#     print("Yes the string start's with 'hello' ")
# else:
#     print("the str not startin with the 'hello' word ")

#################################################################################################################
## EX4:- $ -----> Ends with

# str="Iam from Hyderabad and iam Mr Nazeer"
# x=re.findall("Nazeer$",str)          ## present and returs ['Nazeer']
# print(x)

# if x:
#     print("Yeyyy Nazeer")
# else:
#     print("No Nazeer")

###############################################################################################################
## EX5:- * zero or more accurances

# str="india is my country and in india all the religious are same and in india corona is in spreading everywhere"
# x=re.findall("in*",str)
# print(x)           ### ['in', 'i', 'i', 'in', 'in', 'i', 'i', 'i', 'in', 'in', 'i', 'i', 'in', 'in']
# if x:
#     print("Yes atleast one accurance")
# else:
#     print("No match")

###########################################################################################################
## EX6:- + one or more accurances

# str="The rain in spain falls mainly in the plain!"
# x=re.findall("ai+",str)   ## ['ai', 'ai', 'ai', 'ai']
# print(x)
# ## Extract the word which contain 'ai'
  
# x=re.findall("[a-zA-Z]+ai[a-zA-Z]",str)    ## ['rain', 'spain', 'main', 'plain']
# print(x)

# if x:
#     print("Yes atleast one accurance =",x)
# else:
#     print("No match")

########################################################################################################
## EX7:-  {m}  exactly specified number of accurances

# str="The rain in spain falls mainly in the plain!"
# x=re.findall("ai{1}",str)
# print(x)

# if x:
#     print("Yes atleast one accurance =",x)
# else:
#     print("No match")
#########################################################################################################
##EX8:- | : either this or that 

# str="python is easier than c language"
# ## findind weather str contains python or java
# x=re.findall("python|java",str)
# print(x)

# if x:
#     print("Yes atleast one accurance =",x)
# else:
#     print("No match")
########################################################################################################
## EX:- just check for reference 

# z=""" 101,Smith,100000
#     Blake,102,454500
#     30000,103,Miler """
# a=re.findall("\d{6}",z)
# print(a)
# a=re.findall("[a-zA-Z]{4}",z)
# print(a)
### ------------------------------------------------------------------------------------------4
#Check if the string starts with "The" and ends with "Spain":

# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)
# print(x)
# if x:
#   print("YES! We have a match!")
# else:
#   print("No match")
# ## --------------------------------------------------------------------------------------------
# txt = "The rain in Spain"
# ### Check if the string has any a, r, or n characters:
# x = re.findall("[arn]{2}", txt)
# print(x)
# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")

""" Extract only year from the following data """

data=""" 
1st World Cup held in the year 1975
2nd World Cup held in the year 1979
3rd World Cup held in the year 1983
4th World Cup held in the year 1987
5th World Cup held in the year 1992
1st World Cup held in the year 1996
# """
# hell=re.findall("\d{4}",data)
# print(hell)
# #OR
# hell=re.findall("\d\d\d\d",data)
# print(hell)
# #OR
# hell=re.findall("[0-9]{4}",data)
# print(hell)
# #OR
# hell=re.findall("[0-9][0-9][0-9][0-9]",data)
# print(hell)

""" I want all 1 digit,2 digit,3 digit no's """

# hell=re.findall("\d+",data)
# print(hell)

""" A pattern which can extract numericals and charecters """

# string="b,B,7,@,$,8,S,!"
# sub=re.findall("[a-zA-Z0-9]",string)
# print(sub)

""" Pattern which can print all the special symbols  """

# string="b,B,7,@,$,8,S,!"
# sub=re.findall("[^a-zA-Z0-9]",string)
# print(sub)

#OR

# string="b,B,7,@,$,8,S,!"
# sub=re.findall("\W",string)   ## 
# print(sub)

""" Pattern which can print all the special symbols excluding comma's """

# string="b,B,7,@,$,8,S,!"
# sub=re.findall("[^a-zA-Z0-9,]",string)
# print(sub)

"""  A prattern which can extract these string  """

# str1="Aug 15,Jan_26,Feb-14,Oct@2,2021,September,Sep30"
# x=re.findall("\w+",str1)
# print(x)

""" Pattern which can print only special symbols """
# str2="January2020,Feb@,#123,Super@@,209029!,Dec123"
# s=re.findall("\W",str2)
# print(s)

""" A pattern which can extract only $ """

# str2="January2020,$Feb@,#123,Super@@,209029$,Dec123,$"
# s=re.findall("[$]",str2)
# print(s)

""" A pattern which can extract $ along with associated numbers"""
# str2="January2020$,$Feb@,$123,Super@@,209029$,Dec123,$"
# x=re.findall("\d+[$]|[$]\d+",str2)
# print(x)

""" A pattern which can extract any number,uppercase,lowercase,specialsymbuls """
# x=re.findall(".+","9,b,bb,B,BB,+,*,++")
# print(x)

""" Extract only height of the persons from the following data """
# persons="""
# Sachin=5.4
# Virat=5.9
# Dohni=5.10
# Rohit=5.10
# Dhavan=5.8
# Rishab=5.7
# prethivi=5.4
# """
# a=re.findall("\d.\d+",persons)
# print(a)

""" Extract only weights of the persons from the following data """
persons="""
Sachin=65.4
Virat=62.9
Dohni=85.10
Rohit=80.10
Dhavan=65.8
Rishab=75.7
prethivi=65.4
"""
# v=re.findall("\d+.\d+",persons)
# print(v)

# #Return the domain type including .com or .in etc of given email-ids
# import re
# regex='@\w+.\w+'
# result=re.findall(regex,'Techm@gmail.com, osmania@ac.in, naresh@online.com, abc@rest.biz,naresh@yahoo.co.in') 
# print(result) 

"""Extract only scores from the following data and compute the total score """
# scorecard='''
# Dhawn=55
# Rohith=60
# Kohli=125
# Dhoni=25
# Hardik=15
# pant=5 '''

# x=re.findall("\d+",scorecard)
# print(x)

# scores=[]
# for p in x:
#     scores.append(int(p))
# print(scores)
# print("Total score=",sum(scores))

###---------------------------------------------------------------------------------------------------------------
# regex="[a-zA-Z]+ \d+" #, regex is a variable
# #+ indicates one or more occurance of a character, follwed by
# #one space,followed by 1 or more occurance of a digit.
# x=re.findall(regex,"June 15,August 9,Dec 12,May ,oct ,Feb 2020,2021")
# #findall is a fn for searching a given pattern in given string
# #it takes 2 parameters---> regex and string 
# #x is a list of matched strings
# print(x)
# for match in x:
#      print("Full match:",match)

#Note:if------> regex="[a-zA-Z]+ \d*"----->then May ,oct also will be extracted
###----------------------------------------------------------------------------------------------------------------

# import re
# regex="[a-zA-Z]+ \d+"  
# matches=re.findall(regex,"June 15,July 15,August 9,Dec 12,12 Feb") #12 Feb is invalid
# print(matches)
# for match in matches:
#      print("Full match",match)

###--------------------------------------------------------------------------------------------------------------


###---------------------------------------------------------------------------------------------------------

""" To capture DOB---->month and day """
# import re
# regex="[a-zA-Z]+ \d+" 
# x=re.findall(regex,"June 15th,August 9,Dec 12,Feb 22,jul ,hello ,chennai") #jul is invalid
# print(x)
# for match in x:
#      print("month:",match)
# print("\n")


""" II) #To capture  only month   """
# regex="([a-zA-Z]+) \d+" #it extracts only the pattern within parenthesis
# x=re.findall(regex,"June 15th hyd,August 9,Dec 12,Feb 22,jul ,hello,chennai") #jul is invalid
# print(x)
# for match in x:
#      print("month:",match)
# print("\n")
      
""" III) #To capture  only date but not month  """
# regex="[a-zA-Z]+ (\d+)" #it extracts only the pattern within parenthesis
# x=re.findall(regex,"June 15th,August 9,Dec 12,Feb 22,jul ,2020,2019") #jul is invalid
# print(x)
# for match in x:
#      print("Date:",match)
# print("\n")



# #ex:3
# data='''Miller DOB: June 15th,
# Blake DOB: August 9th
# Ajay DOB: Febrauary 21st
# Amar DOB: march 17th'''


# target_string = "Emma is a basketball player who was born on June 17, 1993. She played 112 matches with scoring average 26.12 points per game. Her weight is 51 kg."
# result = re.findall("\d+", target_string)

# # print all matches
# print("Found following matches")
# print(result)



""" Extract only  month and day """

# x=re.findall("[a-zA-Z]+ \d+",data)
# print(x)
# #or
# regex1="[a-zA-Z]+ \d+" 
# x=re.findall(regex1,data) 
# print(x)
# print("\n")

"""ex:4
extract only emp names now  """

# x=re.findall("([a-zA-Z]+) [a-zA-Z]+",data)
# print(x)
# #or
# x=re.findall("([a-zA-Z]+) [A-Z]+",data) 
# print(x)
# #or
# y=re.findall("(\w+) [A-Z]+",data) 
# print(y)
# #or
# x=re.findall("([a-zA-Z]+) DOB",data) 
# print(x)
# #or
# x=re.findall("(.+) DOB",data) 
# print(x)#


# #ex:5
# #extract only names and months
# data='''Miller DOB: June 15th,
# Blake DOB: August 9th,
# Ajay DOB: Febrauary 21st,
# Amar DOB: march 17th'''

# x=re.findall("[a-zA-Z]+ ",data) 
# print(x)
# #or
# regex2="(\w+) "
# y=re.findall(regex2,data)
# print(y)
# #or
# x=re.findall("([a-zA-Z]+) [A-Z:]+ ([a-zA-Z]+)",data) 
# print(x)

# #Extract only Miller and June
# x=re.findall("(Miller).+(June)",data) 
# print(x)

# x=re.findall("Miller |June",data) 
# print(x)


# #extract only---> DOB

# x=re.findall("([A-Z]+):",data) 
# print(x)

# #ex:6
# #Create a dictionary from the above data by extracting name as key and month as value
# #first create 2 lists-->names and months and merge those lists and convert to dictionary using zip() function

# #extract only emp names as one list

# #Extract names
# regex2="([a-zA-z]+) DOB"
# enames=re.findall(regex2,data)
# print(enames)

# #extract only months
# regex2=": ([a-zA-z]+)"
# months=re.findall(regex2,data)
# print(months)

# #Merging 2 lists using zip() function
# x=zip(enames,months)
# print(x,type(x))

# y=list(x)
# print(y,type(y))

# z=dict(y)
# print(z,type(z))

###---------------------------------------------------------------------------------------------------------------

""" Return the domain type of given email-ids """
# import re
# regex='@(\w+).\w+'
# result=re.findall(regex,'mahendra@gmail.com, osmania@ac.in, techm@online.com, abc@rest.biz,rajesh@yahoo.co.in') 
# print(result) 

#Return the domain type including .com or .in etc of given email-ids
# import re
# regex='@\w+.\w+'
# result=re.findall(regex,'Techm@gmail.com, osmania@ac.in, naresh@online.com, abc@rest.biz,naresh@yahoo.co.in') 
# print(result) 

#re.match():
#Validate a phone number: phone number must be of 10 digits and starts with 7 or 8 or 9
# import re
# x=['9983764321','7384963897','5376412769','938476182']
# for val in x:
#     if(re.match('[7-9]{1}[0-9]{9}',val) and len(val) == 10):
#         print('Valid')
#     else:
#         print('Invalid')

""" Check if the string starts with "python" and ends with "java": """

# txt = "python is easier and simpler than Java"
# x = re.search("^python.*Java$", txt)#. indicates any character,* indicates multiple occurences
# #print(x)
# if (x):
#   print("Matching")
# else:
#   print("No match")



#Extract--------->India from the following URL


# str="https://www.udemy.com/course/taming-big-data-with-apache-spark-hands-on/?gclid=CjwKCAjwztL2BRATEiwAvnALcvzxEh4uWqmuFRUHpPCGXxUQrjKUqwXGz-Sz3EUMdseUnkvc-dmcQBoCps4QAvD_BwE&matchtype=e&utm_campaign=LongTail_la.EN_cc.INDIA&utm_content=deal4584&utm_medium=udemyads&utm_source=adwords&utm_term=_._ag_84769215008_._ad_387461819747_._kw_apache+spark+tutorial_._de_c_._dm__._pl__._ti_kwd-346339260664_._li_9062114_._pd__._"
# res=re.findall(".*cc.([A-Z]+)&.*",str)
# print(res)

# #extract data b/w ----->/taming-big-data................/?
# res1=re.findall(".*/([a-z-]+)/?.*",str)
# print(res1)






""" finditer(): Returns a Iterator object which yields Match object for every match """

"""
But why use finditer()?

In some scenarios, the number of matches is high, and you could risk filling up your memory by loading them all using findall(). 
Instead of that using the finditer(), you can get all possible matches in the form of an iterator object, which will improve performance.

It means, finditer() returns a callable object which will load results in memory when called. Please refer to this Stackoverflow 
answer to get to know the performance benefits of iterators.

"""

# To print the start and end of the match

# import re
# regex="[a-zA-Z]+ \d+" 
# matches=re.finditer(regex,"June 15,August 9,Dec,Jan 31,Feb 21") 
""" finditer() returns iterator object
findall() returns list object,here list doesnt support start() and end() methods """
# print(matches)
# for match in matches:
#      print("match start index and end index:",match.start(),match.end())
