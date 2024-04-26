numbers = [1, 2, 3, 4, 5]
for i, number in enumerate(numbers):
    print("Number {}: {}".format(i + 1, number))

# Using and operator
print("Using and operator:")
result = True
if result and numbers[0]:
    print("The number is {}".format(numbers[0]))
else:
    print("The number is not present in the list.")