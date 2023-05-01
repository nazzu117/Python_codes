""" MULTITHREADING:- The processes of executing 2 or more threads(logics) simulteniously is known as multithreading"""

# class X:
#     def m1(self):
#         for p in range(10):
#             print(p)
#     def m2(self):
#         for q in range(10,20):
#             print(q)
# x1=X()
# x1.m1()
# x1.m2()
"""
Here first m1 method executed and then m2 method ,so here execution is sequential if we want execution 
Parellel then go for the Multithreading

Generally processor executes the programs,it is an electronic circute it understands only power signals
this electronic circute execute only one statement at a time (Sequentially) won't execute parelley

in the programe if we manke m1 as one thread and m2 as 2nd thread, when is waiting for i/p meanwhile m2 logic
will executes and again switches to m1 thread , if issue in m1 again then continue with m2 ,untill the problem resolved
means internally only one thread executed in processor 

process:- A programe is under execution 
Theread:- It is a part of programe or logic which executes simultensiouly along with the other part of the programe

"""

"""
Threading module:- In Threading module we have predefined module call Thread which has a method called run() method
to make logic as a thread, keep the logic in run method we will override the run() method of thread class and
run() method logic behaves like a thread.

"""

# import threading   ## threading is a in-bult module
# class X(threading.Thread):    ## User defined class extending the Thread class(built-in)
#     def run(self):
#         for p in range(10):
#             print(p)
# ## End of class 
# x1=X()
# x1.run()
# for q in range(10,20):
#     print(q)

## statement outside of the class are treated as main thread
## statements or coad with in the run method is called as 2nd thread

"""
if you executed the programe no multithreading is performed bcz here run executed as normal method,but not
Executed as thread, in above programe there are two threads,but not running parelly bcz they are executed normally
so to execute parelley use start() method as function call insteed of run() .
"""

"""
In order to execute run() method logic as thread,need to call run method through the start() method of Thread class
then they are executed parllely  
# """
# import threading
# class X (threading.Thread):
#     def run(self):           ## Thread 2
#         for p in range(1000):
#             print("Hello...!!")
#         # for s in range(300,400):
#         #     print(s)
# # End of the class
# x1=X
# x1.start()    ## Main Thread
# for p in range(100,200):
#     print(p)

## By default python interpreter creates one thread i.e, called main thread
## first main thread start executing ,meanwhile remaining threads gets executed - mixed execution
## here both threads executed parelley

""" If i want to 2 logics ---> if i keep 2 run() methods ---> Takes two classes ----> means 2 Threads   """

# import threading
# class X(threading.Thread):
#     def run(self):         ## Thread 2
#         for p in range(100):
#             print(p)
# class Y(threading.Thread):
#     def run(self):         ## Thread 3
#         for q in range(100,200):
#             print(q)
#             print(a)       ### We are not defined a 

# x1=X()    ## Main Thread
# x1.start()
# y1=Y()
# y1.start()
# x1.start()  ## Therad can only start once 

# for r in range(200,300):
#     print(r)
# for s in range(300,400):
#     print(s)

""" ---> Here totally 3 threads 1.Main Therad 2.'X' class Thread 3.'Y' class Thread
if multiple threads are running ,if we get erroe in one thread then will effet other Thread ececution---=No
"""


""" Temparaly suspending the execution of thread :
We can suspend the execution of Thread temperarly by calling the sleep() method of time module
"""

import threading
import time       ## time module for suspending the execution

class X(threading.Thread):
    def run(self):              ## 2nd Thread
        time.sleep(10)    ## Delay or suspend the time in secounds ,sleep() present in time module for suspending
                          ## Execution for some time
        for p in range(1,101):
            print(p)

class Y(threading.Thread):
    def run(self):          ## 1st Thread
        for q in range(101,201):
            print(q)

x1=X()       ## Main Thread
x1.start()   ## Thread 2 starting and getting suspended,meanwhile Thread 3 executes,after suspend time again thread 2
y1=Y()       ## executes ,if we give less suspend time then we get mixed output
y1.start()

""" ---> If multiple threads are running ,if we get error in one thread then will efect the other thread execution
----> every time not only run() method acts as thread,normal method also behave like a thread but should be called
      run method only..
"""

