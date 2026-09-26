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


"""