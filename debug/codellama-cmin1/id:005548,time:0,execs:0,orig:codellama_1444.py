import threading

def foo(n):
    # Assert that n is a positive integer
    assert isinstance(n, int) and n > 0
    
    # Acquire the mutex
    mutex.acquire()
    
    try:
        # Do some work with n
        print("Worker {} is processing...".format(threading.current_thread().name))
        
        # Release the mutex
        mutex.release()
    except:
        # Catch any exceptions and release the mutex
        mutex.release()
    
    # Return the result of the work
    return n * 2

# Create a list of threads
threads = []
for i in range(5):
    t = threading.Thread(target=foo, args=(i,))
    threads.append(t)

# Start the threads
for t in threads:
    t.start()

# Join the threads
for t in threads:
    t.join()