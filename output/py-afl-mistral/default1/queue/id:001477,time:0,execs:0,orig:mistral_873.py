
# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use range function to generate sequence of numbers
sequence = range(len(numbers))

# Iterate through the sequence and check conditions
for index in sequence:
    # Check if the current number is even and greater than 2
    if (numbers[index] % 2 == 0) and (numbers[index] > 2):
        print(f"The number {numbers[index]} satisfies the condition.")
