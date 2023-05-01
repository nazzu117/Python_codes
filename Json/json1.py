"""
JSON (JavaScript Object Notation):-

---> jason is syntax for storing and exchanging data.it is a text, written with java script notation

---> it is the way of storing the information 

---> data stored in human-readable format

--->NOTE: this is not JavaScript.

---> data must be in the text format

---> a packet of json is ideantical to python dictionary

NOTE:- We can convert all the following oython types to jason

          PYTHON                        JAVASCRIPT
          int       -------------->   number
          float     -------------->   number
          list      -------------->   array
          dict      -------------->   object
          str       -------------->   string
          True      -------------->   true
          False     -------------->   false
          None      -------------->   null
          etc......



Json has more compact style than XML and it is often more readable.the lihgt weight approach of json can make 
significant improvements.

The XML softwear parsing process can take a long time. JSON uses less data overall ,so you reduces the cost and 
increasing the parsing speed.(it's fast,readable)

JSON uses map data structure insteed XML's tree.in some situations,key,value pairs can limit what you can do,but
you get a predatable and easy to understand data model.

Syntax Rules:-  {"name":"John","age":26}

// data is in name/value pairs
// data has saperated by commas
// curly braces holds the Object
// squre brackets holds arrays.              """

import json

# x='{"name":"Samrat","age":29,"location":"Hyderabad","Maturial":"Married"}'

# print(x)
# print(type(x))

# data=json.loads(x)
# print(data)
# print(data['age'])

##------------------------------------------------------------------------------------------
"""Cover from python to jason """

# x={
#   "anme":"Samrat",
# "age":29,
# "location":"Hyderabad",
# "Maturial":"Married"
# }

# y=json.dumps(x)
# print(y)

## We can convert dict ---> list,tuple,string,int,float,True,False,None

# lst=["hello World",23,"Banglore",34,22,8.96,12+4]

# y=json.dumps(lst)
# print(y)

# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))


""" Convert a Python object containing all the legal data types:- """


x= { "name":"John",
      "age":30,
      "city":"Banglore",
      "married":True,
      "divorsed":False,
      "children":("Allen","Solley"),
      "pets":None,
      "cars":[{"model":"BMW 350","mpg":27.5},
                {"model":"Audi A8","mpg":30.6}]

}

# print(json.dumps(x))

y=json.dumps(x)
print(x["children"])


## use four indents to make it easier to read the result:
# print(json.dumps(x, indent=4))

## Use the separators parameter to change the default separator:

# s=json.dumps(x, indent=4, separators=(". ", " = "))
# print(s)
## Use the sort_keys parameter to specify if the result should be sorted or not:

# a=json.dumps(x, indent=4, sort_keys=True)
# print(a)
















# import json

# json1_string=''' {                              
#   "name"="Ramesh",
#   "age"=26,
#   "salary"=77677,
#   "ismarrid="false"
#   "ishavinggirlfriend"="null"
#   } '''
#   ## This is jason string 
#   ## I want conver it into Python dictionary.
# emp_dict=json.loads(json1_string)
# print(type(emp_dict))
# print(emp_dict)
# print("Employee name:",emp_dict['name'])
# print("Employee age:",emp_dict['age'])
# print("Employee salary:",emp_dict['salary'])
# print("Employee marriege status:",emp_dict['ismarrid'])
# print("Employee is having girlfriend:",emp_dict['ishavinggirlfriend'])

# import json

# people_string="""
# {
# "people":[
# {
# "emp_name":"Johnson",
# "emp_id":"123321",
# "emp_salary":99999,
# "emp_email":[johnson@dummymail.com],
# "has_liceance":"False"
# },
# {
# "emp_name":"parriker",
# "emp_id":"987656",
# "emp_salary":"912345",
# "emp_email":[parikar@dummymail.com],
# "has_liceance":"True"
# }
# ]
# }

# """

# data=json.loads(people_string)
# print(data)
# print(type(data))
# print(type(data["people"]))

# for person in data['people']:
#   print(person["emp_name"],["emp_id"])



# import json

# new="""

# {
#   "results": [
#     {
#       "transaction": "LstPartnerMedia",
#       "records": [
#         {
#           "DIVI": "",
#           "DONR": "231",
#           "DOVA": "",
#           "MEPF": "",
#           "PRF1": "600996",
#           "PRF2": "",
#           "MEDC": "MAIL",
#           "SEQN": "1",
#           "SIID": "M3_IDM_COM",
#           "MVIF": "COM",
#           "METY": "04",
#           "FMTP": "",
#           "COPY": "0",
#           "OUTP": "",
#           "UDTA": "",
#           "1UDT": "",
#           "TFNO": "",
#           "TFT1": "",
#           "1TFT": "",
#           "FLRN": "",
#           "PAFD": "",
#           "FSUX": "",
#           "GNNM": "0",
#           "DEV": "",
#           "FOVR": "",
#           "BINX": "",
#           "TOMA": "toxley@americanfoodsgroup.com; kkoffi@americanfoodsgroup.com",
#           "FRMA": "M3@AFG.com",
#           "CCMA": "",
#           "FAXT": "0",
#           "SUBJ": "",
#           "NOTE": "",
#           "CPPL": "2",
#           "LSID": "",
#           "LSAD": "",
#           "TEME": "0",
#           "E065": "",
#           "SRD1": "",
#           "SRD2": "",
#           "RRD1": "",
#           "RRD2": "",
#           "RRD3": "",
#           "TRAY": "",
#           "LAYC": "",
#           "MARI": "",
#           "ARCH": "0",
#           "CNID": "0",
#           "EVPR": "0",
#           "BONM": "",
#           "BOVB": "",
#           "FIET": "1",
#           "EMBT": "",
#           "EMGR": "",
#           "FILM": "00",
#           "FNAM": ""
#         }
#       ]
#     }
#   ],
#   "wasTerminated": "false",
#   "nrOfSuccessfullTransactions": 1,
#   "nrOfFailedTransactions": 0
#  }
#  """
# d=json.loads(new)
# print(new)




