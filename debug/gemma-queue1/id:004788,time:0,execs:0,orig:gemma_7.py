
import multiprocessing

def hello(name):
    print("Hello, ", name)

if __name__ == "__main__":
    # Create a list of processes
    processes = []

    # Start a process
    for i in range(5):
        process = multiprocessing.Process(target=hello, args=("Process %s" % i))
        processes.append(process)

    # Start all processes
    for process in processes:
        process.start()

    # Wait for all processes to complete
    for process in processes:
        process.join()

    print("All processes completed!")
