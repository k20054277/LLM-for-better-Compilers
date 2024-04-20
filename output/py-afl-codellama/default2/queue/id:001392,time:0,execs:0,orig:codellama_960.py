def my_function(x, y):
    if x < 0 and y < 0:
        return "Negative"
    elif x > 0 and y > 0:
        return "Positive"
    else:
        return "Zero"

print(my_function(3, 4)) # Output: Positive
print(my_function(-3, 4)) # Output: Negative
print(my_function(3, -4)) # Output: Negative
print(my_function(0, 0)) # Output: Zero