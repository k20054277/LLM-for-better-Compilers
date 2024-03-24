
import multiprocessing

def my_function(x):
    print("Hello, world!")
    print(x)
    return None

if __name__ == "__main__":
    processes = []
    for i in range(10):
        process = multiprocessing.Process(target=my_function, args=(i,))
        processes.append(process)

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    print("All processes finished")
