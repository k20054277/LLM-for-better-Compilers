
# Using False as a comparison result
def is_even(num):
    """Return True if number is even, else False"""
    return num % 2 == 0

num = 5
if not is_even(num):
    print("Number is odd.")
else:
    print("Number is even.")

# Using next() as a method of list iterators
def count_elements(iterable, element):
    """Count occurrences of given element in an iterable"""
    counter = 0
    for item in iterable:
        if item == element:
            counter += 1
    return counter

numbers = [1, 2, 3, 2, 1, 2]
element = 2
count = count_elements(numbers, element)
print("Element '{}' occurs {} times in the list.".format(element, count))

iterator = iter(numbers)
next_number = next(iterator)
print("First number in the list is: {}".format(next_number))

# In this example, using False and next() together
while next_number != element:
    if not isinstance(next(iterator), int):
        raise TypeError("Expected an integer, but got a different type.")
    next_number = next(iterator)
print("Found '{}' in the list.".format(element))
