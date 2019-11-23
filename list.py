#sequence of elements enclosed in [ ], it can be any datatypes(strings,numbers,tuples etc etc
#lists are mutable
#its like a string,index starts with 0


#declaring an empty list, 
list1=[]

print(list1)

#which returns type
print(type(list))

list2=["VANI",32,32.5,-1]
str1="list2 elements"
print(str1)
print(list2)

print(list2[1])
list2[0]="RANI"

print(list2)

print (list2[-1])


#print ( list(-32))
#indexbound error


#######LIST functions#########################
list9=[1,4,6]

#max_value=max(list9)
print(max(list9))
#It returns max value in the list
print(min(list9))
#It returns min value in list


let_str=['a','b','c']
print(min(let_str))
#This returns min string value
print(max(let_str))
#This returns max string value

print(len(let_str))
#This returns length of the list

value_list=['VANI',23,45,'9']

value_list.append(100)
print(value_list)
#Appends the value


del value_list[2]
#Should pass the index , it removes the index file
print(value_list)


#POP
value_list.pop(0)
print(value_list)

#Removing elements
value_list.remove('9')


#INSERT
value_list.insert(3,'RANI')
print(value_list)


#EXTEND
list02=[123,34,'VANI']
value_list.extend(list02)
#insert list1 to list2
print(value_list)

#INDEX
print(value_list.index('VANI'))

#COUNT
print(value_list.count('VANI'))

#SORT
list_el=[23,12,45,89,34]
list_el.sort()
print(list_el)

#Reverse
list_el.reverse()
print(list_el)

#SORTED
new_b=sorted(list_el)
print(new_b)

new_rev=sorted(new_b, reverse=True)
print(new_rev)



#ADDING list
print(new_b+new_rev)


print(new_rev *3 )


####SLICING, this is similar to string slicing

list_slice=[1,2,3,'a','b','c']

print(list_slice[1:3])

print(list_slice[-1:])
print(list_slice[-3:])
print(list_slice[::2])
print(list_slice[::-1])

print(list_slice[-3:-1])

print(list_slice[:])







