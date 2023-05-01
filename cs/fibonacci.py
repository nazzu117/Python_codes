
# a series of numbers in which each number ( Fibonacci number ) \n 
# is the sum of the two preceding numbers. The simplest is the series 0,1, 1, 2, 3, 5, 8,13 etc...

num=int(input("Enter how many numbers you want in fibonacci serices: "))
first=0
secound=1
for i in range (num):
    # print(first,end=" ")
    temp=first
    first=secound
    secound=temp+secound
print(first,end=" ")