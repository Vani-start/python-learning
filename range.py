#ranges 
print(range(10))

#we cannot slice the ranges, instaed we can convert range to slice and check

ran=range(10)

print(type(ran))

print(list(ran))
#convert to range to list

print(ran[0])

print(ran.index(9))

print(list(ran) [2:5])


#Ranges - unlike in Python 2, where the range() function returned a list, in Python 3 it returns an iterator; cannot be sliced
r = range(10)   #defining a range
 
r
range(0, 10) #the result
 
type(r)
<class 'range'> #the result
 
list(r) #converting a range to a list
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  #the result
 
list(r)[2:5]    #slicing a range by using the list() function first
[2, 3, 4]   #the result




