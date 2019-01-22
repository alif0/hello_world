# read and write to files
import csv

def cat(in_file):
	''' function cat similar to unix cat 

	Args:
	param1 : in_file, str containing the name of the file to read

	Returns:
	nothing
	:rtype: object

	'''

	# try / except block try to open the file 
	try:
		# initliaze the file object
		fobj = open(in_file, "r")     # "r"-read, "w"-write, "a"-append, default without anything is "r"
		for s in fobj:
			print(s.rstrip())

		# always close the file
		fobj.close()
	except FileNotFoundError:
		print("{0} does not exists!".format(in_file))
	except PermissionError:
		print("Permission error reading file : {0}".format(in_file))			
	except:
		print("Some other error reading file : {0}".format(in_file))			

	# return the dictionary
	return(0)

def out(out_file):
	''' function to write content to file

	Args:
	param1 : out_file, str containing the name of the file to write to

	Returns:
	nothing
	:rtype: object

	'''

	# try / except block try to open the file 
	try:
		# initliaze the file object
		fobj = open(out_file, "w")     # "r"-read, "w"-write, "a"-append, default without anything is "r"
		s = "Hello World from Python"
		for i in range(10):
			fobj.write(s)
			fobj.write("\n")

		# always close the file
		fobj.close()
	except FileNotFoundError:
		print("{0} does not exists!".format(in_file))
	except PermissionError:
		print("Permission error reading file : {0}".format(in_file))			
	except:
		print("Some other error reading file : {0}".format(in_file))			

	# return the dictionary
	return(0)
############################################################
# main

if __name__ == "__main__":
	file_to_read = input("Please enter the name of a file to read : ")
	print ("reading file {0}".format(file_to_read))
	#call the function
	r_c = cat(file_to_read)

	r_c = out("test_file.txt")
