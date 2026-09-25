"""
Function in python is a block of code that is designed to perform a specific task. It can take inputs, process 
them, and return an output. Functions help in organizing code, making it reusable, and improving readability.

Types of Functions in Python:
--> in-built functions: These are the functions that are already defined in Python and can be used directly.
 examples of in-built functions are print(), len(), type(), etc.
--> User-defined functions: These are the functions that are defined by the user to perform specific tasks.
 examples of user-defined functions are def my_function():, def add_numbers(a, b):, etc.
--> Module Functions: These are the functions that are defined in external modules and can be imported and used in 
 the code.examples of module functions are math.sqrt(), random.randint(), etc.

 

Redundancy in simple terms means:

Doing or keeping something that is unnecessary because the same thing is already there or already done.
 
"""


def sum(a, b):
    return a + b
print(sum(5, 10))

def gst(price):
    total_price = price + price *0.18
    return total_price
print(gst(133))
import math

print(dir(math))  # This will print all the attributes and methods of the math module

from math import sqrt,log2
print(sqrt(16))  # This will print the square root of 16
print(log2(16))  # This will print the base-2 logarithm of 16
