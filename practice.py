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

"""


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