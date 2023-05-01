"""
1.Dictionary is collection datatype which holds groupv of key:value pairs
     Ex:- x={"Name"="Supen Women","Age"=34}
2.Dictionary is a collection which is unordered ,changable and indexed. In python dictionarys are written with curley \n
     braces '{}' and they have keys and values
3.keys and values can be either homogious or heterogenious
4.keys can't duplicate but values can be Ex:- "age"=55,weight=55
5.Insercetion order is not preserved
6.Indexing and slicing is not supporting
7.Dictionaries are mutable objects:
    with in a dictionary we can have mutable and immutable object
8.Dictionary can be created by {} or dict() function
9.dictionarys allows duplicates it will considered latest one like if u gave barand name twice it will consider latest one
10.keys only immutable...
11.to access elements of dictionary pass the key and we will get value
12.It stored values like a map,contails key value pairs unlike other datatypes,
13.simelar to realife dictonarys with distint key values.
"""

""" Different ways to create dictionaries """

# player={"Virat Kohli":125,"Rohit":80,"KL Rahul":110,"Rishab Pant":54,"Hardik Pandya":40}  ## Homogeneous keys(String type),Homogeneous values(int type)
# print(player)
# print(type(player))
# print(len(player))

# emp={"emp_Name":"Stuat Broad","emp_Id":101,"Salary":120500.78,"Designation":"Engineer Automation"}  ## Heterogenious type 
# print(emp)
# print(type(emp))
# print(len(emp))

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
#              }
# print(thisdict)

# z={
# "CSE":120,  ## the duplicate one gets removed
# "ECE":120,
# "EEE":60,
# "CIVIL":60,
# "IT":60,
# "CSE":60
# }
# print(z)
# print(type(z))
# print(len(z))

# this={"x":100,"y":200,"z":300,"y":700,"x":1000}
# print(this)
# print(len(this))

## Accising the elements from Dictionary
# x={"x":10,"y":12,"z":20,"w":33}
# print(x,type(x),len(x))
# print(x['x'])
# print(x['y'])  ## if we pass the key will get the value
# print(x['w'])

# details={"name":"Nazeer","age":26,"height":5.8}
# print(details,len(details))
# print(details["name"])
# print(details["age"])
# print(details["height"])

# thisdict =	{
#   "brand": "F6ord",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict["brand"]    # we can get element like as shown
# print(x)

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict.get("model")  # we can use get method to get a required element
# print(x)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["model"]="Jai mahishmathi"  #change the item value
# thisdict["brand"]="mahishmathi"
# thisdict["year"]=2017
# print(thisdict)
# print(thisdict.values())
# print(thisdict.keys())


### looping through Dictnories
# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# if "model" in thisdict:
#   print("yeyy its there in the Dictinoriy")

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x in thisdict:           # all keys 
#     print(x)
# for x in thisdict.values():
#   print(x)

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x in thisdict:             # for all values
#   print(thisdict[x])

# details={"name":"Ramesh","age":33,"height":5.10}
# for i in details:
#     print(i)       ## it will prints only keys

# for p in details:
#     print(details[p])    ## for printing values
  
# for s in details:
#     print(s,":",details[s])
#     print(s,":",details[s],sep="")   ## if space not required

# print(details["age"],type(details["age"]))   

# # loop through both items by using item() function

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(len(thisdict))   # length of dictionary
# for x,y in thisdict.items():  # both keys and values
#   print(x,y)

""" Another way of creating dictionary """
# a={}
# print(a,type(a),len(a))
# a={10,20}
# print(a,type(a),len(a))
# a={"a":1,"b":2,"c":3}
# print(a,type(a),len(a))

# ## dict() function
# a=dict()
# print(a,type(a),len(a))

# d={"rank":23}
# print(d,type(d),len(d),id(d))

# c=dict(d)
# print(c,type(c),len(c),id(c))  ## passing dictionary as a parameter
# print(c,type(c),len(c),id(c))

# e=d
# print(e,type(e),len(c),id(e))
# print(d,type(d),len(d),id(d))

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["colour"]="Matt black"
# thisdict["varient"]="Petrol"
# print(thisdict)


# # remove item

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.pop("model")
# print(thisdict)


# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["colour"]="Matt black"
# thisdict["varient"]="Petrol"
# thisdict.popitem()     # a random item is removed
# print(thisdict)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del thisdict["model"]
# print(thisdict)


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del thisdict
# print(thisdict)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.clear()
# print(thisdict)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# a=thisdict.copy()   # copy a dictionary
# print(thisdict)
# print(a)
""" Create dictionary by using formkeys """

