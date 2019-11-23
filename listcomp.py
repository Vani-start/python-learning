#List comprehensions using range
#this is to reduce the number of lines in a code and works efficient way.


list1=[]

for i in range(10):
	res=i ** 2
	print(res)
	
#How to do it in comprehension method

list2=[ x ** 2 for x in range(10)]
print(list2)

list3=[ m ** 2 for m in range(10) if m < 5]
print(list3)




#How to use in sets

set1={o ** 3 for o in range(10)}
print(set1)


#how to do it in dictionaries
#key values
dict1={ u : u ** 4 for u in range(9)}
print(dict1)
