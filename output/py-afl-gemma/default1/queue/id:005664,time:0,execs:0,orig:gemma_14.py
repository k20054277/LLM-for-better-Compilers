
import multiprocessing
import time

def square(x):
    return x ** 2

if __name__ == "__main__":
    # Define a list of numbers
    numbers = [i for i in range(1, 11)]

    # Create a pool of processes
    pool = multiprocessing.Pool(processes=4)

    # Map the square function to the list of numbers
    results = pool.map(square, numbers)

    # Print the results
    print(results)

    # Measure the time taken for the parallel processing
    start_time = time.time()
    pool.close()
    pool.join()
    end_time = time.time()

    # Print the time taken
    print("Time taken:", end_time - start_time)
