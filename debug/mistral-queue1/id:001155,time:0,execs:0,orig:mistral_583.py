
class Counter:
    def __init__(self, value):
        self._value = value

    # Read-only property
    @property
    def is_even(self):
        return self._value % 2 == 0

# Instantiate a Counter object with an even number
counter_even = Counter(4)
print("Counter even: ", counter_even.is_even)  # Output: True

# Instantiate a Counter object with an odd number
counter_odd = Counter(3)
print("Counter odd: ", counter_odd.is_even)  # Output: False
