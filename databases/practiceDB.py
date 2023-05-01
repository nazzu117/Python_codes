# we have pymysql,mysqlclint

# import pymysql

# conn=(pymysql.connect(user="root",password="",host="localhost",database="nazzu_python"))
# cur=conn.cursor()
#cur.execute("create database nazzu_python")

# cur.execute("create table employee_details(emp_id int(10),emp_name varchar(30),emp_salary int(8),emp_location varchar(20),emp_designation varchar(22))")

# cur.execute("insert into employee_details values(1001,'suresh',76000,'banglore','softweardeveloper')")
# cur.execute("insert into employee_details values(1002,'ramesh',66000,'pune','softwearengineer')")
# cur.execute("insert into employee_details values(1003,'mahesh',74000,'mumbai','softweardeveloper')")
# cur.execute("insert into employee_details values(1004,'nazeer',96000,'hyderabad','softweardeveloper')")
# cur.execute("insert into employee_details values(1005,'venkatesh',56000,'delhi','softweardeveloper')")
# cur.execute("insert into employee_details values(1006,'venkatesh',66000,'banglore','softweardeveloper')")
# cur.execute("insert into employee_details values(1007,'kulraman',126000,'kolkatta','softweardeveloper')")
# cur.execute("insert into employee_details values(1008,'suvarna',176000,'chennai','softweardeveloper')")
# cur.execute("insert into employee_details values(1009,'raleka',116000,'pune','softweardeveloper')")
# cur.execute("insert into employee_details values(1010,'bogesh',276000,'pune','softweardeveloper')")
# print(cur.execute("select * from employee_details"))
# # print(cur.fetchone())
# print(cur.fetchall)



# conn.commit()
# conn.close()
### =================================================================================================================

import pymysql

conn=pymysql.connect(user="root",password="",host="localhost",database="my_family")
cur=conn.cursor()
# cur.execute("create database my_family")
# cur.execute("create table falily_data(sno int(10),family_member_name varchar(20),family_member_age int(3),family_member_accupation varchar(10))")
# cur.execute("insert into falily_data values(1001,'suresh',34,'softweardeveloper')")
cur.execute("insert into falily_data values(1001,'suresh',34,'softweardeveloper')")
cur.execute("insert into falily_data values(1001,'suresh',34,'softweardeveloper')")
cur.execute("insert into falily_data values(1001,'suresh',34,'softweardeveloper')")
cur.execute("insert into falily_data values(1001,'suresh',34,'softweardeveloper')")
cur.execute("insert into falily_data values(1001,'suresh',34,'softweardeveloper')")
cur.execute("insert into falily_data values(1001,'suresh',34,'softweardeveloper')")
print(cur.execute("select * from falily_data"))

cur.execute("drop database my_family")







conn.close