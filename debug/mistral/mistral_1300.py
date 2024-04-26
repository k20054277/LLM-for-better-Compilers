
# A counter variable in outer scope
counter = 0

def recursive_function():
    # Use nonlocal to access and modify the counter variable
    nonlocal counter

    if counter > 5:
        assert False, "Recursion depth exceeds limit ({}), aborting".format(counter)

    counter += 1
    print("Recursive call #{:}".format(counter))
    recursive_function()

# Call the recursive function
recursive_function()
