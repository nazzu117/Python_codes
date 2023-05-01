# 1.Method overloading--> python dosent support 
# 2.Method overriding

#1. method overloading is not supporting by python --we can't create two methods with the same name


# class student:
#     def add(self,*a):
#         return sum(a)
#     # def add(self,a,b,c,d,e):
#     #     return a+b+c+d+e
#     # def add(self,a,b,c,d):
#     #     return a+b+c+d

# obj=student

# print(obj.add(3,5,7,4,3,9,8,9))

#2. method overriding

# overriding supports thst same attributes and same methods and considered child class first

# class school:
#     sch_name="Delhi public school"
#     sch_location="Hyderabad"
#     def student_details(self):
#         return "{} studing at {}".format(self.sch_name,self.sch_location)

# class student(school):
#     std_name="Suresh"
#     sch_name="Okridge international school"
#     std_location="Banglore"

#     # def student_details(self):
#     #     return "{} is studing at {}".format(self.std_name,self.sch_name)

# obj=student()
# print(obj.sch_location)
# print(obj.student_details())

# # print(obj.std_school)
# # print(obj.student_details())