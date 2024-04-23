
import multiprocessing

def square(x):
    return x ** 2

if __name__ == "__main__":
    # Create a list of processes
    processes = []

    # Create a list of tasks
    tasks = [square(i) for i in range(10)]

    # Start the processes
    for i in range(len(tasks)):
        process = multiprocessing.Process(target=tasks[i])
        processes.append(process)

    # Wait for the processes to complete
    for process in processes:
        process.start()
        process.join()

    # Print the results
    print(tasks)
