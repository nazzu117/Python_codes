#Creating Pandas Dataframes from series

#Create a DataFrame from Dict of Series
#Dictionary of Series can be passed to a DataFrame.
#The resultant index is the union of all the series indexes passed.

import pandas as pd

d= { 'student1':pd.Series([90,95,99],index=["Maths","Physics","Chimestry"]),
     'student2':pd.Series([99,99,98],index=["Maths","Physics","Chimestry"])
  }
# print(d)
# print(type(d))
# print(len(d))

df=pd.DataFrame(d)    ## Observe the difference in the outputs 
print(df)

# ## -->1) Column selection 
# print(df["student1"])

## -->2) Column adding

## Adding a new column to an exesting DataFrame with column label by passing new series
print("Adding a new column by passing as Series:")
df['student3']=pd.Series([100,99,98],index=["Maths","Physics","Chemistry"])
print(df)

print ("Adding a new column using the existing columns in DataFrame:")
df['Total']=df['student1']+df['student2']+df['student3']
df['Average']=(df['student1']+df['student2']+df['student3'])/3
print(df)

##-------------------------------------------------------------------------------------------------------------

## 3) Deleting a column 
# using del function
print ("Deleting the first column using DEL function:")
del df['student1']
print(df)
print("\n")
# using pop function
print ("Deleting another column using POP function:")
df.pop('student2')
print(df)

##-----------------------------------------------------------------------------------------------------------

#5)Addition of Rows using append()
#This function will append the rows at the end.

import pandas as pd

df1 = pd.DataFrame([["Ajay",20000], ["James", 50000]], columns = ['NAME','SALARY'])
df2 = pd.DataFrame([["Naresh",60000], ["Blake",80000]], columns = ['NAME','SALARY'])

df = df1.append(df2)
print(df)
print("\n")


#--------------------------------------------------------------------------------------------------
#Deletion of Rows using drop()
#Use index label to delete or drop rows from a DataFrame.
#If label is duplicated, then multiple rows will be dropped.

df = df.drop(0)
print(df)



#---------------------------------------------------------------------------------------