#Lamda functions
#anonymous user defined functions

func1=lambda x,y: x ** y

print(func1(10,20))



#How to use this in list comprehensions



def myfunc(mylist):
	x_list=[]
	for x in range(10):
		for y in range(5):
			res= x * y
			print(res)


myfunc([10,20])



func2=lambda mylist: [x * y for x in range(10) for y in range(5)] + mylist
print(func2([10,20]))
			
