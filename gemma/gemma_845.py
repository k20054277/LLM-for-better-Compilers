
# Define a function using lambda
square = lambda x: x**2

# Print squares of numbers from 1 to 5 using Lambda and and
print( ",".join(str(square(x)) for x in range(1, 6)) )
