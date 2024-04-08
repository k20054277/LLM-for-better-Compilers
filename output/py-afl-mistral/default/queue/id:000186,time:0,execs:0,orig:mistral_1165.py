
from multiprocessing import Pool, Process
import time

def func(arg):
    """A simple function that takes some time."""
    print(f'Function {arg} started')
    time.sleep(2)
    print(f'Function {arg} finished')
    return arg * 2

if __name__ == '__main__':
    args = [1, 2, 3, 4]

    # Creating a process pool with 4 processes
    with Pool(processes=4) as pool:
        results = pool.map_async(func, args)

        print('Process pool started')
        print('Waiting for all processes to finish')
        pool.close()
        pool.join()

        print('All processes finished')
        print('Results:', results.get())

        # Simulating a long running task by sleeping for some time
        time.sleep(5)

# Output will look something like this:
# Process pool started
# Function 1 started
# Function 2 started
# Function 3 started
# Function 4 started
# Waiting for all processes to finish
# All processes finished
# Results: [2, 4, 6, 8]
