# note the looping - we set the initial value for x =10  and when the first for loop is 
# executed, it is evaluated at that time, so changing the variable x in the loop 
# does not effect that loop. Now the next time that for loop is executed at that 
# time the new value of x is used!

x = 10
for i in range(0,x):
	print(i)
	x = 5

for i in range(0,x):
	print(i)

# another example 
x = 5
# outer loop
for i in range (0, x):
	# inner loop
	for j in range(0, x):
		print(i, j)
		x = 3        # next time the inner loop is evaluted it will use this value
	


