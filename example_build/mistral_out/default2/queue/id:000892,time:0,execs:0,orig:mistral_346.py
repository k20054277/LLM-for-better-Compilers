
# List of numbers with some elements as None
numbers = [1, 2, 3, None, 5, None, 7]

# Using sum() function to add up all the numbers in the list excluding the None values
total_sum = sum(filter(None, numbers))

print("Total Sum of non-None numbers: ", total_sum)
