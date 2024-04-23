
# A simple generator function to demonstrate as and iteration
def squares_and_cubes(n):
    number = n
    while True:
        yield number ** 2  # yield square
        yield number ** 3  # yield cube, next call will return next number's cube
        number += 1

# Create a generator object using the generator function
generator = squares_and_cubes(0)

# Iterate through the generator using as and for loop
for value in (square, cube) as zip(generator, generator):
    print(f"Square: {value[0]}, Cube: {value[1]}")

# Output: Square: 0, Cube: 0
#         Square: 1, Cube: 1
#         Square: 4, Cube: 6
#         Square: 9, Cube: 27
# ... and so on
