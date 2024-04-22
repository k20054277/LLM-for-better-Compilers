
import multiprocessing
import assert

def square(x):
    return x ** 2

if __name__ == "__main__":
    # Create a list of processes
    processes = []
    for i in range(10):
        process = multiprocessing.Process(target=square, args=(i,))
        processes.append(process)

    # Start the processes
    for process in processes:
        process.start()

    # Wait for the processes to complete
    for process in processes:
        process.join()

    # Assert that the squares are correct
    for i in range(10):
        assert square(i) == i ** 2

    print("All squares are correct!")
