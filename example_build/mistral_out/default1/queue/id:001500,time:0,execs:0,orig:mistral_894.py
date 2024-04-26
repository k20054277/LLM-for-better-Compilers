
import time

def is_even(number):
    """
    Check if a given number is even.
    :param number: An integer number
    :return: True if number is even, False otherwise
    """
    return number % 2 == 0

if __name__ == "__main__":
    start_time = time.time()

    number = int(input("Enter an integer number: "))

    if number > 0 and is_even(number):
        print(f"{number} is a positive even number.")
    elif number < 0 and is_even(abs(number)):
        print(f"{-number} is a negative even number.")
    else:
        print("Number is not even or not positive.")

    end_time = time.time()

    execution_time = end_time - start_time
    print(f"\nExecution Time: {execution_time:.10f} seconds")
