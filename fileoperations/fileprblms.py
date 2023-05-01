## programme to Python Program to Read the Contents of a File

# a=str(input("Enter the file name wit .txt extension: "))
# b=open(a,"r")
# line=b.readline()
# while(line!=""):
#     print(line)
#     line=b.readline()
# b.close()

#Python Program to Read a String from the User and Append it into a File

fname = input("Enter file name: ")
file3=open(fname,"a")
c=input("Enter string to append: \n")
file3.write("\n")
file3.write(c)
file3.close()
print("Contents of appended file:")
file4=open(fname,'r')
line1=file4.readline()
while(line1!=""):
    print(line1)
    line1=file4.readline()    
file4.close()

