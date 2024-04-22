# Using `as` to create an alias for a variable or object
x = 10
y = x
print(y) # prints 10

x = "hello"
y = x
print(y) # prints "hello"

# Using `enumerate` to iterate over a list and get the index and value of each element
my_list = [1, 2, 3, 4, 5]
for i, v in enumerate(my_list):
    print(f"Index: {i}, Value: {v}")
# Output:
# Index: 0, Value: 1
# Index: 1, Value: 2
# Index: 2, Value: 3
# Index: 3, Value: 4
# Index: 4, Value: