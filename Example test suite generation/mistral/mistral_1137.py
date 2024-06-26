
import time

def square_numbers(numbers):
    """
    Square each number in the list
    :param numbers: List of numbers
    :return: List of squared numbers
    """
    return [i * i for i in numbers]

if __name__ == "__main__":
    # Define a list of numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Measure the time before calling the function
    start_time = time.time()

    # Call the function and store the result
    squared_numbers = square_numbers(numbers)

    # Measure the time after calling the function
    end_time = time.time()

    # Calculate the execution time
    execution_time = end_time - start_time

    # Print the result and execution time
    print("Squared numbers: ", squared_numbers)
    print(f"Function execution time: {execution_time} seconds")
