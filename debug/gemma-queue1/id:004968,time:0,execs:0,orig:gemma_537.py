
import multiprocessing

def square(x):
    return x**2

if __name__ == "__main__":
    # Create a list of processes
    processes = []

    # Assign a function to each process
    for i in range(10):
        process = multiprocessing.Process(target=square, args=(i,))
        processes.append(process)

    # Start all processes
    for process in processes:
        process.start()

    # Wait for all processes to complete
    for process in processes:
        process.join()

    # Print the results
    print("Results:")
    for i in range(10):
        print(square(i))