# marks = {}.fromkeys(['Math','English','Science'], 100)  # fromkeys helps u to creat dictionarys in dynamic way
# print(marks)

# for item in marks.items():
#     print(item)

# a={"mail","pswd","user","city"}
# print({}.fromkeys(a))
# print({}.fromkeys(a,"nazzu"))

# # OR

# a={"mail","pswd","use","city"}
# b={}
# for j in a:
#   b[j]=None
# print(b)


# data={1:"nazeer",2:"arkala",3:"samarala",5:"mrakala"}
# print(data.get(1))      # it will give the value at key 1
# print(data.get(4),"not found")   # it will not found through the error\not found
# print(data.get(3,"not found"))     # here we have key 3 value that will return samarala
# print(data)

# keys=["naveen","kiran","mahesh","ramesh","suma"]
# values=["python","java","c","c++","DataScence"]           #we can convert 2 lists into a dictionary 
# data=dict(zip(keys,values))
# print(data)
# print(data["naveen"])        

# a=["Maths","English","Science","Hindi","Social"]
# b=[100,99,96,89,92]
# c=dict(zip(a,b))
# print(c)


# a={"name":"ramesh","age":33,"gender":"male"}
# b={"place":"andhrapradesh","ocupation":"doctor"}
# print(a)
# a.update(b)
# print(a)

# a={1:"Hyderabad",2:"Secundrabad",3:"Delhi",4:"Mumbai",5:"Kolkatta"}
# b={"a":"India","b":"United States Of America","c":"Austrila","d":"Newziland"}
# a.update(b)
# print(a)

# # prgm to keys with values
# key=(input("Enter the key (int) to be added:"))
# value=(input("Enter the value for the key to be added:"))
# d={}
# d.update({key:value})
# print("Updated dictionary is:")
# print(d)

##update a dicts into one
# d1={"a":1,"b":2,"c":3}
# d2={"d":4,"e":5}
# d1.update(d2)
# print(d1)

""" Add key and value to dictionary """

# members={1001:"James",1002:"Elon",1003:"Jack"}
# print(members)
# members[1004]="Slaken"
# print(members)

# sum all the values in the dictionary

# d={'A':100,'B':540,'C':239}
# print("Total sum of values in the dictionary:")
# print(sum(d.values()))

""" Dictionary comphencrision is similary list comprehension """

# text =""" By 1908 Einstein was recognised 
# as a leading scientist and was appointed 
# lecturer at the university of Bern"""
# dict_a={x: len(x) for x in text.split(" ")}
# print(dict_a)

# x=int("10")
# print(x,type(x))
# print(x*25)
# x=int("hello")
# print(x,type(x))   ## error

# x=dict([10,20,30,40,50])    ## cNNOT CONVERRT this list to dictionary
# print(x,type(x))


## tuple keys
# dict_t={(1,10):"Value1",(1,20):"Value2",(1,30):"Value3"}
# print(dict_t)
# print(dict_t.get((1,10)))

# ## if we try to assign unhashable type,gives Type error
# dict_l={[1,10]:"Value1",[1,20]:"Value2",[1,30]:"Value3"}
# print(dict_t)

# sequence=[[1,"john"],[2,"jain"],[3,"sunlean"]]
# print(dict(sequence))

# p=dict([("Kohli",18),("Dohni",7),("Rohit",45),("Rishab",777),("RAhul",1)])  ## Assigning list of tuple elements to dictionary
# print(p,type(p),id(p))

# for s in p.values():    # for only values 
#     print(s)
# for k in p.keys():
#     print(k)
# ## Or 
# for w in p:      ## for Values
#     print(p[w])

# ## For key and values

# for h in p:
#     print(h,":",p[h])
#     print(h,":",p[h],sep="")

# p=dict([["Kohli",18],["Dohni",7],["Rohit",45],["Rishab",777],["RAhul",1]])  ## Assigning list of list elements to dictionary
# print(p,type(p),id(p))

# p=dict([("Kohli",18),("Dohni",7),("Rohit",45),("Rishab",777),("RAhul",1)])  ## Assigning list of tuple elements to dictionary
# print(p,type(p),id(p))

# p=dict((["Kohli",18],["Dohni",7],["Rohit",45],["Rishab",777],["RAhul",1]))  ## Assigning tuple of list elements to dictionary
# print(p,type(p),id(p))


