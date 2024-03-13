
# Custom function that checks if a number is even
def is_even(num):
    return num % 2 == 0

# Function that prints a message based on whether a number is even or odd
def print_number_status(num):
    if is_even(num):
        print(f"{num} is an even number")
    else:
        print(f"{num} is an odd number")
        print("But we know that! Since False and all truth values are falsy,")
        print("we can also use False as a default argument to check if a number is odd.")

# Using False as a default argument for checking if a number is even or odd
def print_number(num=False):
    if num:
        print_number_status(num)
    else:
        print("Please provide a number")

# Testing the functions
print_number()                      # Please provide a number
print_number(5)                     # 5 is an odd number
                                   # But we know that! Since False and all truth values are falsy,
                                   # we can also use False as a default argument to check if a number is odd.
print_number(-3)                    # -3 is an odd number
print_number(6)                     # 6 is an even number
