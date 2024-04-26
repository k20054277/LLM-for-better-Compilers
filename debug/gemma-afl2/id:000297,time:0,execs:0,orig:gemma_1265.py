
# Scripting with As

# Define a function to square a number
def square(x):
    return x ** 2

# As a shortcut to assigning and calling a function
a = square(5)
print(a)

# As a way to simplify a loop
for num in range(1, 6):
    print(square(num))

# As a way to add a prefix to a variable
b = "hello"
print("Mr. " + b)
