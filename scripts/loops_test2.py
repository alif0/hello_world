# find approximate square root of a positive number

# def keyword is used to define a function 

def approx_sqrt(n):
	""" function approx_sqrt

    Args:
		param1 : n - positive integer

  	Returns:
 		sqrt

	"""

	#local variables 
	epsilon = .01
	step = epsilon ** 2
	counter = 0
	sqrt = 0.0
	if ( n <= 0 ):
		n = abs(n)
		print("Finding approx sqrt of {0}".format(n)) 
	while ( abs(sqrt * sqrt - n) > epsilon):
		sqrt += step
		counter += 1
		#print("Current value of sqrt: {0} and counter: {1}".format(sqrt, counter))
		if ( sqrt > n/2 ):
			print("Error - please adjust epsilon or step")
			break

	print("Approx Sqrt of {0} is {1}".format(n, sqrt)) 
	print("Number of steps to arrive at approx: {0} with increment of: {1}".format(counter, step))

	return(sqrt)


#####################################################
n = int(input("Please enter a positive number: "))

# calling the function
approx_sqrt(n)

# the function return a value and we can use that by assigning it to a variable
k = approx_sqrt(n)
print("function approx_sqrt returned : {0}".format(k))



