def my_function(x, y):
    if x > 0 and y > 0:
        print("Both x and y are positive.")
    elif x < 0 and y < 0:
        print("Both x and y are negative.")
    else:
        print("At least one of x or y is not positive or negative.")

my_function(3, 4)  # prints "Both x and y are positive."
my_function(-3, -4)  # prints "Both x and y are negative."
my_function(3, -4)   # prints "At least one of x or y is not positive or negative."