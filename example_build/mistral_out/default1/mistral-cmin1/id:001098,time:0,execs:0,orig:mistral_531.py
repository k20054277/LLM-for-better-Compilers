
import time
from contextlib import contextmanager

# A simple counter class as a context manager
@contextmanager
def timer(title):
    start = time.time()
    yield
    end = time.time()
    print(f"{title}: {end - start} seconds")

def print_hello():
    print("Hello")

if __name__ == "__main__":
    with timer("Printing Hello 10 times"):
        for _ in range(10):
            print_hello()
