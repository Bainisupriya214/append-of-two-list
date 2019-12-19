import numpy as np
a=input("enter the list a :")
b=input("enter the list b :")
d=np.append(a,b)
print ("the append list d :",d)
for i in range (0,len(b)):
	if(b[i]>0):
		a.append(b[i])

print ("the append list c without negative values :",a)
