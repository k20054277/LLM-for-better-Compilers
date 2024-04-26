
import contextlib

@contextlib.contextmanager
def timer(label):
    start = time.perf_counter()
    yield
    end = time.perf_counter()
    print(f"{label} took {end - start:.4f} seconds.")

@timer("Function call")
def square(num):
    return num * num

if __name__ == "__main__":
    result = square(5)
    print(result)
