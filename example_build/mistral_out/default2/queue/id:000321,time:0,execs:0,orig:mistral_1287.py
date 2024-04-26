
# Example with assert statement
def calculate_sum(num1, num2):
    """Calculates the sum of two numbers."""
    result = num1 + num2
    assert type(num1) is (int or float), "First argument must be either int or float"
    assert type(num2) is (int or float), "Second argument must be either int or float"
    return result

try:
    print(calculate_sum("three", 5))
except AssertionError as e:
    print(e)

# Example with del statement
class MyList:
    def __init__(self, items):
        self.items = list(items)

    def remove_first(self):
        """Removes and returns the first item in the list."""
        if not self.items:
            raise IndexError("Cannot remove item from an empty list")
        item = self.items[0]
        del self.items[0]
        return item

my_list = MyList([1, 2, 3])
print(my_list.remove_first())  # Output: 1
print(my_list)               # Output: [2, 3]
