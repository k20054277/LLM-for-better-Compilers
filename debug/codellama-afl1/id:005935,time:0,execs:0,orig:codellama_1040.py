def my_function(x):
    return x * 2

# using as to create a new function with a different name
new_function = my_function.__code__.co_name

# using lambda to define an anonymous function
anonymous_function = lambda x: x * 3

print(my_function(5)) # prints 10
print(new_function(5)) # also prints 10
print(anonymous_function(5)) # prints