#Decorators


#Takes one function from the other functions


def decfun(deffunc):
	def callfun():
		return print("This is" + deffunc() + "Lanuguage")
	return callfun

@decfun
def deffunc():
	return "COOL"
	
deffunc()
		
		