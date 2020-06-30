"""
Created on Mon Jun 29 17:17:44 2020

@author: fali

Learning about dictionary data structure
differnce from list - it has keys instead of indices and 
they can be anything!
"""
# note what we have done below using import rather than
# coding the function printbar like we did in tuple.py
from printbar import printbar

# create a dict object
d1 = {"name": "ali", "class": "python"}
print(d1)
printbar()

for key,value in d1.items():
  print(key, value, sep=':')
  print("--------")
printbar()

# another way to create a dict object
d2 = dict({"name": "abi", "class": "devops"})
print(d2)
printbar()

# what am i doing wrong here
# d3 = {"name": ["ali"], 
#       "class": ["python", "devops", "aws"], 
#       "name": ["syed"], 
#       "class" : ["datascience", "programming", "gcp"]}

d3 = {"name": "ali", 
      "class": ["python", "devops"],
      "address": "Dallas",
      "github": "github.com/alif0"
      }
for key,value in d3.items():
  print(key, value)
  print("--------")
printbar('#')

monthNumbers = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5,
                1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May'}
print (f"The third month is: {monthNumbers[3]}")
diff = monthNumbers['Apr'] - monthNumbers['Jan']
print(f"Apr and Jan are {diff} months apart")
printbar()

# method len
print(len(d3))
printbar()

# method keys - gets you the keys of the dictionary
# not sorted!!
x = monthNumbers.keys()
print(x)
printbar()

#method values
x = monthNumbers.values()
print(x)
printbar()

#update the dictionary need the key of the item you 
# want to update
d3['name'] = 'abi'
print(d3)
printbar()

#method del
del d3['name']
print(d3)
printbar()

d3['name'] = 'qamber'
print(d3)
printbar()












