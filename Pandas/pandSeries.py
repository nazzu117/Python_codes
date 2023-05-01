"""  pip install pandas
---> Main componds of pandas are:
1) Series
2)Dataframe

1) Series:- Series is nothing but is calumn
2)Dataframe:- Dataframe is a multidimensions table made up a collection of Series


   Serice       Serice        Dataframe
   eid          ename        eid   ename
   101          Miller       101   miller
   102     +    blake   =    102   blake
   103          slank        103   slank
   104          bosch        104   bosch

"""

"""1) Pandas Series:-
---> Series is one-dimension label arrey
---> A pandas series can be created using following constructor 

pandas.Series(data,index,datatype)

1)data: data takes various forms like ndarrey, list, constants
2)index: index values must be unique
3)datatype: is for datatype

"""

import pandas as pd

""" 1.Creating empty a empty series """

# s=pd.Series()
# print(s)

""" 2. reating a series from Dictionary """

# data={'maths':99,'science':95,'english':90}
# s=pd.Series(data)   ## Here maths,science,english are taken as indeces
# print(s)
# print(s['maths'])   ## Accessing the element using index value

""" 3.Creating a series from List """

data=[10,20,30,40,50]
s=pd.Series(data)
print(s)

# Creating our own indexes
s=pd.Series(data,index=["a","b","c","d","e"])  ## index=values otherwise Error
print(s)

# print(s['b'])
""" 4.Accesing a series of lements """

print(s[0])   ## Accesing the first element
print("\n\n")

print(s[:3])   ## Retrive the first three elements
print("\n\n")

print(s[-3:])  ## Retrive the last three elements
print("\n\n")

print(s['a'])  ## Accesing using index value
print("\n\n")

print(s[['a','c','d']])



