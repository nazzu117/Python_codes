import matplotlib.pyplot as plt

x1=[1,2,3]
y1=[5,7,4]

x2=[1,2,3]
y2=[10,14,12]

plt.plot(x1,y1,label="First Line")
plt.plot(x2,y2,label="Secound Line")
plt.xlabel("Plot Number")
plt.ylabel("Important Var")
plt.title("Intrest Graph\ncheck it out")   ## Title for the graph
plt.legend()  ## For line indicator i.e, 1st line which color and 2nd line which color
plt.show()
