
# Definition of a simple function that raises a number to the power of 2
def square_number(number):
    return number * number

# Assignment using as keyword (aliasing)
num = 5
sq_num = num  # alias num as sq_num
print("Num is: ", num)
print("Sq_num is: ", sq_num)

# Multiplying a list by a constant and assigning the result back to the list
my_list = [1, 2, 3]
my_list *= 2  # multiplies each element of my_list by 2
print("Before *= : ", my_list)
print("After *= : ", my_list)

# Applying as keyword to a function return value
result = square_number(num)
square_root = result ** 0.5  # calculate the square root
print("Result: ", result)
print("Square root: ", square_root)

# Using as for making a dictionary key an alias of another variable
x, y = 3, 4
z = {'x': x, 'y': y}
w = {'square_x': z['x'], 'square_y': z['y']}
print("Original Dictionary: ", z)
print("Modified Dictionary using as: ", w)
