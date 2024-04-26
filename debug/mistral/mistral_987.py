
import threading

# Function for printing even numbers
def print_evens():
    for i in range(0, 11):
        if i % 2 == 0:
            print(i, end=" ")

# Function for printing odd numbers
def print_odds():
    for i in range(0, 11):
        if i % 2 != 0:
            print(i, end=" ")

# Create two Thread objects for even and odd number printing tasks
thread_even = threading.Thread(target=print_evens)
thread_odd = threading.Thread(target=print_odds)

# Start the threads
thread_even.start()
thread_odd.start()

# Wait for both threads to finish their tasks
thread_even.join()
thread_odd.join()

print("\nThreads finished executing.")
