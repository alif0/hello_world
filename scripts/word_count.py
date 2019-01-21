# read a text file and do a word count, sort it by the count and write to a file
import string
import csv


def word_count(in_file):
	''' function word_count

	Args:
	param1 : in_file, str containing the name of the file to read

	Returns:
	dictionary {word, count} pairs
	:rtype: object

	'''

	# initliaze the dictionary variable
	word_count = {}

	#needs import string
	# define a translator to remove punctuations
	translator = str.maketrans('','', string.punctuation)

	# try / except block 
	try:
		with open(in_file) as f:
			s = f.read()
		print("File {0} read successfully, bytes read: {1}".format(in_file, len(s)))
	except FileNotFoundError:
		print("{0} does not exists!".format(in_file))
	except PermissionError:
		print("Permission error reading file : {0}".format(in_file))			
	except:
		print("Some other error reading file : {0}".format(in_file))			

	# words is a list of words from the file
	# we also use lower function call to make all words lower case
	words = s.lower().split()

	# build the dictionary, loop through all words and update the word_count dict
	for word in words:

		# ignore punctuations
		word =  word.translate(translator)

		# ignore digits
		if word.isdigit():
			print("found {0}".format(word))
			continue
		count = word_count.get(word, 0)
		count += 1
		word_count[word] = count

	# return the dictionary
	return(word_count)

def sort_wc(w_c, sort_key):
	"""Sorts the dictionary and returns sorted dictionary

	Args; dictionary, 0 or 1
	0 - sort by key
	1 - sort by value

	Return
	sorted dictionary

	"""
	sorted_w_c = {}
    # sorted is a built in function and returns a sorted list
	# if sort_key is 1 - sort on value in the dictionary
	# if sort_key is 0 - sort on key in the dictionary
	if sort_key == 1:
		sorted_list = sorted(w_c, key=w_c.get, reverse = True)
	else:
		sorted_list = sorted(w_c, reverse = True)

	#build the sorted dictionary
	for word in sorted_list:
		sorted_w_c[word] = w_c[word]

	return(sorted_w_c)



############################################################
file_to_read = input("Please enter the name of a file to read for word_count : ")

#call the function

w_c = word_count(file_to_read)

sorted_w_c = sort_wc(w_c, 1)

# write to a csv file
fp = open("dict_words.csv", 'w')
wfp = csv.writer(fp)
wfp.writerow(['word', 'count'])
for key in sorted_w_c.keys():
	wfp.writerow([key, sorted_w_c[key]])


#print(sorted_w_c)

