                                         ## BAR GRAPHS                                 

import matplotlib.pyplot as plt

plt.bar([1,3,5,7,9],[5,2,7,8,2],label="LG")
plt.bar([2,4,6,8,10],[8,6,2,5,6],label="SONY",color="r")
plt.legend()
plt.xlabel("Bar Number")
plt.ylabel("Bar Height")
plt.title("Epic Graph\nAnother line Whoa..")
plt.show()