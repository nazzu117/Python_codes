""" Pattern for love simbole"""
# for row in range(6):
#     for col in range(7):
#         if (row==0 and col%3!=0) or (row==1 and col%3==0) or (row-col==2) or (row+col==8):
#             print("*",end="")
#         else:
#             print(end=" ")
#     print()


# n=int(input("Enter the number of rows: "))
# num=1
# for row in range(1,n+1):
#     for col in range(1,row+1):
#         print(num,end=" ")
#         num=num+1
#     print()


# 10 is the total number to print
# for num in range(10):
#     for i in range(num):
#         print (num, end=" ") #print number
#     # new line after each row to display pattern correctly
#     print()


# print("Print full Triangle pyramid using stars ")
# size = 7
# m = (2 * size) - 2
# for i in range(0, size):
#     for j in range(0, m):
#         print(end=" ")
#     m = m - 1 # decrementing m after each loop
#     for j in range(0, i + 1):
#         # printing full Triangle pyramid using stars
#         print("* ", end=' ')
#     print(" ")


# print("Program to print half pyramid: ")

# rows = input("Enter number of rows ")
# rows = int (rows)

# for i in range (0, rows):
#     for j in range(0, i + 1):
#         print("*", end=' ')

#     print("\r")


#Example 3: Program to print inverted half pyramid using an asterisk (star)

# print("Program to print half pyramid: ")

# rows = input("Enter number of rows ")
# rows = int (rows)

# for i in range (rows,0,-1):
#     for j in range(0, i + 1):
#         print("*", end=' ')

#     print("\r")