#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 11:35:16 2020

@author: fali

Learning about tuple data structure
"""

# simple function to print a line of char
def printbar(char = '-'):
    """Print a line of char"""
    print(char * 40)
    
    
# create an empty tuple
t1 = ()
t2 = (1, 'two', 3)
t3 = ('hello', 3, 3.4)

print(t1)  
print(t2)
print(t3)
printbar()

# we can use + with tuples
t4 = t1 + t2
t5 = t2 + t3

# notice the print statements below!
print("t4", t4)
print(f"t5 {t5}")
printbar()

# can we use * with tuples?
t6 = t4 * 6
print(f"t6: {t6}")
printbar()

# tuples are immutable!
#t4[0] = 2
print(f"t4: {t4}")

#but you can do something like this why?
t4 = t4 * 2
print(f"t4: {t4}")
#because when we have an assignment its by reference 
#by reference we mean t4 points to location in memory
#where the object was created! remember we said everything
#in python is an object!

#slicing similar to strings
print(f"slice of t4: {t4[1:3]}")
print(f"slice of t4:{t4[3:]}")
printbar()
