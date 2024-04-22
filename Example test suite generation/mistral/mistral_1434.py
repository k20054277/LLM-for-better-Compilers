
def sum_list(numbers):
    """
    This function takes a list of numbers as an argument and returns the sum of all its elements
    :param numbers: List of numbers
    :return: The sum of all elements in the given list
    """
    total = 0
    for num in numbers:
        total += num
    return total

if __name__ == "__main__":
    test_cases = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [0],
        [10]
    ]

    for numbers in test_cases:
        result = sum_list(numbers)
        assert sum(numbers) == result, f"Test case failed. Expected: {sum(numbers)}, Actual: {result}"
        print(f"Test case passed: [{' '.join(map(str, numbers))}]")
