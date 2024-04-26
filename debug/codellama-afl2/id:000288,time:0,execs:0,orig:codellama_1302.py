# Assert statement
x = 5
y = 10

assert x < y, "The value of x ({}) must be less than the value of y ({})".format(x, y)

# Format statement
message = "The value of x is {} and the value of y is {}"
print(message.format(x, y))