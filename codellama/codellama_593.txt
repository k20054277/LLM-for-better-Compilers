def my_function(x):
    try:
        if x == 0:
            raise ValueError("Zero is not allowed")
        return 1 / x
    except ZeroDivisionError as e:
        print("An error occurred:", e)
        return False

print(my_function(0)) # Output: An error occurred: Zero is not allowed
print(my_function(1)) # Output: True