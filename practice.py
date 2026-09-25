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
Find and print the first number between 1 and 1000 that is divisible by both numbers.




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



#erercise 7 example

print("Multiples of 3 from 1 to 50 (skipping 15):")
for i in range(1, 51):
    if(i == 15):
        continue
    
    if i % 3 ==0:
        print(i);


#erecise 8 example
a = int(input("Enter first integer (a): "))
b = int(input("Enter second integer (b): "))
for i in range(1, 1001):
    if i % a == 0 and i % b == 0:
        print(i)
        break
        



"""



"""
Exercise 9:
Given a list of roll numbers :[101,102,105,101,108,105,110]. print all unique roll number in the list



Exercise 10:
given Employee records in the formof list of tuples where each tuple contains:
(Employee ID, Employee NAme, Salary).

Example - [
(101,"Alice", 50000),
(102,"Bob", 60000),
(103,"Charlie", 55000)]


Ask user to enter Employee ID and search it inside records. If the employee is not found, 
print "Employee not found".


#exercise 9 example
roll_numbers = [101, 102, 105, 101, 108, 105, 110]
unique_roll_numbers = set(roll_numbers) #The important thing about a set is: A set does not keep duplicate values.
print("Unique roll numbers:", unique_roll_numbers);




#exercise 10 example
employee_records = [
    (101, "Alice", 50000),
    (102, "Bob", 60000),
    (103, "Charlie", 55000)
]
emp_id = int(input("Enter employee Id"));
for emp in employee_records:
    if emp[0] == emp_id:
        print("Employee found:",emp)
        break


# <--------------------- OR --------------------->


employee_records = [
    (101, "Alice", 50000),
    (102, "Bob", 60000),
    (103, "Charlie", 55000)
]
employee_id = int(input("Enter Employee ID to search: "))
found = False
for record in employee_records:
    if record[0] == employee_id:
        print(f"Employee found: {record[1]}, Salary: {record[2]}")
        found = True
        break
if not found:
    print("Employee not found")


"""
"""
Exercise 11:
Write a function to check if a number is even or odd.

Exercise 12:
Write a function to count the number of vowels in a given string.

Exercise 13:
Write a function to check if the number is prime or not.


Exercise 14:
Write a function to return the average marks if a list of marks is passed as parameter to the function.


"""

#Exercise 11 example
def check_even_odd(num):
    if num %2 ==0:
        return"The number is even"
    else:
        return "The number is odd"

print(check_even_odd(5));
print(check_even_odd(20));



#exercise 12 example
def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

print(count_vowels(set("Hello, World!")));

#exercise 13 example
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

print(is_prime(17));
print(is_prime(20));


#exercise 14 example
def average_marks(marks):
    if len(marks) == 0:
        return 0
    return sum(marks) / len(marks)

print(average_marks([85, 90, 78, 92, 88]));

