
# An assignment with a false value
var1 = 0

# Directly using False
var2 = False

# A list with no elements, an empty string or an empty tuple are considered false in Python
var3 = []
var4 = ""
var5 = ()

def is_even(num):
    """Check if number is even"""
    return num % 2 == 0

# Using bool() function to convert other types to boolean values
num1 = 5
num2 = -3
bool_num1 = bool(num1)
bool_num2 = bool(num2)

print("Values:")
print("var1:", var1)
print("False:", False)
print("var2:", var2)
print("var3:", bool(var3))
print("var4:", bool(var4))
print("var5:", bool(var5))
print("\nNumbers:")
print("num1:", num1, "\t->", bool_num1)
print("num2:", num2, "\t->", bool_num2)
\
# Applying bool() function to other objects like lists and strings
bool_list = bool([0])
bool_empty_list = bool([])
bool_str1 = bool("Hello")
bool_empty_str = bool("")
print("\nLists and Strings:")
print("Non-empty list [0]:", bool_list)
print("Empty list:", bool_empty_list)
print("String 'Hello':", bool_str1)
print("Empty string:", bool_empty_str)

# Using False as an assignment value or in conditional statements
if not is_even(num1):
    print(num1, "is odd.")
else:
    print(num1, "is even.")
