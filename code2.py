"""
Type conversion : Type conversion is the process of changing a value from one data type to another. 
It can happen automatically when Python detects a mismatch during an 
operation (Implicit), or manually when the programmer forces a change 
using functions like str() or int() (Explicit).


Type Casting :Type conversion is when we use built-in functions—like 
int(), float(), or str()—to change a value from one data type into another.this is 
explicit
  
  
"""

# ****** Everything By Default jisko hum input() se input krvate hai vo as string store hota hai instead of number.


age = input("Enter age");

print (age);
age1 = int(age);
print (age1);







# String Methods

# string operations
"""
Strings in Python are immutable.which means once a string object is created in 
memory, its characters cannot be altered or rewritten. When we assign a new 
value to the same variable (like changing a = 'abc' to a = 'xyz'), Python does 
not modify the original string; instead, it creates a completely new string 
object in memory and redirects the variable to point to it.



name.find("rk");
name.replace("what you want to replace" , "with what you want to replace")


in is a keyword in python that checks the presence that means
for example 
print ('S' in name)

if S in present there in name variable it'll return True , else it'll return 
False
"""