# import threading
# import time        #time module----> for suspending the execution
# class x(threading.Thread):
#     def run(self):   # thread 2
#         time.sleep(10)  #delay or suspend time in seconds, sleep() present in time module for suspending
#         i=1
#         while(i<=30):  #execution for some time
#             print("PYTHON")
#             i=i+1
#         time.sleep(15)
#         for p in range(30):
#             print("hello")
#     def m1(self):
#         print("Hai")
# class y(threading.Thread):  
#     def run(self):   # thread 3
#         time.sleep(20)
#         j=1
#         while(j<=30):
#             print("JAVA")
#             j=j+1
#         time.sleep(25)
#         for p in range(30):
#             print("Good morning....") 
# x1=x()        #main thread
# x1.start() #thread 2 starts and get suspended,meanwhile thread 3 executes and after suspend time is finished 
# y1=y()     #again thread 2 excutes ,if u give less suspend time then we get mixed output
# y1.start()
# x1.m1()

# ##-----------------------------------------------------------------------------------------------------------

# #If a class have got 10 objects,then we have 10 threads

# import threading
# import time        
# class x(threading.Thread):
#     def run(self):   # thread 2
#         time.sleep(10)  
#         for p in range(1,11):  
#             print(p)
         
# class y(threading.Thread):
#     def run(self):   # thread 3
#         for q in range(11,21):
#             print(q)
# t1=x()        
# t1.start() 
# t2=y()     
# t2.start()
# t3=x()
# t3.start()
# t4=y()
# t4.start()

#here totally 5 threads, 1 main thread+ 4 threads

##-----------------------------------------------------------------------------------------------------------
""" Different ways of creating Threads : 3 Types
---->Creating the thread without using class name 
---->Creating a thtead by extending the thread class
---->Creating a thread without extending the Thread class
"""

""" 1.Creating a Thread without using any class  """

import threading

## help(threading.Thread)

def display(self):
    for p in range(1,11):
        print("Child Thread....@@ ")

## Creating object of Thread class

t1=threading.Thread(target=display)   ## Creating Thread object
t1.start()    ## Start the Thread
for p in range(1,11):
    print("Main Thread....!!!")


""" 2)Creating a Thread by extending Thread class

#we have to create a sub-class for Thread class.
#In that sub class we have to override the run() method with our logic.
#we call start() method then automaticaly run() method will be executed.   """

import threading

class mythread(threading.Thread):
    def run(self):                #Thread-2
        for p in range(10):
            print("Child Thread!!!")
t1=mythread()                    #main Thread
t1.start()
for p in range(10):
    print("Main Thread!!!")



"""Creating a Thread without extending Thread class  """

import threading
class sample:
    def display(self):
        for p in range(10):
            print(p)
s1=sample()
#creating object of pre-defined class
t1=threading.Thread(target=s1.display)  #here condtructor is invoked and  initializes target with display method
t1.start()   #here run() will be invoked and which invokes display() method
for p in range(11,20):
    print(p)




"""Functions of threading module

#1.current_thread(): It returns the current executing Thread object.

#2.getName() :IT returns the current executing thread name
#             Every thread in python has name,it may be the default name generated by python  """

import threading
import time

class x(threading.Thread):
    def run(self):
        time.sleep(10)     #Thread 2
        for p in range(10):
            print("Child Thread-1!!!")
            #print(threading.current_thread())
            print("Current Executing Thread:",threading.current_thread().getName())
            
class y(threading.Thread):
    def run(self):        #Thread 3
        time.sleep(15)
        for p in range(10):
            print("Child Thread-2!!!")
            #print(threading.current_thread())
            print("Current Executing Thread:",threading.current_thread().getName())
x1=x()          #MAin Thread
x1.start()
y1=y()
y1.start()
print(threading.current_thread())
print("Current Executing Thread:",threading.current_thread().getName())

for p in range(10):
    print("Main Thread!!!")





""" 3.setName():To set our own name for a thread  """

from threading import *

print(current_thread().getName())
current_thread().setName("demo thread")
print(current_thread().getName())












