"""  sub() :for substitutions  """
# #To print date and month
# import re
# regex="([a-zA-Z]+) (\d+)" #extracts month and also date bcoz both r in parenthesis 
# print(re.sub(regex,r"\2 of \1","June 15,August 9,Dec 22,Jan 31,Feb 21"))
# #\2 of \1, means 15 of June,means 2nd pattern extracted first and then extracts 1st pattern
# #To print each in separate line 

# #help(re)

""" to print month and date in a seperate lines  """
# import re
# regex="([a-zA-Z]+) (\d+)"
# x=re.sub(regex,r"\2 of \1","June 15,August 9,Dec 12,Jan 31")#x stores o/p of sub----->15 of June,...
# print(x)
# regex1="\d+ [a-zA-Z]+ [a-zA-Z]+" # RE for--->15 of June
# matches=re.findall(regex1,x)
# for match in matches:
#     print(match)

print("\n\n")
""" If i want only month then keep the pattern in bracket """
# regex="([a-zA-Z]+) (\d+)"
# x=re.sub(regex,r"\2 of \1","June 15,August 9,Dec 12,Jan 31")#x stores o/p of sub----->15 of June,...
# regex1="\d+ [a-zA-Z]+ ([a-zA-Z]+)" # RE for--->15 of June
# matches=re.findall(regex1,x)
# for match in matches:
#     print(match)

# import re
# regex="([a-zA-Z]+) (\w+)"
# x=re.sub(regex,r"\2 is capital of \1","Telangana Hyderabad,Ap Amaravathi,Karnataka Bengluru,maharashtra Mumbai")#x stores o/p of sub----->15 of June,...
# print(x)

# import re
# regex="([a-zA-Z]+) (\w+) (\d+)"
# x=re.sub(regex,r"\2 capital of \1 has covid cases of \3","Telangana Hyderabad 15000,Ap Amaravathi 25000,Karnataka Bengluru 30000,maharashtra Mumbai 40000")#x stores o/p of sub----->15 of June,...
# print(x)
# print("\n")
# #ex:2
# x=re.sub(regex,r"\1 has covid cases of \3","Telangana Hyderabad 15000,Ap Amaravathi 25000,Karnataka Bengluru 30000,maharashtra Mumbai 40000")#x stores o/p of sub----->15 of June,...
# print(x)