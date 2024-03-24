
def is_even(number):
    """ Returns True if given number is even, False otherwise """
    return number % 2 == 0

def print_even_numbers(start, end):
    """ Prints all even numbers between start and end (inclusive)"""
    for i in range(start, end + 1):
        if is_even(i) and i > 0: # Filter out negative numbers and zero
            print(i)

if __name__ == "__main__":
    lower_limit = int(input("Enter starting number: "))
    upper_limit = int(input("Enter ending number: "))
    
    if upper_limit < lower_limit: # Check if the ending number is greater than the starting number
        print("Invalid input! Please provide a valid range.")
    else:
        print_even_numbers(lower_limit, upper_limit)
