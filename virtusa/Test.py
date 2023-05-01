#Task--1

# a=input("Enter your string: ")
# b=input("Enter your charecter: ")


# count=0

# for i in a:
#     if b in a:
#         if i==b:  
#            count=count+1
# print(a.count(b))


# print(count)

##----------------------------------------------------------------------------------------------------------


x = int(input("Input first number: "))
y = int(input("Input second number: "))
z = int(input("Input third number: "))

a = min(x,y,z)
c = max(x,y,z)
b = (x+y+z)-a-c
print("Numbers in sorted order:",a,b,c,sep=",")




