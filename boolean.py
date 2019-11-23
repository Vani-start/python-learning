#true returns True and false returns False
var1=2
var2=2
print(var1==var2)

print(var1!=var2)

# and or operator

var3 = 3
var4 = 6

print((var1==var2) and (var3==var4))
# if both expression is true results true
print((var1==var2) or (var3==var4))
# if any expression is true which returns true


#not denying an expression
not(var1 == var2)

not(var1 == var3)

print(bool(0))
#returns false
print(bool(1.1))
print(bool(""))
print(bool(None))
print(bool({}))
print(bool([]))

#not(1 == 1) #result is False; using the NOT operator means denying an expression, in this case denying a True expression
 
#not(1 == 2) #result is True; using the NOT operator means denying an expression, in this case denying a False expression
 
#None, 0, 0.0, 0L, 0j, empty string, empty list, empty tuple, empty dictionary #these values always evaluate to False
 
#bool(None) #returns False; function that evaluates values and expressions
 
#bool(0) #returns False; function that evaluates values and expressions
 
#bool(2) #returns True; function that evaluates values and expressions
 
#bool("router") #returns True; function that evaluates values and expressions
