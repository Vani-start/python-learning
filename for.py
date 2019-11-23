#for loop by string

Str1="Vani Vishwantha"

for index in range(len(Str1)):
	print(Str1[index])
	#print(index*2)
	#print(len(Str1))
	
#for loop by lists

List1=["rani","vani","ramya","flora","lakshmi"]

for lis_ind in List1:
	print(lis_ind)
	#print(len(List1))
	#It print each element
	
#for by range function
Venders=["ECI","CISCO","Juniper","HPE"]

for index_vend in range(len(Venders)):
	print(Venders[index_vend])


for ind,element in enumerate(Venders):
	print(ind,element)

for index_vend in range(len(Venders)):
	print(Venders[index_vend])
else:
	print("Range exceede")


#For / For Else loops - executes a block of code a number of times, depending on the sequence it iterates on; the "else" clause is optional
vendors = ["Cisco", "HP", "Nortel", "Avaya", "Juniper"]
 
for element in vendors: #interating over a sequence and executing the code indented under the "for" clause for each element in the sequence
    print(element)
else: #the indented code below "else" will be executed when "for" has finished looping over the entire list
    print("The end of the list has been reached")
    
#result of the above "for" block
#isco
#HP
#Nortel
#Avaya
#Juniper
#The end of the list has been reached
