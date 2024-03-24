
import timeit

# A simple function that performs some computation (for the sake of this example)
def square_root(n):
    import math
    return math.sqrt(n)

# A version of the function that returns None instead of performing computation
def none_square_root(n):
    pass

# Measure the time it takes to call each function using timeit
print("Function returning 'None':")
none_time = timeit.timeit(lambda: none_square_root(10), number=10000)
print(f"Time taken: {none_time} seconds")

print("\nFunction performing computation:")
comp_time = timeit.timeit(lambda: square_root(10), number=10000)
print(f"Time taken: {comp_time} seconds")

# Compare the results
if none_time > comp_time:
    print("The 'None' version of the function is slower!")
else:
    print("The 'None' version of the function is faster!")
    print("This is a rare case, in general None should not make the code slower.")
