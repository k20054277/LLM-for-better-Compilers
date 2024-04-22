
# Define a function with an enclosing function
def outer_function():
    x = 5

    def inner_function():
        nonlocal x
        x += 1
        print("x in inner_function: ", x)

    inner_function()
    print("x in outer_function: ", x)

outer_function()
