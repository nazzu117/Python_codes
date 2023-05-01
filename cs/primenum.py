# a number that is divisible only by itself and 1 (e.g. 2, 3, 5, 7, 11)...
# "prime numbers are very useful in cryptography"

num=int(input("Enter the Number to find out prime number: "))
if num>1:
    for i in range(2,num):
        if (num%i)==0:
            print( "its not a prime numner")
            break
    else:
        print("its a prime number")
else:
    print("its not a prime number")