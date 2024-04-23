
# This program checks if a given number is positive, zero or negative
# and prints out a message accordingly
def check_number(n):
    """
    :param n: an integer number
    :return: None
    """
    if n > 0:
        print("The number", n, "is positive.")
    elif n == 0:
        print("The number", n, "is zero.")
    else:
        print("The number", n, "is negative.")

# The main part of the program
number = 5
check_number(number)  # This will print: "The number 5 is positive."

numbers = [-3, -1, 0, 2, 6]
for num in numbers:
    if num > 0:
        print("The number", num, "is positive.")
    elif num == 0:
        print("The number", num, "is zero.")
    else:
        print("The number", num, "is negative.")
        break  # exit the loop as soon as we find a negative number
else:
    print("All numbers in the list are non-negative.")
