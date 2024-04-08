
import time

# Function to be tested for performance and correctness
def square_numbers(numbers):
"""
This function takes a list of numbers and returns a new list with each number squared.
"""
 result = []
 for num in numbers:
 result.append(num ** 2)
 return result

# Function under test using assert statement
def square_numbers_assert(numbers):
"""
This function takes a list of numbers and returns a new list with each number squared.
It uses an assert statement to ensure the input is a list.
"""
 assert isinstance(numbers, list), "Input must be a list."
 result = []
 for num in numbers:
 result.append(num ** 2)
 return result

if __name__ == "__main__":
 print("Performance test:")
 numbers = [i for i in range(1000)]
 start_time = time.time()
 square_numbers(numbers)
 end_time = time.time()
 print(f"Time taken by square_numbers function: {end_time - start_time} seconds")

 print("Correctness test:")
 numbers = [1, 2, 3]
 assert square_numbers_assert(numbers) == [1, 4, 9], "square_numbers_assert function failed"
 print("All is well.")
