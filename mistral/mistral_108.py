
import time

def is_even(number):
    """Return True if number is even, False otherwise."""
    return number % 2 == 0

def main():
    # Get user input for a number
    try:
        number = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    if is_even(number):
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")
        start = time.time()  # record the starting time
        for i in range(1000000):
            i * 2  # an idle loop to delay execution a bit
        elapsed = time.time() - start  # calculate the elapsed time
        print(f"Square of {number} is {number ** 2}, and it took {elapsed} seconds.")

if __name__ == "__main__":
    main()
