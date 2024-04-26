import sys

# create a list of integers
my_list = [1, 2, 3, 4, 5]

# create a memoryview from the list
mv = memoryview(my_list)

# check that the memoryview is not empty
assert mv.nbytes > 0

# print the first element of the memoryview
print(mv[0])