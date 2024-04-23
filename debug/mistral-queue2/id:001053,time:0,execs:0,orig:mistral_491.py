
# Assigning None to a variable
x = None
print("Value of x is:", x)

# Checking if None is in a list or not
my_list = [1, 2, 3, 4, None]
if None in my_list:
    print("None is present in the list")
else:
    print("None is not present in the list")

# Checking if variable is equal to None using is keyword and in keyword
if x is None or None in [x]:
    print("Variable x is None")
else:
    print("Variable x has some value")
