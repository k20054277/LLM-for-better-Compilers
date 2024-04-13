import multiprocessing

def do_work(input_data):
    # Do some work here
    return input_data

if __name__ == '__main__':
    # Create a pool of workers
    pool = multiprocessing.Pool(processes=4)

    # Use the pool to process data in parallel
    results = []
    for i in range(10):
        result = do_work(i)
        results.append(result)

    # Close the pool and wait for the work to finish
    pool.close()
    pool.join()

    # Print the results
    print(results)