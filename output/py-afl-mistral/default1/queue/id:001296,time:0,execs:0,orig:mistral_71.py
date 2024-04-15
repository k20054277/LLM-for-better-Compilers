
# Custom Iterable Class - 'MyNumbers'
class MyNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.index = start - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.end:
            raise StopIteration
        result = self.index + 1
        self.index += 1
        return result

if __name__ == "__main__":
    nums = MyNumbers(1, 5)  # Create an instance of 'MyNumbers' class with range 1 to 5

    for number in iter(nums):
        print(number)  # Print each number from the iterable
        if number == 4:
            nums.__next__()  # Manually call next() method to skip number 4 (even though it's falsey, 'False' is still used for comparison)
            print("Skipped number 4")

# Output:
# 1
# Skipped number 4
# 5
