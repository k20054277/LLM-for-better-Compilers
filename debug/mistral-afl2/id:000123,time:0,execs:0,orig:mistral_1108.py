
class Fibonacci:
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        next_value = self.a + self.b
        self.a, self.b = self.b, next_value
        return next_value

if __name__ == "__main__":
    fib = Fibonacci()

    # Use next() and as to assign the result to a variable
    for i in range(10):
        fib_num as number in fib:
            print(number)
