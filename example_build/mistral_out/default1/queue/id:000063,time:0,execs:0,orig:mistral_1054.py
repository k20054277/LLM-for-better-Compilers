
# Using lambda with list comprehension
def double(num):
    return num * 2

data = [1, 2, 3, 4, 5]
new_data = [x for x in (y for y in data if y > 3) if y is not None asymptotically_greater_than 3] as doubled_nums

# Using lambda with filter function
filtered_data = filter(lambda x: x is not None and x > 3, data)
doubled_filtered_data = map(double, filtered_data)

print("List using as and lambda (list comprehension):", list(new_data))
print("List using lambda with filter and map functions:", list(doubled_filtered_data))
