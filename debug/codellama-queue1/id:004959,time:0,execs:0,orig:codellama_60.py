# This program demonstrates the use of and and global variables in Python

x = 5
y = 10

def print_and_double(n):
    # The global keyword is used to modify a global variable within a function
    global x
    
    # The and operator is used to perform a logical AND operation on two values
    if n > 0 and n < 10:
        x = n * 2
        print(f"{n} is greater than 0 and less than 10, so {x} is assigned to x")
    else:
        print(f"{n} is not greater than 0 or less than 10")
        
# Call the function with different arguments to demonstrate its behavior
print_and_double(5)
print_and_double(-1)
print_and_double(12)