## filter(): function is for filtering the data based aon the condition 
## filter () takes two arguments :
##    1.Lambda function
##    2.iterable like list

# EX:=

list1=[10,20,30,40,50,60]

""" Filter those elements whose value grater than 30  """

s=list(filter(lambda x:x>30,list1))     ### Here x is the each element of list1
print(s,type(s))

""" filter whose value is 3%==0 """
s=list(filter(lambda x:x%3==0,list1))
print(s,type(s))

## EX2:-

emps=[[101,"miller",75000,"m",11,"hyderabad"],
      [102,"david",80000,"m",12,"banglore"],
      [103,"curran",72000,"m",13,"hyderabad"],
      [104,"perry",66000,"f",14,"pune"],
      [105,"smith",90000,"m",15,"hyderabad"],
      [106,"sofia",74000,"f",16,"banglore"]]

""" TASK: filter those emps those who belongs to hyderabad """
# hi=list(filter(lambda x:x[5]=="hyderabad",emps))
# print(hi,type(hi))

""" TASK: filter those emps are male """
# hi=list(filter(lambda x:x[3]=="m",emps))
# print(hi,type(hi))

""" TASK: we can provide multiple conditions also """
s=list(filter(lambda x : x[2]>75000 and x[4]==11,emps))

print(s,type(s))