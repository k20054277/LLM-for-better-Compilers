
class Counter:
    def __init__(self, count=0):
        self.count = count

    def increment(self, value=1):
        """Increment the counter by a given value."""
        self.count += value

    def square(self):
        """Square the current count."""
        assert self.count >= 0, "Error: The count must be non-negative"
        self.count **= 2

counter = Counter()
print("Initial counter:", counter.count)
counter.increment(5)
print("Counter after incrementing by 5:", counter.count)
counter.square()
print("Counter squared:", counter.count)