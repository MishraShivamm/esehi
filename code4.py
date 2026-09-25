"""
Range : The range() function is used to generate a sequence of numbers. It can
be used in for loops to iterate over a sequence of numbers. The range() function can take one, two, or three arguments. When one argument is 
provided, it generates numbers from 0 to the specified number (exclusive). When two arguments are provided, it generates numbers
from the first argument to the second argument (exclusive). When three arguments are provided, it generates numbers from the first argument to the second argument (exclusive) with a specified step size.


while : The while loop is used to execute a block of code repeatedly as long as
a specified condition is true. It checks the condition before executing the 
block of code, and if the condition is false, it exits the loop.

for : The for loop is used to iterate over a sequence (such as a list, tuple, 
or string) and execute a block of code for each item in the sequence. It is 
commonly used with the range() function to iterate over a sequence of numbers.


break : The break statement is used to exit a loop prematurely. When the break 
statement is encountered inside a loop, it immediately terminates the loop and 
transfers control to the next statement after the loop.

continue : The continue statement is used to skip the current iteration of a 
loop
"""

#Range function example
print("Range function example:")
for i in range(5):
    print(i)


num = range(1, 10, 2)  # Generates numbers from 1 to 9 with a step size of 2
print("\nRange with step size example:")
for i in num:
    print(i)



#While loop example
print("\nWhile loop example:")
count = 0
while count <= 5:
    print(count)
    count += 5
print("End code")


number = 1;
while number<=9:
    print(number * "*")
    number +=1
print("End code")