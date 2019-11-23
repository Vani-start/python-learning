#itertools
#builtin methods


from itertools import *


list1=[1,2,3,'a','b','c']
list2=[5,6,7,'x','y','z']

for i in chain(list1,list2):
	print(i)
	
print(list(chain(list1,list2)))


#count
for i in count(5,2.5):
	if i<=20:
		print(i)
	else:
		break
		
		
#cycle
#repeats the iteraters included
a=range(1,4)
for j in cycle(a):
	print(j)
		