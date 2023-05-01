from collections import namedtuple

# # #create employee NamedTuple
# Employee = col.namedtuple('Employee', ['name', 'city', 'salary'])
# # #Add two employees

# e1 = Employee('Asim', 'Delhi', '25000')
# e2 = Employee('Bibhas', 'Kolkata', '30000')
# #Access the elements using index
# print('The name and salary of e1: ' + e1[0] + ' and ' + e1[2])
# #Access the elements using attribute name
# print('The name and salary of e2: ' + e2.name + ' and ' + e2.salary)
# #Access the elements using getattr()
# print('The City of e1 and e2: ' + getattr(e1, 'city') + ' and ' + getattr(e2, 'city'))


import collections as col
#create employee NamedTuple
# Employee = col.namedtuple('Employee', ['name', 'city', 'salary'])
# #List of values to Employee
# my_list = ['Asim', 'Delhi', '25000']
# e1 = Employee._make(my_list)
# print(e1)
# #Dict to convert Employee
# my_dict = {'name':'Bibhas', 'city' : 'Kolkata', 'salary' : '30000'}
# e2 = Employee(**my_dict)
# print(e2)
# #Show the named tuple as dictionary
# emp_dict = e1._asdict()
# print(emp_dict)


import collections as col
#create employee NamedTuple
Employee = col.namedtuple('Employee', ['name', 'city', 'salary'])
#Add an employees
e1 = Employee('Asim', 'Delhi', '25000')
print(e1)
print('The fields of Employee: ' + str(e1._fields))
#replace the city of employee e1
e1 = e1._replace(city='Mumbai')
print(e1)


# Python code to demonstrate namedtuple() 
      
# from collections import namedtuple 
      
# # Declaring namedtuple()  
# Student = namedtuple('Student',['name','age','DOB'])  
      
# # Adding values  
# S = Student('Nandini','19','2541997')  
      
# # Access using index  
# print ("The Student age using index is : ",end ="")  
# print (S[1])  
      
# # Access using name   
# print ("The Student name using keyname is : ",end ="")  
# print (S.name)


# Python code to demonstrate namedtuple() and
# _make(), _asdict() and "**" operator
  
# # importing "collections" for namedtuple()
# import collections
  
# # Declaring namedtuple()
# Student = collections.namedtuple('Student',['name','age','DOB'])
  
# # Adding values
# S = Student('Nandini','19','2541997')
  
# # initializing iterable 
# li = ['Manjeet', '19', '411997' ]
  
# # initializing dict
# di = { 'name' : "Nikhil", 'age' : 19 , 'DOB' : '1391997' }
  
# # using _make() to return namedtuple()
# print ("The namedtuple instance using iterable is  : ")
# print (Student._make(li))
  
# # using _asdict() to return an OrderedDict()
# print ("The OrderedDict instance using namedtuple is  : ")
# print (S._asdict())
  
# # using ** operator to return namedtuple from dictionary
# print ("The namedtuple instance from dict is  : ")
# print (Student(**di))
  