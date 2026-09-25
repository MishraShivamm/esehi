"""
# Exercise 1
first_name = "Tony";
last_name = "Stark";
age = 53 ; 
height = 1.85 ;
secret = input("Enter his comic name");

print("My name is" , first_name , last_name ," and my age is" , age ,
      "and my height is" , height , "AND I'm" , secret);

 # this is f string command:
print(f"My name is {first_name} {last_name} and my age is {age}and my height is {height} AND I'm {secret}");
"""



#EXERCISE 2
"""
write a sum program where there are 2 integers a and b ,
whose input we'll get from terminal. and calculate those and print it .
"""
"""
A = int(input ("enter value of A"));
B = int(input("Enter value of B"));

num = A + B;

print (num);

"""

"""
write a subtraction program where there are 2 integers a and b ,
whose input we'll get from terminal. and calculate those and print it .


Aa = int(input ("enter value of A"));
Bb = int(input("Enter value of B"));

numm = Aa - Bb;

print (numm);
"""

"""
Exercise 3:

Take price of 3 products as input (eg - 99.8, 23.56, 16.15)
. print total Bill amount
. print the average price

Take a superhero name as input & check if it starts with 's' /'S' or not.



product_price1 =  99.8;
product_price2 = 23.56;
product_price3 = 16.15;

total_price = product_price1 + product_price2  + product_price3;
avg_price = ((product_price1 + product_price2  + product_price3)/3);

print (total_price , avg_price);

name = "IronMan";
print ('s' in name);
print ('S' in name); 

"""


"""
EXERCISE 4:
Build a simple calculator which can perform addition, subtraction, multiplication, modulo and division operations on two numbers.




a = int(input("Enter value of A: "));
b = int(input("Enter value of B: "));
operation = input("Enter operation (+, -, *, /, %, **): ");

if operation == "+":
    result = a + b;
    print("Result: ", result);

elif operation == "-":
    result = a - b;
    print("Result: ", result);
elif operation == "*":
    result = a * b;
    print("Result: ", result);
elif operation == "/":
    result = a / b;
    print("Result: ", result);
elif operation == "%":
    result = a % b;
    print("Result: ", result);
elif operation == "**":
    result = a ** b;
    print("Result: ", result);
else:
    print("Invalid operation!");

"""

"""Exercise 5:
Print all odd numbers from 1 to 20.

Exercise 6:
print the table of 57.

Exercise 7:
Print alll the multiples of 3 from 1 to 50. but skip 15.

Exercise 8:
Take two integers as input a and b.
Find and print the first nmber between 1 and 1000 that is divisible by both numbers.




#exercise 5 example
print("Odd numbers from 1 to 20:")
for i in range(1, 21):
    if i % 2 != 0:
        print(i)    

# or 
num = 1 ;
while num <=20:
    print(num);
    num+=2;


#exercise 6 example
print("Table of 57:")
for i in range(1,571):
    if(i%57 == 0):
        print(i);

#or

for i in range(1, 11):
    print(i * 57);

"""

#erercise 7 example

print("Multiples of 3 from 1 to 50 (skipping 15):")
for i in range(1, 51):
    if(i == 15):
        continue
    
    if i % 3 ==0:
        print(i);