
def find_zero(numbers):
    i = 0
    while i < len(numbers) and numbers[i] is not None:  # Iterate until either end of list or non-None value found
        if numbers[i] == 0:
            return i  # Return index of zero as soon as it's found
        i += 1
    return None  # If no zero was found, return None

numbers = [1, 2, 3, None, 5, 6, 7, None, 9]
index = find_zero(numbers)

if index is not None:
    print("Zero found at index:", index)
else:
    print("No zero found.")
