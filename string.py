#strings declaration
#IMMUTABLE


#we can declare it by ' '
string1 = 'Hello string1'

#we can declare it by " "
string2 = "Hello string2"

#we can declare it by ''' '''
string3 ='''hello
str3'''

#\ represents escaping charecter
#\n newline charecter
string4 ='''hello\
str3\
hi'''

print(string1)

print(string2)

print(string3)

print(string4)


################################STRING OPERATIONS################################

#len
len_str=len(string1)

print(len_str)

#INDEX

ind_str=string1[3]
print(ind_str)
#this returns index value

#right to left index, last charecter of index is -1
ind_str1=string1[-1]
print(ind_str1)
#This returns value of index


######################STRING Methods############################################

####1.index, returns the index
ind_str1=string1.index("l")
print(ind_str1);

####2.count , returns the count of cahrs
cnt_str=string1.count("str")
print("Count is")
print(cnt_str);

##returns 0 if it is not exist
cnt_str3=string1.count("xy")
print("not found char")
print(cnt_str3)


####3.find, returns the index in which it find
fin_str2=string2.find("Hel")
print(fin_str2)

###4 lower, converts string into lower case
lower_case=string1.lower()
print("To lower")
print(lower_case)

###4 upper, converts string into lower case
upper_case=string1.upper()
print("To upper")
print(upper_case)

###5 starts with, this returns true if it is exists, or else false

strt1=string1.startswith("H")
print(strt1)
strt2=string1.startswith("xc")
print(strt2)


####6 ends with

strt3=string1.endswith("1")
print(strt3)
strt4=string1.endswith("g")
print(strt4)

#####7 strip,

string4="   Hellow world   "
strip_str=string4.strip()
print(strip_str)

string5="$$$$I am strong$$$"
strip_srt=string5.strip("$")
##removes $ in o/p
print(strip_srt);

#####8 replace , replaces " " by single empty
replace_srt=string4.replace("H", "")
###above it replcae H by empty string
print(replace_srt)


#####9 split, splits string into substring
planet="earth,jupiter,mars,uranus"
split_planet=planet.split(",")
print(split_planet)


####10 join, its interesting
###It joins_ by each of charecter
my_name="VANI"
join_name="_".join(my_name)
print(join_name)

###########################################################################################333

###Concat
212.203
212.202
var1="VANI"
var2="Vishwanath"

result=var1+var2
print(result)

res=3*var1
print(res)


###################################################################################333333
#############Printing string,String format
print("Printing string %s,printing num %d,printing float %f" % ("VANI",2,12.4))

####To avoid printing decimal value of float use this 
print("Printing string %s,printing num %d,printing float %.1f" % ("VANI",2,12.4))
print("Printing string %s,printing num %d,printing float %.2f" % ("VANI",2,12.4))

print("Printing string {},printing num {},printing float {}" .format("VANI",2,12.4))
##we can put .format also

print("Printing string {0},printing num {1},printing float {2}" .format("VANI",2,12.4))
##We can pass arguments also

print("Printing string {2},printing num {1},printing float {2}" .format("VANI",2,12.4))


#####fstrings

name="vani"
Age=24
floa_val=12.8

print(f"name is {name}, Age is {Age},float value is {floa_val}")

###Above f strings which allows value inside the {} and also does its operations


print(f"name is {name}, Age is {Age *3},float value is {floa_val}")

print(f"name is {name.upper()}, Age is {Age *3},float value is {floa_val}")


#########Slice###################

###To extract substring
str_variable="ip address is 147.234.158.240/20 ethernet eth0"

# before : from which index which should starts
##after : to which it should end
print(str_variable[13:28])
##[start : stop: step]

print(str_variable[13:])
#it slices from 13th index and prints rest

print(str_variable[:13])
#it slices ends 13th index and prints rest

print(str_variable[-1])
print(str_variable[-4:-1])

print(str_variable[:])

print(str_variable[::])

print(str_variable[::2])
##Slices every 2nd chars,keeps every chars of string

##How to print it reverse very inp
print(str_variable[::-1])


var="0123456789"

print(var[::2])
##It slices atarts from string 0 and steps 2

print(var[1::2])
##It starts slicing from index 1 and skips 2

print(var[1:7:2])
##It start skip from index 1 and don't inclusde 7

print(var[-2:-1])

print(var[::-1])











