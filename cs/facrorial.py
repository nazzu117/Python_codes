# the product of an integer and all the integers below it; e.g. factorial four ( 4! ) is equal to 24.

n=int(input("Enter the number :"))
result=1
for i in range(n,0, -1):
    result=result*i
print("factorial of", n ,"is",result)


# factorial using function recursion..

# def factorial(a):
#     if a==1:
#         return 1
#     else:
#         return a*factorial(a-1)    #n*(n-1)(n-2)....
# print(factorial(6))

# recursion

