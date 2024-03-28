
# Define a list of tuples with two integer elements
numbers = [(2, 3), (5, 7), (1, 9), (8, 2)]

# Function to check if first number is greater than 1 and second number is odd
def condition(num):
    first, second = num
    return first > 1 and second % 2 != 0

# Use map to apply the function on each tuple in the list
result = list(map(condition, numbers))

print("Numbers which satisfy the condition:")
print(result)
