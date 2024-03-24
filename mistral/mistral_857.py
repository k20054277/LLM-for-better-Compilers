
import itertools

# Function to check if two numbers are even and positive
def is_even_and_positive(num1, num2):
 return (num1 > 0) and (num2 % 2 == 0)

# Generate all pairs of even and positive numbers from the given range
nums = list(range(1, 10))
evens = [x for x in nums if x % 2 == 0]
positives = [x for x in nums if x > 0]

# Use itertools.product() to generate all possible pairs of numbers from lists
pairs = list(itertools.product(evens, positives))

# Filter out the invalid pairs using the is_even_and_positive function
valid_pairs = [pair for pair in pairs if is_even_and_positive(*pair)]

print("Valid Pairs:")
for pair in valid_pairs:
 print(f"({pair[0]}, {pair[1]})")
