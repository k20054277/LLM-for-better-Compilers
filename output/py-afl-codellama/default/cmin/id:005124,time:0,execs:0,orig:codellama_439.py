# Example using None
none_example = None
if none_example is None:
    print("The value of none_example is None")
else:
    print("The value of none_example is not None")

# Example using all
all_example = [1, 2, 3, 4]
if all(i % 2 == 0 for i in all_example):
    print("All elements of the list are even")
else:
    print("Not all elements of the list are even")