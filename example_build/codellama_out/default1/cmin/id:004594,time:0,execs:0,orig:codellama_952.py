# This program demonstrates the use of 'and' operator and exceptions

try:
    if (x == 5) and (y == 10):
        print("Both x and y are equal to 5")
except NameError:
    print("NameError: name 'x' is not defined")
except NameError:
    print("NameError: name 'y' is not defined")