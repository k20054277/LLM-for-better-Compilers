
# Assigning None to a variable
none_variable = None
print("Type of None: ", type(none_variable))

# Assigning None to a list
my_list = [1, 2, 3]
my_list = None
print("Type of None assigned to my_list: ", type(my_list))

# Using type() function to check types
number = 5
print("Type of number (int): ", type(number))
string = "Hello World"
print("Type of string (str): ", type(string))
boolean = True
print("Type of boolean (bool): ", type(boolean))

# Assigning None to a custom class
class MyClass: pass
my_instance = MyClass()
my_instance = None
print("Type of None assigned to my_instance of MyClass: ", type(my_instance))
