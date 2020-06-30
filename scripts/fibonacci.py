# fibonnaci function 

def fib(n):
	''' prints out a list of n fibonnaci numbers
	
	Args:
	parm1: n  is the number of fibonnaci numbers to print

	Returns:
	nothing
	'''
	print("Called from ",__name__)

	a, b = 0, 1              #Note multiple assignment!
	counter = 1
	while counter < n:
		print (a, end=' ')
		a, b = b, a+b
		print()
		counter += 1

	return(0)

################################################# #################################################
# main
# every python program has special variable that look like
# __xyz__. __name__ is one of them and has the name of the module or __main__ if it is run as a program

if __name__ == "__main__":
	n = int(input("Please enter a positive number: "))

	if n >= 0:
		fib(n)
	else:
		print("Something went wrong")
