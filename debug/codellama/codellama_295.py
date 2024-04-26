# Demonstrate the use of False and its impact on performance

# Create a large list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Print the first element in the list
print(numbers[0])

# Use False as an index to retrieve an element from the list
print(numbers[False])

# Check the time it takes to retrieve an element using False as an index
start_time = time.time()
for i in range(1000):
    numbers[False]
end_time = time.time()
print("Time taken to retrieve element using False:", end_time - start_time)

# Check the time it takes to retrieve an element using a valid index
start_time = time.time()
for i in range(1000):
    numbers[0]
end_time = time.time()
print("Time taken to retrieve element using valid index:", end_time - start_time)