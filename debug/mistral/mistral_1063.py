
# Importing module using as keyword
import math as m

# Using with statement for file handling
try:
    with open('example.txt', 'r') as f:  # Open file in read mode
        print(f.read())                # Read the contents of the file
finally:
    print("File is closed")

# Multiplying two matrices using nested lists and as keyword
matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]

def multiply_matrices(matrix1, matrix2):
    result = [[0, 0], [0, 0]]

    for i in range(len(matrix1)):
        for j in range(len(matrix[0])):
            result[i][j] = sum([matrix1[i][k] * matrix2[k][j] for k in range(len(matrix1))])
            
    return result

result = multiply_matrices(matrix1, matrix2) as final_result
print(final_result)
