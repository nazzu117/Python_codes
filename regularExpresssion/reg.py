# A regular Express ,is a sequence of charecters that forms a search pattern
# RE used to check if a string contains specified search pattern
# use import re



#search
#findall
#Declaring the formate is very important
#ReEx will work only on strings

# symbols--
#--> /d =digits
#--> /w =alphanumeric
#--> {} = specifing the length

# #declaring the pattern formate...

import re

pattern="\d{3} \d{3}-{4}"
a="7799219933 This is my number 7036260029 "

heloo=re.search(pattern,a)
print(heloo)

# import re
# find=re.findall("inform","we have to inform him with the latest information")
# print(find)
# for i in find:
#     print(i)

# str= "we need to inform him with the latest information"

# for i in re.finditer("inform",str):             # find iterator = generats starting and ending index of the matching object
#     locktup=i.span()
#     print(locktup)

# str="sat,mat,bat,rat,bat,cat,fat,pat,rot,rait,hat"
# allstr=re.findall("[shmp]at",str)     # consider only stsrt with s,h,m,p
# for i in allstr:
#     print(i)

# print("--------------------------")

# str="sat,mat,bat,rat,bat,cat,fat,rot,rait"
# allstr=re.findall("[a-z]at",str)   # will consider range a-z stsrting letter
# for i in allstr:
#     print(i)

# str= "het,bet,set,met,net,let,ket,oet"
# allstr = re.findall("[^m-z]et",str)  # ^ carrot symbol not allows the specificed rand i.e,prints remain all
# for i in allstr:

#     print(i)


# replace the string 
# food="rat cat mat fat"
# regex=re.compile("[m]at")
# food=regex.sub("food",food)
# print(food)

# food="chicken,soup,motton,birayani"
# rege=re.compile("[s]oup")
# food=rege.sub("chilli chicken",food)
# print(food)


# a="heloo \\world wakeup"
# b=re.search(r"\\world",a)    # to print double slaces\\
# print(b)
