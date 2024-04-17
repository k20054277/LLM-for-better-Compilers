import time
from profiling import profile

@profile
def my_function():
    # Do some work here
    pass

if __name__ == '__main__':
    start = time.time()
    my_function()
    end = time.time()
    print(f'Time taken: {end - start}')