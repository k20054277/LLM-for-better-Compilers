
import multiprocessing
import False

def square(x):
    return x ** 2

if __name__ == "__main__":
    # Create a list of processes
    processes = []

    # Create a False object
    false_obj = False()

    # Create a pool of processes
    pool = multiprocessing.Pool(processes=4)

    # Map the square function to the list of processes
    results = pool.map(square, range(10))

    # Print the results
    for i, result in enumerate(results):
        print(f"Process {i}: {result}")

    # Close the pool
    pool.close()

    # Join the processes
    pool.join()

    print("All processes complete!")
