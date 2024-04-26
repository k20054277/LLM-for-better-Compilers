# Using as to create a new object with a different type
my_list = [1, 2, 3]
my_tuple = my_list * 2
print(my_tuple) # (1, 2, 3, 1, 2, 3)

# Using *= to multiply a value by a scalar
x = 5
y = x *= 2
print(x, y) # 10