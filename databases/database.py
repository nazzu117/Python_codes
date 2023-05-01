# Python can be used in database applications.One of the most popular databases is MySQL.

# connect from database to python by following ways:-
# connectors--- pymysql,mysqlclint,MYSQLDB......
#---> pip install package name:::::> pip install pymysql
# excel
#import connector

# import pymysql
## connection to the server

# conn=(pymysql.connect(user='root',password="",host="localhost",database="family_details"))
# cur=conn.cursor()
# cur.execute("create database family_details")
# cur.execute("create table Family_Data(Number int(10),Family_Membername varchar(15),Age int(10),Work varchar(15),Material_staus varchar(10))")
# cur.execute("insert into Family_Data values(1,'Nazeer',28,'Developer','Inrelation')")
# print(cur.execute("select * from family_data"))
# print(cur.fetchone()) will gives one person details
# print(cur.fetchall())      # fetchall gives all the members details
# cur.execute("update family_data set Family_Membername='Nazzu' where Age=25") 
# cur.execute("delete from family_data where Age=25")
# cur.execute("truncate family_data")
# cur.execute("drop table family_data")
# cur.execute("drop database family_details")
# conn.commit()    # will affect the changes in table

#conn.close()

