
import multiprocessing
import os

def square(x):
    return x ** 2

if __name__ == "__main__":
    # Create a list of processes
    processes = []

    # Define the number of processes
    num_processes = os.cpu_count()

    # Create a shared memory object
    shared_memory = multiprocessing.SharedMemory(processes=num_processes)

    # Distribute the tasks to the processes
    for i in range(num_processes):
        process = multiprocessing.Process(target=square, args=(shared_memory.raw_value, i))
        processes.append(process)

    # Start the processes
    for process in processes:
        process.start()

    # Wait for the processes to complete
    for process in processes:
        process.join()

    # Print the results
    print(shared_memory.read())
