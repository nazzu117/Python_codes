# print(help("modules"))   # to get list of all modules

# import random
# print(dir(random))
# print(help(random))  # this will give the uses/description of particular module
# print(random.random()) Generates a random float number between 0.0 to 1.0. The function doesn't need any arguments.
# print(random.randrange(1,10,3))
# print(random.choice("Heloo World "))
# print(random.randint(100,10000))
# a=["WELCOME","HELLO","GET50",22,56.66]
# print(random.choice(a))
# random.shuffle(a)
# print(a)


# import datetime

# print(help(datetime))
# print(dir(datetime))

# from datetime import date
# my_date = date(1996, 12, 11)
# print("Date passed as argument is", my_date)

# print(datetime.datetime.now())   # present date with time
# print(datetime.datetime.now().date())   # present date only
# print(datetime.datetime.now().date().year)
# print(datetime.datetime.now().date().day)
# print(datetime.datetime.now().date().month)


# # # time related
# print(datetime.datetime.now().time())
# print(datetime.datetime.now().time().hour)
# print(datetime.datetime.now().secound)
# print(datetime.datetime.now()+datetime.timedelta(days=60))    # timedelta gives the days from particular period

# change format of date
# a=datetime.datetime.now()
# print(datetime.datetime.strftime(a,"%d:%m:%Y"))     # use %b for month in string formate

# import calendar

# print(dir(calendar))
# print(calendar.())   # day 1 in a week
# print(calendar.day_name[0])
# print(calendar.day_name[6])
# print(calendar.isleap(1994))
# print(calendar.month(2020,4))
# print(calendar.calendar(2020))


# import os

# print(os.getcwd())
# os.chdir("your dairecty ")   # past the path here to cange current working folder location
# print(os.listdir())
# print(os.listdir("C//"))      # gives fils on C drive
# os.mkdir("helloworld")    # create a folder at current working folder
# os.rmdir("helloworld")      # delete the folder under current working folder
#os.rename("filename","new name")
# os.system("shutdown /s /t 1")  # shutdown the PC

# # create as many folders as u want as showed below
# a=["folder1","folder2","folder3","folder4"]
# for i in a:
#     os.mkmdir(i+'_folder')

# # remove folders as u want as showed below
# a=["folder1","folder2","folder3","folder4"]
# for i in a:
#     os.rmdir(i+'_folder')

# print(os.path.isfile("C:/Users/nazeer/python/modules/nazeer"))   # it will gives boolen value

# get your system using platform module

# import platform
# print(platform.platform())
# print(platform.system())
# print(platform.processor())
# print(platform.architecture())
# print(platform.release)
# print(platform.machine)
# print(platform.version)
# print(platform.uname)
# print(platform.node)
# print(platform.python_build())
# print(platform.python_compiler)
# print(platform.python_implementation)
# print(platform.python_version)
# print(platform.python_version_tuple)

# import math
# x=math.sqrt(125)
# print(x)
# print(math.floor(2.90))   # it will round it 2
# print(math.ceil(3.01))     # it will 3
# print(math.pow(2,4))
# print(math.pi)
# print(math.e)
# print(math.cosh(10))      # cosine of x
# print(help(math))
# print(dir(math))


# logging
# threading
# re

# import matplotlib.pyplot as plt 
# plt.plot ([10,20,30,40,50],[5,4,3,4,5])
# plt.show()

# import matplotlib.pyplot as plt

# # x-coordinates of left sides of bars
# left = [1, 2, 3, 4, 5]

# # heights of bars
# height = [10, 24, 36, 20, 15]

# # labels for bars
# tick_label = ['one', 'two', 'three', 'four', 'five']

# # plotting a bar chart
# plt.bar(left, height, tick_label = tick_label,
# 		width = 0.5, color = ['Black', 'green'])

# # naming the x-axis
# plt.xlabel('x - axis')
# # naming the y-axis
# plt.ylabel('y - axis')
# # plot title
# plt.title('My bar chart!')

# # function to show the plot
# plt.show()

""" Pi chart """
# import matplotlib.pyplot as plt
  
# # defining labels
# activities = ['eat', 'sleep', 'work', 'play']
  
# # portion covered by each label
# slices = [3, 7, 8, 6]
  
# # color for each label
# colors = ['r', 'y', 'g', 'pink']
  
# # plotting the pie chart
# plt.pie(slices, labels = activities, colors=colors, 
#         startangle=90, shadow = True, explode = (0, 0, 0.1, 0),
#         radius = 1.2, autopct = '%1.1f%%')
  
# # plotting legend
# plt.legend()
  
# # showing the plot
# plt.show()



import matplotlib.pyplot as plt

days = [1,2,3,4,5]

sleeping = [7,8,6,11,7]
eating =   [2,3,4,3,2]
working =  [7,8,7,2,2]
playing =  [8,5,7,8,13]
plt.stackplot(days,sleeping,eating,working,playing, colors=['m','c','r','k'])

plt.xlabel('days')
plt.ylabel('hours')
plt.title('Interesting Graph\nCheck it out')
plt.show()


