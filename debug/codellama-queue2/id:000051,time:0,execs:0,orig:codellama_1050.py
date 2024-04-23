# Using "as" to assign an alias to a variable
x = 10
y = x as int
print(y) # Output: 10

# Using "all" to check if all elements in a list are True
my_list = [True, False, True]
if all(my_list):
    print("All elements in the list are True")
else:
    print("Not all elements in the list are True")

# Using "all" to check if all elements in a list are greater than 0
my_list = [1, 2, 3]
if all(i > 0 for i in my_list):
    print("All elements in the list are greater than 0")
else:
    print("Not all elements in the list are greater than 0")