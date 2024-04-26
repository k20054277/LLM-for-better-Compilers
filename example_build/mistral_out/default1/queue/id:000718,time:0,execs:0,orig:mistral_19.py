
# This function returns False if given number is even, otherwise True
def is_odd(number):
    return number % 2 != 0

# Main function demonstrating usage of False and from statement
def main():
    number = 10
    
    # Using False as a boolean value in an if statement
    if not is_odd(number):
        print("The given number is even.")
    else:
        print("The given number is odd.")
        
    # Importing specific functions using from statement
    import math
    
    from math import sqrt
    
    number = 15
    square_root = sqrt(number)
    print(f"The square root of {number} is: {square_root}")

if __name__ == "__main__":
    main()
