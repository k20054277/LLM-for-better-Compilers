
import time
import multiprocessing as mp

def is_even(n):
    """Return True if number n is even."""
    return n % 2 == 0

def worker(task_queue, result_queue):
    """A worker process that checks for even numbers in a task queue."""
    while True:
        try:
            number = task_queue.get()
        except mp.queues.Empty:
            continue

        if is_even(number):
            result_queue.put(True)
        else:
            result_queue.put(False)

if __name__ == "__main__":
    # Set up queues and processes
    task_queue = mp.Queue()
    result_queue = mp.Queue()

    workers = 4  # Number of worker processes
    processes = [mp.Process(target=worker, args=(task_queue, result_queue)) for _ in range(workers)]

    for process in processes:
        process.start()

    # Generate and send tasks to the worker processes
    numbers = list(range(100))  # A list of numbers to check
    for number in numbers:
        task_queue.put(number)

    # Wait for all tasks to be processed
    for _ in range(len(numbers)):
        _ = result_queue.get()

    # Terminate the worker processes
    for process in processes:
        process.terminate()

# Print the results
print("Even numbers found:")
for number in numbers:
    if number % 2 == 0:
        print(number)
