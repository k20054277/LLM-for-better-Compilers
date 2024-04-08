
import numpy as np

# Creating two random 2x2 matrices
matrix1 = np.random.rand(2, 2)
matrix2 = np.random.rand(2, 2)

print("Matrix 1:\n", matrix1)
print("\nMatrix 2:\n", matrix2)

# Element-wise 'and' operation on matrices (does element-wise comparison and returns the equivalent of Python list '[]' style boolean and):
element_wise_and = np.logical_and(matrix1, matrix2)
print("\nElement-wise AND:\n", element_wise_and)

# Logical indexing using 'and' (returns rows where all elements are true):
rows_with_both_conditions = np.where(np.all(matrix1 >= 0.5, axis=1), matrix1, 0)
print("\nRows in Matrix 1 where ALL elements > 0.5:\n", rows_with_both_conditions)
