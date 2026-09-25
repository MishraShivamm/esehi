"""
Complex data types in Python are data types that can hold multiple values or collections of 
values. The most commonly used complex data types in Python are:


List : Collection of ordered, mutable (changeable) elements. Lists are defined using square brackets [] 
and can contain elements of different data types. 


Tuple : Collection of ordered, immutable (unchangeable) elements. Tuples are defined using parentheses () 
and can contain elements of different data types. 


Set : Collection of unordered, mutable (changeable) elements. Sets are defined using curly braces {}
and can contain elements of different data types. Sets do not allow duplicate elements. 


Dictionary: Collection of unordered, mutable (changeable) key-value pairs. Dictionaries are defined using curly braces {}
and can contain elements of different data types. Each key in a dictionary must be unique, and
the values can be of any data type. Dictionaries are defined using curly braces {} and key-value pairs are separated by a colon (:).


"""



#list example
#list are mutable, ordered collection of elements. They can contain elements of different data 
# types and can be modified after creation.
my_list = [1, 2, 3, "hello", True];
my_list.append(4); #  <---  adding an element to the list  --->
my_list.remove(2); #  <---  removing an element from the list  ---
my_list.insert(1, "world"); #  <---  inserting an element at a specific index  --->
print(my_list[-3:]);#  <---  slicing example  --->
print(my_list[-3]);
print(my_list, type(my_list), len(my_list));

#set example
my_set = {1, 2, 3, "hello", True};
print(my_set, type(my_set), len(my_set));

#dictionary example
my_dict = {"name": "John", "age": 30, "city": "New York"};
print(my_dict, type(my_dict), len(my_dict));


#tuple example
my_tuple = (1, 2, 3, "hello", True);
print(my_tuple, type(my_tuple), len(my_tuple), my_tuple.count(2), my_tuple.index("hello"));    