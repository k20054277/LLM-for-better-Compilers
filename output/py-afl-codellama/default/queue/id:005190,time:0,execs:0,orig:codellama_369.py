import threading

# create a shared counter variable
counter = 0

# create a mutex object
mutex = threading.Lock()

def increment_counter():
    global counter
    
    # acquire the lock on the mutex
    with mutex:
        # increment the counter
        counter += 1
        print(f"Incremented counter to {counter}")

def decrement_counter():
    global counter
    
    # acquire the lock on the mutex
    with mutex:
        # decrement the counter
        counter -= 1
        print(f"Decremented counter to {counter}")

# create two threads that increment and decrement the counter
thread1 = threading.Thread(target=increment_counter)
thread2 = threading.Thread(target=decrement_counter)

# start the threads
thread1.start()
thread2.start()

# join the threads with the main thread
thread1.join()
thread2.join()