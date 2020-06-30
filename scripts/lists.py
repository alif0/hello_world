"""
Created on Mon Jun 29 17:17:44 2020

@author: fali

Learning about lists data structure
"""

# note what we have done below using import rather than
# coding the function printbar like we did in tuple.py
from printbar import printbar

    
# colors is a list with 4 elements
colors = ["red", "green", "blue", "yello"]

print(colors)
printbar()

# indexing into list is similar to strings
print(colors[0])
print(colors[-1])
printbar('*')


# looping over each element of a list
for i in colors:
	print(i, end=' ')

printbar('-')

# lists are mutable! so we can update them
colors[3] = "yellow"

for i in colors:
	print(i, end=' ')

printbar('*')

# similar to strings, we can get a slice of list
print(colors[1:2])
print(colors[1:])
print(colors[:3])
printbar('*')

# lists are object and so has methods that 
# we can use. recall colors. tab will give 
# you the available methods
colors.reverse()   #does not return!
print(colors)
printbar('-')
colors.sort()
print(colors)
printbar('-')

leapyear = []
for year in range (2000, 2040):
  if (year % 4 == 0 and year % 100 !=0 ) or (year % 400 == 0):
    leapyear.append(year)

print(leapyear)
printbar('x')

#list comprehension - expression and loop
years = [x for x in range(2000, 2040)]
print (years)
printbar('y')
#list comprehension - expression and loop with condition
leapyear2 = [x for x in range(2000, 2040) if (x % 4 == 0 and x % 100 !=0 ) or (x % 400 == 0)]
print (leapyear2)
