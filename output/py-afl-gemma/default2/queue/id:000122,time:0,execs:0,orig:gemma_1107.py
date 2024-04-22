
# This Python program demonstrates the use of as and bool

# Define a function to check if a number is even
def is_even(num):
    return num % 2 == 0

# Use as and bool to check if a number is even
num = 10
if is_even(num):
    print(num + " is even")

# Use as and bool to check if a string is empty
str1 = ""
if str1:
    print(str1 + " is not empty")
else:
    print(str1 + " is empty")
