
# This is a Python script that demonstrates the use of 'as' keyword and comments.

# Importing NumPy library using 'as' keyword for aliasing it as 'np'
import numpy as np

# Creating a NumPy array with some random data for demonstration
data = np.array([3, 5, 7, 11, 15])

# Applying an operation on the NumPy array using 'np' alias
square_data = np.square(data)

# Printing the original and squared arrays with comments for better understanding
print("Original Array:")
print(data)
print("\nSquared Array:")
print(square_data)

# Comment explaining that the following code block calculates the mean of the squared array using 'np.mean()' function
"""
Calculating the mean of the squared array using NumPy's 'np.mean()' function
"""
average_square = np.mean(square_data)

# Printing the average of squared numbers with a comment for better understanding
print("\nAverage of Squared Numbers:")
print(average_square)
