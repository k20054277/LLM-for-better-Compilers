# Using False and range in Python

# Example 1: Iterating over a sequence with a default step size of 1
for i in range(5):
    print(i)

# Output: 0, 1, 2, 3, 4

# Example 2: Iterating over a sequence with a custom step size
for i in range(5, 20, 2):
    print(i)

# Output: 5, 7, 9, 11, 13, 15, 17, 19

# Example 3: Using False to stop iteration early
for i in range(5):
    if i == 3:
        break
    print(i)

# Output: 0, 1, 2, 3 (only the first four iterations are performed)