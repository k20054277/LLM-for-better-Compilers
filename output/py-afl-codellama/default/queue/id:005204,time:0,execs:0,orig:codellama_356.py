# requirements.txt
numpy==1.20.3
pandas==1.3.5

# main.py
import numpy as np
import pandas as pd

# Define a function that takes a list of numbers and returns the sum of their squares
def square_sum(numbers):
    return np.sum(np.square(numbers))

# Print the result of calling the function with a list of numbers
print(square_sum([1, 2, 3]))