# p=dict([{"Kohli",18},{"Dohni",7},{"Rohit",45},{"Rishab",777},{"RAhul",1}])  ## Assigning list of tuple elements to dictionary
# print(p,type(p),id(p))  ## valid bu not recommend bcz its set inserction order is not presssvered @@ check OP

# p=dict([("Kohli",18),{"Dohni",7},("Rohit",45),["Rishab",777],{"RAhul",1}])  ## Assigning list of tuple elements to dictionary
# print(p,type(p),id(p))    ## list of different elements possibllen but not suggesteble

# """NOTE: IN A DICTIONARY VALUE CAN BE ANY TYPE int,float,str,Bool,set,list,tuple,dict types """

# x={"emp":["Rahul","Ramesh","John","Reyan"],"e_id":[101,102,103,104]}
# print(x,type(x))
# print(x["emp"])
# print(x["e_id"])
# print(x["emp"][0],x["e_id"][0],sep=":")
# print(type(x["emp"]))
# print(type(x["emp"][0]))
# print(type(x["e_id"]))
# print(type(x["e_id"][0]))
# ## Accessing the name Ramesh and his id
# print(x["emp"][1])
# print(x["e_id"][1])
# ## Extracting the Ramesh john rean
# print(x["emp"][1:5])

""" Dictionary is used for collection of various detils{k:v} about a particular object 
ex: customer,employee,student
"""

# customer={"Name":"Nazeer","Ac_no":1234567890123,"Ac_type":"Savings","Branch":"Ameerpet","Bank_name":"Statebank of India"}
# employee={"Name":"Cummins","Salary":700000,"Designation":"Manager","Work_location":"Hyderabad"}
# student={"Name":"Mark Jukar Burg","Branch":"CSE","university":"Oxford University","Location":"London"}
# print(customer)
# print(employee)
# print(student)
# ##  Accesing the valuse if you pass key u will get values

# print(customer["Name"])
# print(employee["Name"])
# print(student["Name"])
# print(student["university"])
# print(student["Location"])
# print(customer["Ac_no"])
# print(customer["Bank_name"])
# print(employee["Salary"])
# print("Work_location",employee["Work_location"])
# ##print(employee["Name","Designation"])   ## not correct syntax error
# print(employee["Name"],["Designation"])  ## check output not correct syntax
# # Ex:
# x=[12,25,30,45,6,49,5]
# ##print(x[1,4])   ### TypeError: list indices must be integers or slices, not tuple
# print(x[1:4])
# ##print(x[1,2])   ## TypeError: list indices must be integers or slices, not tuple
# ##print(x[1][2])    ## TypeError: 'int' object is not subscriptable
# print(x[1],x[2])

""" Working with dictionarys addresses """

# d={"a":10,"b":20,"c":40}
# print(d,type(d));print(id(d))
#                                ##  }---> this two adresses are different
# e={"a":10,"b":20,"c":40}
# print(e,type(e));print(id(e))

# print(d==e) ## compares Content
# print(d is e) ## compares Adressespri
# print(d["a"],type(d["a"]),id(d["a"]))    ## this two adresses are same
# print(e["a"],type(e["a"]),id(e["a"]))

# print(d["a"]==e["a"])
# print(d["a"] is e["a"])    ## this two adresses and content are same so both conditions are True

# p=10
# print(p is d["a"])
# print(p == d["a"])
# print(p is e["a"])    # }--> content and addresses are same  
# print(p is e["a"])

# a=[10,20,30,40]
# print(a[0] is e["a"])   # yes True

""" Dictionary within Dictionary """

# customer={"name":"Adam Jampa","account_no":987654321,"bank_name":"HDFC","address":{"hno":"50/10 12 A","street":"Madhuranagar","city":"Hyderabad","pin_code":500038}}
# print(customer)
# print(customer["name"])
# print(customer["account_no"])
# print(customer["bank_name"])
# print(customer["address"])
# print("\n")
# print("Hno",customer["address"]["hno"],sep="=")

# ## Modifying the dictionary

# customer["name"]="Deepk Chahar"
# customer["account_no"]=123456789
# customer["address"]["hno"]="121-12/10A"
# customer["address"]["street"]="SR Nagar"

# Method of dictionary :- getting key and values
# print(customer.keys())
# print(customer.values())

#print(customer)
## NOTE:we can only change values of a dictionary if u acnt change key also just 
# remove that key:value and add as new as u required





