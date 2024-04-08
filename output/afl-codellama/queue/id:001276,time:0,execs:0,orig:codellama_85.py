def my_function(x):
    return x**2

print(my_function(5))  # Output: 25

if callable(my_function):
    print("The function is callable")
else:
    print("The function is not callable")

if my_function and callable(my_function):
    print("The function is both callable and true")