""" CREATING DATAFRAME """

"""i) Creating a dataframe from a dictionary """

# import pandas as pd

# data={ 
#     'enames':['Samrat','Ravana','Rama','Lakshman','Sita','Vibhishana'],
#     'salarys':[1000,2000,3000,4000,5000,6000]

# }
# ## Passing this dictionary(data) into pandas dataframe constructor,so that a dataframe gets created

# df1=pd.DataFrame(data)
# print(df1)
# #Note here by default we get index starting with 0, even we can have our own index
# df1=pd.DataFrame(data,index=["a","b","c","d","e","f"])
# print(df1)

###-----------------------------------------------------------------------------------------------------------
""" ii) Even we can create index as string type """

from datetime import date
import pandas as pd

data={ "Sony":[250,400,350,300,500,600,280,890,900,330,450,550],
       "Samsung":[300,400,230,500,890,750,340,880,600,800,500,550],
       "Lenovo":[500,300,500,690,380,500,780,990,300,450,680,660]
}

df2=pd.DataFrame(data)
# print(df2)

print("\n\n")
### Changing the indexes names
df2=pd.DataFrame(data,index=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"])
# print(df2)

## Retrive particular month data
# print(df2.loc['Feb'])
# print(df2.loc['Jan'])
# print(df2.loc['Aug'])
# print(df2.loc['Sep'])


###------------------------------------------------------------------------------------------------------------

""" iii) indexing and slicing """
## --> A) Printing a particular series(Data)
print(df2['Lenovo'])
## Here we don't see any coloumn

## --> B) Printing DataFrame
print(df2[['Lenovo']])          ## Observe The double Squre Brackets[[]] for columns

## --> C) Printing Multiple columns as dataframe
print(df2[['Sony','Samsung']])
print('\n\n')
## --> D) Slicing a Dataframe, Retriving specific row

# x=df2[0:3]
# print(x)

## --> E) More Dataselection operations
## using loc,ilocyou can get select certain data set.
## loc uses string indeces
## iloc uses int indeces

# x=df2.loc[['Apr','May']]
# print(x) 
# print('\n\n')

# x=df2.loc[['Jan','Sep']]
# print(x) 
# print('\n\n')

## --> F) iloc

# x=df2.iloc[3]
# print(x)

## --> G) getting more than one coloum

# x=df2.iloc[:,1:3]
# print(x)
# print('\n\n')

# x=df2.iloc[0:3,1:3]
# print(x)

##------------------------------------------------------------------------------------------------------------

## --> H) Sorting data
##  def.sort_values('Sony')
## By default sorts in assinding order

x=df2.sort_values('Sony')
print(x)
print('\n\n')


x=df2.sort_values("Sony",ascending=False)
print(x)
print("\n\n")


##############################################################################################################

## --> I) Renaming a DataFrame

""" Renaming Sony to LG"""

x=df2.columns=['LG','Samsung','Lenovo']
print(x)
print("\n\n")

'''
o/p:

['Samsung', 'LG', 'Lenovo']

'''
## --> J) Dropping a column

x=df2.drop("LG",axis=1)
print(x)
"""
o\p
     Samsung  Lenovo
Jan      300     500
Feb      400     300
Mar      230     500
Apr      500     690
May      890     380
Jun      750     500
Jul      340     780
Aug      880     990
Sep      600     300
Oct      800     450
Nov      500     680
Dec      550     660
"""

## Droping a row

x=df2.drop('May')
print(x)

## --> K) Adding a new coloumn

df2['Apple']=df2.eval("LG+100")         ## LG+100 Means it adds +100 to all LG values
print(df2)

## -->L) Adding a new colounm  JIO

df2["JIO"]=pd.Series([120,300,330,450,280,700,600,500,890,900,680,580],index=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"])
print(df2)


## --> M) Converting DataFrame to Excel

# df2.to_excel("Mobiles.xlsx")

##--> N) max()

x=df2.Lenovo.max()
print(x)

""" OP  -> 990  """

## -->O) groupby
x=df2.groupby('Apple').sum()
print(x)

## -->P)  Missing values in pandas
## isnull(): will tell  if a column misses a value

print(df2.isnull())

"""
        LG  Samsung  Lenovo  Apple    JIO
Jan  False    False   False  False  False
Feb  False    False   False  False  False
Mar  False    False   False  False  False
Apr  False    False   False  False  False
May  False    False   False  False  False
Jun  False    False   False  False  False
Jul  False    False   False  False  False
Aug  False    False   False  False  False
Sep  False    False   False  False  False
Oct  False    False   False  False  False
Nov  False    False   False  False  False
Dec  False    False   False  False  False

"""

## -->Q)Ranking:
## --> rank():to rank every column according to its value

print(df2.rank())

"""
       LG  Samsung  Lenovo  Apple   JIO
Jan   1.0      2.0     6.0    1.0   1.0
Feb   6.0      4.0     1.5    6.0   3.0
Mar   5.0      1.0     6.0    5.0   4.0
Apr   3.0      5.5    10.0    3.0   5.0
May   8.0     12.0     3.0    8.0   2.0
Jun  10.0      9.0     6.0   10.0  10.0
Jul   2.0      3.0    11.0    2.0   8.0
Aug  11.0     11.0    12.0   11.0   6.0
Sep  12.0      8.0     1.5   12.0  11.0
Oct   4.0     10.0     4.0    4.0  12.0
Nov   7.0      5.5     9.0    7.0   9.0
Dec   9.0      7.0     8.0    9.0   7.0
"""

##--> R) Concatenating 2 dataframes
##--> concat():we can concatenate two or more DataFrames
x=pd.concat([df2,df2])
print(x)

#Note: we can even concat 3 or more dataframes