
# Demonstrating the use of and and hash

# Define a function to check if a number is even and divisible by 5
def is_even_and_ divisible_by_5(num):
    return num % 2 == 0 and num % 5 == 0

# Create a dictionary to store numbers and their hashes
numbers_dict = {}

# Hash and store each number in the dictionary
for num in range(1, 11):
    hash_value = hash(num)
    numbers_dict[hash_value] = num

# Check if a number is even and divisible by 5 and get its hash
num = 6
if is_even_and_ divisible_by_5(num):
    print("Number:", num)
    print("Hash:", numbers_dict[hash(num)])
