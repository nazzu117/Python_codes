""" MatplotLib:- For ploting different types of graphs ,first install matplotlib module as follows
--->Matplotlib is an exteranal module we need to install by using pip
--->Install external module ------>pip install matplotlib
--->Also install pandas module --->pip install pandas
--->It install-->i)python-dateutil,ii)numpy,iii)pytz etc...
"""
##Graphs

import matplotlib.pyplot as plt   #matplotlib--->package, pyplot-->module ,plot()--->function

# plt.plot([1,3,6],[5,10,15])  # Normal 
# plt.plot([1,3,6],[5,10,15],"--")   ## doted lines like ---
# plt.plot([1,3,6],[5,10,15],"--")
# plt.plot([1,3,6],[5,10,15],"-")
plt.plot([1,3,6],[5,10,15],"v")
# plt.plot([1,3,6],[5,10,15],"_")
# plt.plot([1,3,6],[5,9,15],"*",color="red")
plt.show()



'''
Instead of the linear graph, the values can be displayed discretely by adding a format string to the plot() function. Following formatting characters can be used.

Sr.No.	Character & Description
1	
'-'    Solid line style

2	
'--'   Dashed line style

3	
'-.'  Dash-dot line style

4	
':'   Dotted line style

5	
'.'   Point marker

6	
','  Pixel marker

7	
'o'  Circle marker

8	
'v'  Triangle_down marker

9	
'^'  Triangle_up marker

10	
'<'  Triangle_left marker

11	
'>'  Triangle_right marker

12	
'1'  Tri_down marker

13	
'2'  Tri_up marker

14	
'3'  Tri_left marker

15	
'4'  Tri_right marker

16	
's'  Square marker

17	
'p'  Pentagon marker

18	
'*'  Star marker

19	
'h'  Hexagon1 marker

20	
'H'  Hexagon2 marker

21	
'+'  Plus marker

22	
'x'  X marker

23	
'D'  Diamond marker

24	
'd'  Thin_diamond marker

25	
'|'  Vline marker

26	
'_'  Hline marker

The following color abbreviations are also defined.

Character	Color
'b'	Blue
'g'	Green
'r'	Red
'c'	Cyan
'm'	Magenta
'y'	Yellow
'k'	Black
'w'	White '''