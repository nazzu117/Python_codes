# Python programe to Add a Key-Value Pair to the Dictionary 

# currency={
#     "India":"Rupees",
#     "USA":"Doller",
#     "UAE":"Deenars",
#     "Australia":"Australian dollar",
#     "Brazil":"Real"
# }
# print(currency)
# currency.update({"China":"Chinese yuan"})
# print(currency)

# OR

# key=(input("Enter the key (int) to be added:"))
# value=(input("Enter the value for the key to be added:"))
# currency.update({key:value})
# print(currency)

#OR

# key=int(input("Enter the key (int) to be added:"))
# value=int(input("Enter the value for the key to be added:"))
# d={}
# d.update({key:value})
# print("Updated dictionary is:",d)

# """Python Program to Concatenate Two Dictionaries Into One"""
# hi={"a:":1,"b":2,"c":3}
# heloo={"d":4,"e":6}
# hi.update(heloo)
# print(hi)
# print(heloo)

""" Python Program to Check if a Given Key Exists in a Dictionary or Not """

# currency={
#     "India":"Rupees",
#     "USA":"Doller",
#     "UAE":"Deenars",
#     "Australia":"Australian dollar",
#     "Brazil":"Real"
# }

# key=input("enter the key to check:")
# if key in currency.keys():
#     print("Yes it's present:",currency[key])
# else:
#     ("it's not presente...")

""" Python Program to Generate a Dictionary that Contains Numbers (between 1 and n) in the Form (x,x*x). """

# n=int(input("Enter the number"))
# d={x:x*x for x in range(1,n+1) }
# print(d)

""" Python Program to Sum All the Items in a Dictionary """

# dit={"a":123,"b":456,"c":789}
# print("Sum of all the valuesn in the dictionaer:",sum(dit.values()))

""" Python Program to Multiply All the Items in a Dictionary """

# d={"a":123,"b":456,"c":789,"d":987,"e":567}
# total=1
# for i in d:
#     total=total*d[i]
# print(total) 

