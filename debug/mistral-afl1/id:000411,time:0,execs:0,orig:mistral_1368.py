
def validate_ages(people):
    """
    Validates ages in a given list of tuples and raises an AssertionError if any age is negative.

    Args:
        people: A list of tuples where each tuple contains a name (str) and an age (int).

    Raises:
        AssertionError: If any age is negative.
    """

    # Use assert to validate ages
    for person in people:
        name, age = person
        assert age >= 0, f"Age of {name} ({age}) is not non-negative."

    print("Original list:")
    print(people)

    # Sort and print the sorted list
    print("Sorted list:")
    print(sorted(people, key=lambda x: x[0]))

# Create a list of tuples
people = [("Alice", 35), ("Bob", -1), ("Charlie", 25)]

try:
    validate_ages(people)
except AssertionError as e:
    print(f"Error: {e}")
