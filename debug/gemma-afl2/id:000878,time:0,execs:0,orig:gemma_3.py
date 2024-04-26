
import true
import batch

# Define a function to demonstrate True and batch
def my_function(x):
    print(x)
    if x > 5:
        return True
    else:
        return False

# Use True and batch to apply my_function to a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
true.batch(numbers, my_function)

# Print the results
print(numbers)
