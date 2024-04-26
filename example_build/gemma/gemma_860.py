
# This Python program demonstrates the use of and and bin operators

# Define a function to demonstrate the use of and operator
def demonstrate_and(a, b):
    # Check if a and b are both greater than 5
    if a > 5 and b > 5:
        print("a and b are both greater than 5")

# Define a function to demonstrate the use of bin operator
def demonstrate_bin(num):
    # Convert num to binary using the bin() function
    binary = bin(num)
    # Print the binary representation of num
    print("The binary representation of num is:", binary)

# Demonstrate the use of and operator
demonstrate_and(6, 7)

# Demonstrate the use of bin operator
demonstrate_bin(10)
