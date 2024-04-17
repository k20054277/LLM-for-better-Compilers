def check_condition(x):
    if x > 0 and x < 10:
        pass
    else:
        print("The value of x is not between 0 and 10.")

check_condition(-5)  # Output: The value of x is not between 0 and 10.
check_condition(5)   # No output