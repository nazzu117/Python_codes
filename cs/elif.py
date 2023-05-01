#Note: to dlecare elif condition before the if condition is compulsory

# experiance=int(input("Enter years of experiance:"))
# if experiance >6:
#     print("based on your experiance you are a seniour level developer...!")
# elif experiance>3 and experiance<=6:
#     print("based on your experiance you are a associated level developer...!")
# elif experiance>0 and experiance<=3:
#     print("based on your experiance you are a Junior or  level developer...!")

num = int(input("give me a number to check: "))
check = int(input("give me a number to divide by: "))

if num % 4 == 0:
    print(num, "is a multiple of 4")
elif num % 2 == 0:
    print(num, "is an even number")
else:
    print(num, "is an odd number")

if num % check == 0:
    print(num, "divides evenly by", check)
else:
    print(num, "does not divide evenly by", check)