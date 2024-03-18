
# Python program to demonstrate use of and and exception

# Define a function to check if a number is even and divisible by 5
def check_number(num):
    # Use and operator to check if number is even and divisible by 5
    if num % 2 == 0 and num % 5 == 0:
        return True
    else:
        return False

# Try to check if number is even and divisible by 5
try:
    num = int(input("Enter a number: "))
    if check_number(num):
        print("Number is even and divisible by 5")
    else:
        print("Number is not even and divisible by 5")
except ValueError:
    # Catch exception if input is not an integer
    print("Error: Invalid input. Please enter an integer:")
