a=[1,2,3]
b=[4,5,6]
##c=a+b contatinate two lists
##print(c)
##a.append(b) append the new list as an element at the end of current list
##a.append(4)#append new number at the end of list
a.extend(b) # ?? extend only takes one argument
a.append(1) # ?? append only takes one argument 
a.append(b) 
a.extend([0])
a.extend(b)


