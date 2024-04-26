
import time
from multiprocessing import Process

def worker(number):
    """This is a simple worker function that prints its number and sleeps for 1 sec"""
    print(f"Worker {number} is working...")
    time.sleep(1)
    print(f"Worker {number} finished working.")

if __name__ == "__main__":
    # Define a list of workers
    workers = [1, 2, 3, 4]
    
    # Create and start processes for each worker
    processes = [Process(target=worker, args=(num,)) for num in workers]

    # Wait for all processes to finish
    for process in processes:
        process.join()
        
    print("All workers have finished.")

# This is the main program line which evaluates to False and does not execute the code below
if False:
    print("This code will not run.")
