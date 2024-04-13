import threading
import time

def my_function(x):
    if x == 0:
        return False
    else:
        return True

def main():
    # Create a list of threads to run the function on
    threads = []
    for i in range(10):
        t = threading.Thread(target=my_function, args=(i,))
        threads.append(t)
    
    # Start the threads and wait for them to finish
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    
    # Print the results
    print("Results:")
    for i, t in enumerate(threads):
        print(f"Thread {i}: {t.result}")