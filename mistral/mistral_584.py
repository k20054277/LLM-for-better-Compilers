
# This function prints numbers from start to end-1 if end is given, or up to 10 if no arguments are passed
def print_numbers(start=0, end=None):
    if end is not None:
        for number in range(start, end+1):
            if number % 2 == 0:  # Print only even numbers if True is given as argument
                print(number)
    else:
        for number in range(0, 11):
            if not (number % 2):  # Print all numbers if no arguments are passed or False is given
                print(number)

# Demonstrating the usage of True and range
print("Printing even numbers from 0 to 5:")
print_numbers(start=0, end=6, condition=True)

print("\nPrinting all numbers from 0 to 10:")
print_numbers()
