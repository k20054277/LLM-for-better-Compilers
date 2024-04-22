# This program demonstrates the use of False and type()

# Example 1: Using False
print("Using False")
if False:
    print("This code will never be executed")

# Example 2: Type check using isinstance()
print("\nUsing isinstance() to check the type")
my_list = [1, 2, 3]
print(isinstance(my_list, list)) # True
print(isinstance(my_list, str)) # False

# Example 3: Type check using type()
print("\nUsing type() to check the type")
print(type(my_list) == list) # True
print(type(my_list) == str) # False