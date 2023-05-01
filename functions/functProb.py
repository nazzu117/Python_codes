#  Write a python function to multiple all numbers in a list?

# def multiplyList(myList):
#     # Multiply elements one by one
#     result = 1
#     for x in myList:
#         result = result * x
#     return result

# # Driver code
# list1 = [1, 2, 3]
# list2 = [3, 2, 4]
# print(multiplyList(list1))
# print(multiplyList(list2))

# Write a python function for reversing a string ?

# def reverse(x):
#     return x[::-1]
# mytxt=reverse("A text to reverse the string..")

# print(mytxt)

# # 2nd Way

# def reverse(string):
#     if len(string) == 0:
#         return string
#     else:
#         return reverse(string[1:]) + string[0]
# a = str(input("Enter the string to be reversed: "))
# print(reverse(a))

# 3rd Way

# def reverse(string):
#     if len(string)==0:
#         return string
#     else:
#         return string[::-1]
# n=input("enter string: ")
# print(reverse(n))


# Write a python function to print even numbers from the given list?

# def is_even_num(l):
#     e_num = []
#     for n in l:
#         if n % 2 == 0:
#             e_num.append(n)
#     return e_num
# print(is_even_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# Write a python function program for factorial of a given numbers?

# def factorial(a):
#     if a==0:
#         return 1
#     else:
#         return a * factorial(a-1)
# a=int(input("Input a number to compute the factiorial : "))
# print(factorial(a))



# Write a python function program which can generate a dictionary where the keys...
# ....are numbers between 1 and 20 and the values are square of keys.

# d=dict()
# for x in range(1,20):
#     d[x]=x**2
# print(d)



# def avg(n1,n2,n3):
#     return (n1+n2+n3)/3
# result1=avg(20,444,37)
# result2=avg(1.1,56.76,4.9)
# result3=avg(34,55.7,45)
# print(result1)
# print(result2)
# print(result3)


# def myfun(x):
#     return 45*x
# print(myfun(5))
# print(myfun(25))
# print(myfun(54))
    
# num=int(input("Enter the number to check abs value:"))
# def abs(num):
#     if num>=0:
#         return num
#     else:
#         return -num
# print(abs(-45635))
# print(abs(8484))



# passing a list to a variable


# def count(lst):
#     even=0
#     odd=0
#     for i in lst:
#         if i%2==0:
#             even+=1
#         else:
#             odd+=1
#     return even,odd
# lst=[23,1,54,78,3,5,66,98,123,7,68,203]
# even,odd=count(lst)
# print("even:",even)
# print("odd:",odd)

# print("Even: {} \n odd: {}".format(even,odd))

# passing list to function2

# def show(l):
#     print(l)
#     print(type(l))
#     for i in l:
#         print(i)
# list=[10,20,30,'nazzu','rama']
# show(list)

# 3

# def my_function(food):
#   for x in food:
#     print(x)

# fruits = ["apple", "banana", "cherry"]

# my_function(fruits)

