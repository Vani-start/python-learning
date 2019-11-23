#Unordered collection of unique elements
#Lists of not duplicated elements
#Sets are mutable

#How to declare sets, it can done by 2 ways,By {} and by set built in function


set1={1,2,3,4,4,5,6}
print(set1)


list1=[1,2,3,4,11,11,11,45,'a','a','b','c','d','d']
print(set(list1))

#Sets is mutable, we can add or remove

print(type(set1))

print(2 in set1)

print (12 in set1)

print (12 not in(set1))

set1.add(12)
print(set1)
#Add an elements

set1.remove(2)
#Remove an elements
print(set1)

#It won't allow to add duplicates elements it gives an error

set1.add(6)
print(set1)


#Sets operartions

set3={1,2,3}
set4={3,5,6}

print(set3.intersection(set4))

print(set4.intersection(set3))


print(set3.difference(set4))
print(set4.difference(set3))


print(set3.union(set4))
print(set4.union(set3))

#To remove elements
set3.pop()
print(set3)

set4.clear()
print(set4)

####Frozen sets
#This calls immutable sets, elements of the sets remains same after creation

list1=[1,2,3,4]
list2 =[4,5,6,7]

fs1=frozenset(list1)
fs2=frozenset(list2)

print(type(fs1))


## As it is frozen we cannot modify the elements

#fs1.add(6)
#fs2.remove(1)
#fs1.pop()

#Above examples given error, as we cannot modify

#But intersection,union,difference works fine

print(fs1.intersection(fs2))
print(fs1.difference(fs2))
print(fs1.union(fs2))


print(len(set1))

lis1={'a','b','c','d',1,2,3,4}
lis2={4,5}

print(lis1)


