#Iterators , to traverse in the list


list1=[1,2,3,4,56,6,7,8]



my_itr= iter(list1)
print(next(my_itr))
print(next(my_itr))
print(next(my_itr))
print(next(my_itr))


#Generators controls the iteraters
#resumable sequence
#you can suspend the execution



def my_gen(x,y):
	for i in range(x):
		print("ivalue is %d " %i)
		print("y value is %d" %y)
		yield i*y
	
my_obj=my_gen(5,6)
print(next(my_obj))


gen_exp=(x for x in range(5))
print(next(gen_exp))