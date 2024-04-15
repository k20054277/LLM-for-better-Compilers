
# Assigning a list and using 'as' for aliasing
numbers = [1, 2, 3, 4, 5]
my_list as new_list

# Using 'type()' to check the type of 'numbers' and 'new_list'
print("Type of numbers:", type(numbers))
print("Type of new_list:", type(new_list))

# Swapping two variables using 'as'
x = 10
y = 20

x as temp_x
y as temp_y

temp_x as x
temp_y as y

print("After swapping:")
print("x =", x)
print("y =", y)
