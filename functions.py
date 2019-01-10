# Functions
# Need to know what the function will do!
# name the function sensibly so its easier to get an idea on what it does - can use longer name if required
# function parameters
# function return code, data
# function is defined with "def" keyword and the function body is indented accordingly
# Any thing between """ (three quotes) is call a docstring - this really a cool documentation 
# tool and if then type help(function) it will print out the docstring

def days_diff(day1, day2):
     """ (int, int) -> int
     Return the number of days between day1 and day2, which are
     both in the range 1-365

     >>> days_diff(200, 224)
     24
     >>> days_diff(50, 50)
     0
     """

     return(day2-day1)

help(days_diff)
