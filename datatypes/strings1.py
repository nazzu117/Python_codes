## String Functions.....

x="Hyderabad"
print(x)
print(type(x))
print(id(x))
print(x.upper())
print(x.lower())
print(x.capitalize()) # First letter capital
y="good morning hyderabad"
print(y.title()) ## All words first letter makes captals
names="ramu siva ramesh suresh venkat"
print(names.title())
## swapcase():For converting one case to another case if upper it will convert to lower ,if lower makes upper
s="HaPPY Birth day"
w="Java is easy and Java is simple"
print(s.swapcase())
print(s.replace("Birth","Marrage"))
print(s.replace("Birth","Barrage"))  ## replace(): will replace 
print(w.replace("Java","Python"))
string = "geeks for geeks geeks geeks geeks"  
print(string.replace("geeks", "Geeks")) 
# Prints the string by replacing only
# 3 occurrence of Geeks  
print(string.replace("geeks", "GeeksforGeeks", 3))

string = "geeks for geeks geeks geeks geeks"
print(string.replace("e", "o"))
# 3 occurrence of ek by o
print(string.replace("ek", "o", 3))

song = 'cold, cold heart'

# replacing 'cold' with 'hurt'
print(song.replace('cold', 'hurt'))

song = 'Let it be, let it be, let it be, let it be'

# replacing only two occurences of 'let'
print(song.replace('let', "don't let", 2))
# returns copy of the original string
print(song.replace('let', 'so', 0))

## strip(): for removing the blank spaces
a="     Nazeer   Basha is the good  boy  super      guy          "
print(len(a))
b=(a.strip())
print(len(b))
## split():- will plit and gives a string
x="GOOD MORNING HYDERABAD"
y=x.split(" ")  # Based on spaces
print(y)
print(type(y))
emp="101,David,Manager,255000" ## Split based on comma
y=(emp.split(","))
print(y[0])
print(y[3])
print(y[2])

## format():- for substractions
# #String formates we can add string and integer with this method:--
x="{} is the capitan of indian cricket team"
print(x.format("Virat kohli"))
y="{} is the {} of {}"
print(y.format("Delhi","Capital","India"))
a=("{},i'm Mr ".format("nazeer"))

my_string = "{}, is a {} science portal for {}"
print (my_string.format("GeeksforGeeks", "computer", "geeks"))
s=" Iam nazeer and my age is {}"
age=25
print(s.format(age))


## count():- to count the no of occurances of sub string of a character
x=" hello how are you hello man heloo hello"
print(x.count("hello"))
print(x.count("h"))



## find():- to check weather substring avilable or not, if avilable it returns first charactor of the
##          substring else it returs -1

x="python is easier than java"
print(x.find("java"))
print(x.find("Python"))


## String slicing: Extracting particular portion of a string
x="heloo Hyderabad"
print(x[2])
print(x[0:5])
print(x[0:9])
print(x[9:6]) ## gives a empty string caz slicing in forward direction
print(x[-9:-6]) ## -ve indexing
print(x[0])
print(x[:7])
print(x[5:])
print(x[:])
print(x[0:])
print(x[-9:9])
print(x[0:15:2])
print(x[0:15:3])
print(x[::-1])  # Reverse the string
## string functions:-
x="Happy Birthday Nazzu"
print(len(x))
print(max(x))
print(min(x))
print(x[:]+" Have a Great year") ## String concatination
print("Hai "+x[15:])
print(x*3)
print(2*x)
print("Nazzu"*4)
## in or not in functions:
print("Nazzu" in x)
print("Nazzu" not in x)
print("day" in x)
print("u" in x)
print(x.count("a"))

print("---------------------------------------")



""" complex datatypes: A complex number is comprised of 2 parts
1.imaginary
2.real part
"""
x=3+5j
print(x)
print(type(x))
print(id(x))
print(x.real)
print(x.imag)
## we can also creat complex numbers by using complex() function:
x=complex(4,5)
print(x)
print(complex(5,10))
print(complex(10))
print(complex())
print(complex('4-4j'))   # Observe the string
print(complex(2.2,3.5))
print("---------------------------------------")


