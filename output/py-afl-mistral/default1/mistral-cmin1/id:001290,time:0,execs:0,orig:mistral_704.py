
import threading

# Shared variable to be accessed by multiple threads
counter = 0

def increment_counter(name):
    global counter
    
    for i in range(1000):
        # Simulate some work here before the actual increment
        # e.g., some heavy computation or I/O operation
        
        # Try to increment the counter
        try:
            current_value = counter
            counter = current_value + 1
            print(f"Thread {name} incremented counter from {current_value} to {counter}")
        except Exception as e:
            print(f"Thread {name}: Error while incrementing counter - {e}")
            
# Create and start two threads
thread_one = threading.Thread(target=increment_counter, args=(1,))
thread_two = threading.Thread(target=increment_counter, args=(2,))

# Start both threads
thread_one.start()
thread_two.start()

# Wait for both threads to finish their execution
thread_one.join()
thread_two.join()

print("Final counter value: ", counter)
