"""

# Sum of Two Numbers

a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
sum = a + b
print("SUM = ", sum)


# Even or Odd

num = int(input("Enter the number:"))
if num %2 ==0:
    print("The number is Even")
else:
    print("The number is Odd")



#Take three integers and print the largest number without using max().

a = int(input("Enter first number : "))
b= int(input("Enter second number : "))
c = int(input("Enter third number : "))

if a> b and a > c:
    print("The largest number is:", a)
elif b > a and b > c:
    print("The largest number is:", b)
else:
    print("The largest number is:", c)



# Grade Calculator
#Take marks from 0 to 100. Print A for 90+, B for 75–89, C for 60–74, D for 40–59, otherwise F.
marks = int(input("Enter your marks: "))
if marks>=90:
    print("Grade: A")
elif marks>=75 and marks<90:
    print("Grade: B")
elif marks>=60 and marks<75:
    print("Grade: C")
elif marks>=40 and marks<60:
    print("Grade: D")   
else:
    print("Grade: F")




# Multiples
# Take n and print all multiples of n from 1 through 10.

num = int(input("enter your number : "))
nm = range(1,11,1)

for i in nm:
    print(num *i)




#Count Vowels
#Take a string and count how many vowels (a, e, i, o, u) it contains, ignoring case.
string = input("Enter a string: ")
vowels = "aeiou"
count = 0
for char in string:
    if char.lower() in vowels:
        count += 1
print("Number of vowels:", count)




#Reverse a String
#Take a string and print it reversed.

string_name = input("Enter a string: ")
reversed_input = string_name[::-1]
print("Reversed string:", reversed_input)

"""


#Number Guessing Game
#Generate a random integer from 1 to 20. Give the user 5 attempts and report whether they guessed it.

import random


num = random.randint(1,20)
guess = 0
attempts = 0

while attempts <= 5:
    guess = int(input("Enter your guess: "))

    if guess == num:
        print("You guessed it right!")
        break
    else:
        print("Wrong guess! Try Again.")
        attempts += 1

    if attempts == 5:
        print("You are out of attempts!")
        print("The number was:", num)