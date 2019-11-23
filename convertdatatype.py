#Convet one datatype into otehr


int1=5
float1=5.5


int2=str(int1)

print(type(int1))
print(type(int2))


str1="78"

str2=int(str1)
print(type(str1))
print(type(str2))

str3=float(str1)
print(type(str3))

###Covert tuple to list
tup1=(1,2,3)

list1=list(tup1)
print(list1)
print(tup1)


set1=set(list1)
print(set1)


####bin, dec,hex


number=10

num_to_bin=bin(number)
print(num_to_bin)


num_to_hex=hex(number)
print(num_to_hex)


num_from_bin=int(num_to_bin,2)
print(num_from_bin)

num_from_hex=int(num_to_hex,16)
print(num_from_hex)


#Conversions between data types
#str() #converting to a string
#int() #converting to an integer
#float() #converting to a float
#list() #converting to a list
#tuple() #converting to a tuple
#set() #converting to a set
#bin() #converting to a binary representation
#hex() #converting to a hexadecimal representation
#int(variable, 2) #converting from binary back to decimal
#int(variable, 16) #converting from hexadecimal back to decimal


