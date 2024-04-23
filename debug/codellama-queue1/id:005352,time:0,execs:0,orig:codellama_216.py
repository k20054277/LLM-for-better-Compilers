# Using False and iter() to iterate over a list
my_list = [1, 2, 3, 4, 5]

for item in iter(my_list, False):
    print(item)

# Output:
# 1
# 2
# 3
# 4
#