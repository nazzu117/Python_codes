# we are going to have two types of  attribute 
# 1. instance attribute--> those arguments we can accessed only with object is called as instance
# 2. class attribute ---> can accessed with class and object
   
# 1.instance : we can accesed only with object and declared inside self -->most used method
#2. class : accessed with both class and object,can acessed with both objet and class
# when we dont have arrribute we get it from class only is called class attributes

# 1.instance attribute: inside a method inside self,can accessed with method
# class  Employee:
#     emp_id=1001                 # class attributes
#     emp_name="Naresh"
#     def __init__(self,emp_id,emp_name,emp_email):
#         self.emp_id=emp_id                        # instance attributes 
#         self.emp_name=emp_name
#         self.emp_email=emp_email

# obj=Employee(444,"Nazzu","suman@gmail.com")
# print(obj.emp_id)
# print(obj.emp_name)         ## instance attributes that accesed with obj name
# print(Employee.emp_name)    ## class attributes that accessed with class name



# methods--> functions declared inside the class are called methods
# instance methods - which will take self as default argument.can accesed with only object
# class methods--it will take cls as default argument and acessed with both class have @classmethod decorators


# class  Employee:
#     emp_id=1001                 # class attributes
#     emp_name="Naresh"
#     def __init__(self,emp_id,emp_name,emp_email):
#         self.emp_id=emp_id                        # instance attributes 
#         self.emp_name=emp_name
#         self.emp_email=emp_email

#     def mymethod(self):
#         print("heloo")
#         pass
#     def details(self):
#         return "{} is {}".format(self.emp_name,self.emp_email)

#     @classmethod                      # class method ,observe cls insteed of self
#     def clsmethod(cls,emp_name,emp_email):
#         return "{} {}".format(emp_name,emp_email)

# obj=Employee(444,"Nazzu","suman@gmail.com")
# print(obj.emp_id)
# print(obj.emp_name)         ## instance attributes that accesed with obj name
# print(Employee.emp_name)
# print(Employee.clsmethod("nazeer","nazeer@gmail.com"))        # calling class method
# print(obj.clsmethod("suresh","suresh@gmail.com"))