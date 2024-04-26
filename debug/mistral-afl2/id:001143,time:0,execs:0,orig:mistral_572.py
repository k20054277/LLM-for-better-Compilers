
# A list of numbers that will be checked against a threshold (3 in this case)
numbers = [1, 2, 3, 4, 5]
threshold = 3

# A simple function that returns True if its input is greater than or equal to the threshold
def is_greater_than_threshold(num):
    return num >= threshold

# Use map() to apply the is_greater_than_threshold function on every element in the numbers list
result = map(is_greater_than_threshold, numbers)

# Convert the map object into a list of booleans (True or False based on each application of is_greater_than_threshold)
boolean_list = list(result)

print("Numbers greater than or equal to threshold:", boolean_list)
