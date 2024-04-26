
def outer_function():
    inner_value = None

    def inner_function(new_value=None):
        nonlocal inner_value
        if new_value is not None:
            inner_value = new_value

        print("Inner value: ", inner_value)
        print("Outer value: ", outer_function.counter)

    outer_function.counter = 0
    inner_function(new_value=1)
    inner_function(new_value=2)
    inner_function()

outer_function()
