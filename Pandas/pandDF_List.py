"""  Pandas DataFrame """

## A pandas DataFrame can be created using the following class constructor -
## pandas.DataFrame(data,index,column,dtype)
"""
--> Data:-  data takes various forms like ndarray,serices,list,dictionary,constants,files also other DataFrames
--> index:- For the row labels
--> columns:- For column labels
--> Data type of each column. 

===> A pandas DataFrame can be created using various inputs like:
                                                                 i) List
                                                                 ii) Dict
                                                                 iii)Series
                                                                 iv) Numpy ndarrys
                                                                 v) Another DataFrame
                                                                 Vi) Files
"""

## 1) Creating a empty dataframe

# import pandas as pd
# df=pd.DataFrame()
# print(df)
# print('\n\n')

##---------------------------------------------------------------------------------------------------------

## 2) Creating a DataFrame with List
import pandas as pd
# cites=["Hyderabad","Pune","Banglore","Delhi","Mumbai"]
# df=pd.DataFrame(cites)
# print(df)

##----------------------------------------------------------------------------------------------------------

## 3) Creating a DataFrame from NestedsLists

# data=[["Miller",10000],["Blake",30000],["Bosch",50000],["Srlnk",60000]]
# df=pd.DataFrame(data,columns=["NAME","SALARY"])
# print(df)

##----------------------------------------------------------------------------------------------------------

## 4) Creating a DataFrame from a list of dictionary

# data=[{"LG":4,"SAMSUNG":6},{"LENOVO":3,"APPLE":1},{"HP":6,"DELL":2}]
# df=pd.DataFrame(data)
# print(df)

##----------------------------------------------------------------------------------------------------------

## 5) Creating our own indeces(string indeices)



import pandas as pd
data = [{'LG': 10, 'SONY': 20},{'LG': 5, 'SONY': 10, 'SAMSUNG': 20}]
df = pd.DataFrame(data,index=["first","second"])
print(df)
