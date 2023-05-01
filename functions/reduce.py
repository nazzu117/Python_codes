## reduce(): reduce function for cumulative operations 
## reduce() takes two arguments :
##    1.Lambda function
##    2.iterable like list

# EX:-

from functools import reduce
list1=[1,2,31,4,5,6]
res=reduce(lambda x,y:x+y,list1)
print(res)

## O\P ---> ((((1+2)+3)+4)+5)+6))=21

## EX2: to find max element
res=reduce(lambda x,y:x if x>y else y,list1)
print(res)