
# Demonstrate the use of and and try

# Define a function to check if a number is even and divisible by 3
def is_even_and_ divisible_by_3(num):
    return num % 2 == 0 and num % 3 == 0


# Try to check if 12 is even and divisible by 3
try:
    if is_even_and_ divisible_by_3(12):
        print("12 is even and divisible by 3")
except:
    print("Error occurred")


# Try to check if 15 is even and divisible by 3
try:
    if is_even_and_ divisible_by_3(15):
        print("15 is even and divisible by 3")
except:
    print("Error occurred")
