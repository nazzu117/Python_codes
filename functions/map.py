## map(): map function also takes two arguments 
##    1.lambda
##    2.iterable type list


""" Adding 5 to each element of the list """
# list1=[10,20,30,40,50]
# dee=list(map(lambda x:x+5,list1))
# print(dee)

# emps=[[101,"miller",75000,"m",11,"hyderabad"],
#       [102,"david",80000,"m",12,"banglore"],
#       [103,"curran",72000,"m",13,"hyderabad"],
#       [104,"perry",66000,"f",14,"pune"],
#       [105,"smith",90000,"m",15,"hyderabad"],
#       [106,"sofia",74000,"f",16,"banglore"]]

""" Adding 5000 salary to each employee as bonous """

# rslt1=list(map(lambda x:(x[0],x[1],x[2]+5000,x[3],x[4],x[5]),emps))
# print(rslt1)

""" Modify each name should start with uppercase """
# res=list(map(lambda x:(x[0],x[1].capitalize(),x[2],x[3],x[4],x[5]),rslt1))
# print(res)

# res2=list(map(lambda x:(x[0],x[1],x[2],"male" if (x[3]=="m") else "female",x[4],x[5]),res))
# print(res2)











""" BOOL():- 
Bool function which returns either True or False
"""
# def disp(x,y):
#     if x>y:
#         return True
#     else:
#         return False
# print(disp(100,12))
    





























































