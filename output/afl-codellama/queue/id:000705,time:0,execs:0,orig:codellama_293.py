# Using False keyword to exit a loop
while True:
    if some_condition:
        # do something
    else:
        break

# Refactoring using early return
def some_function():
    if some_condition:
        return "something"
    else:
        return "something else"