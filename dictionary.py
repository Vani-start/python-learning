#Dictionaries are unordered data types value and key 
#MUATABLE

dict1={}

print(type(dict1))

dict1={"name" : "VANI","age":"24","height":"5.1"}

dict2={1:"first",2:"decond"}

print(dict1)
print(dict2)
#Key should be unique and immutable that means number and strings can be used

print(dict1["name"])
print(dict2[2])



#As it is mutable we can add the elemets

dict1["name"] ="RANI"
print(dict1)

del dict1["age"]
print(dict1)

print(len(dict1))


print(dict1.keys())
print(dict1.values())
print(dict1.items())

val1=print(dict1.keys())
val2=print(dict1.values())

print(list.val1())
print(list.val2())



#dict1 = {} #creating an empty dictionary
 
#dict1 = {"Vendor": "Cisco", "Model": "2600", "IOS": "12.4", "Ports": "4"}
 
#dict1["IOS"] #returns "12.4"; extracting a value for a specified key
 
#dict1["IOS"] = "12.3" #modifies an existing key-value pair
 
#dict1["RAM"] = "128" #adds a new key-value pair to the dictionary
 
#del dict1["Ports"] #deleting a key-value pair from the dictionary
 
#len(dict1) #returns the number of key-value pairs in the dictionary
 
#"IOS" in dict1 #verifies if "IOS" is a key in the dictionary
 
#"IOS2" not in dict1 #verifies if "IOS2" is not a key in the dictionary
 
#Dictionaries - methods
#dict1.keys() #returns a list having the keys in the dictionary as elements
 
#dict1.values() #returns a list having the values in the dictionary as elements
 
#dict1.items() #returns a list of tuples, each tuple containing the key and value of each dictionary pair
 


