
# List of tuples with two elements each, representing pairs of numbers
numbers_list = [(1, 2), (3, 4), (5, 6), (7, 8)]

# Use zip() to iterate over the pairs in numbers_list in parallel
pair_iterator = zip(numbers_list)

# Iterate through each pair using next() and unpacking
try:
    while True:
        # Get the next pair from the iterator, or raise a StopIteration if there are no more pairs
        pair = next(pair_iterator)
        
        # Unpack the pair into two separate variables, x and y
        x, y = pair
        
        print("x:", x)
        print("y:", y)

        # Perform a comparison with False, this will eventually return False when there are no more pairs left
        if not (x + y):
            break
except StopIteration:
    print("No pair found where x and y add up to zero")
