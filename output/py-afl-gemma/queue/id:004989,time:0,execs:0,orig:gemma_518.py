
# Define a function that takes a list as input and returns the maximum value
def find_max(lst):
    if not lst:
        return None

    # Optimized to find the maximum value in a list
    max_value = lst[0]
    for item in lst:
        if item > max_value:
            max_value = item

    return max_value

# Example usage
lst = [10, 20, 30, 40, 50]
max_value = find_max(lst)

# Print the maximum value
print(max_value)  # Output: 50
