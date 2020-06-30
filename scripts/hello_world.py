#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 17:17:44 2020

@author: fali
"""


print(__name__)




def fib(n):
    """prints fibonacci sequence 
       pass a number to the function fib(x)
    """

    a, b = 0, 1    #Note multiple assignment!
    counter = 1
    
    while counter < n:
        print (a, end=' ')
        a, b = b, a+b
        counter += 1
        
    print(a)
    print(__name__)
    return(0)

if __name__ == "__main__":
    fib(8)