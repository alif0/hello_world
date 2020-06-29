#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 17:17:44 2020

@author: fali
"""

for i in range(0, 100, 5):
    print(i**2)


# y = 'Hello'
# y * 5
# y * 5.0

w = 5 / 3
x = 5.0 / 3
y = 5.0 // 3.0
z = 5 % 3
print(w, x, y, z)

# Variable points to the "object" (unlike C it does not hold the value)
# y = 'Hello'
# z = 'hello'
# print(id(y), id(z))

# a = 'Hello'
# b = 'Hello'
# print(id(a), id(b))


# Boolean (True, non 0 value,  False, 0 value)
if ( 5 ):
	print("Five")
	print("True")

if ( 0 ):
	print("Zero")
	print("False")

if (not 0):
	print("Not Zero")

# combining boolean expressions with: and, or, not
# comparison operators: ==, <=, >=, !=, <, >
print( 4 > 5)
print ( 4 <= 5 )

exitCode = 'exit'
ans = ''
while (str(ans) != exitCode):
	ans = input("Please enter your names or exit to exit out of the loop: ")
	if (str(ans) != exitCode):
		print("Hello", ans)

name = ("Ali", "Abu Ali", "Joe", "Abu Joe")
print(name)

