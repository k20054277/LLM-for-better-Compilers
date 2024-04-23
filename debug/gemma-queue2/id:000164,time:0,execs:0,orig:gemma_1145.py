
# Define a function that returns the next number in a sequence
def next_number(n):
    return n + 1

# Create a sequence of numbers from 1 to 10
sequence = range(1, 11)

# Use as and next to iterate over the sequence and print the next number in the sequence for each number in the sequence
for number in sequence:
    print(next_number(number))
