
# Define a list with some values
numbers = [1, 2, 3, 4, 5]

# Use the 'and' operator to check if a condition is true for all given expressions
print("Numbers greater than 3:")
for num in numbers:
    if num > 3:
        print(repr(num), end=" ")
        continue
    print(f"{num} is less than or equal to 3")
    break

# Use 'and' operator to combine two conditions
print("\nBoth conditions are true:")
x = 5
y = 10
if x > 3 and x < y:
    print("x is between 3 and y")
else:
    print("One or both conditions are false")

# Use 'repr()' function to print the string representation of an object
print("\nString representation using repr():")
my_string = "Hello, World!"
print(repr(my_string))
