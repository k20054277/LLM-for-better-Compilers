
import threading

# Function to be executed in a separate thread
def long_running_operation(input):
    # Simulating a long running operation
    result = some_complex_calculation(input)
    return result

def some_complex_calculation(input):
    if not (isinstance(input, int) or isinstance(input, float)):
        raise TypeError("Input must be either integer or float")
    # Perform complex calculations here
    return input * 2

def main():
    input = 5
    # Validating the input and performing operation in the same thread
    result_sync = some_complex_calculation(input)
    assert isinstance(result_sync, (int, float))
    print("Result of synchronous operation: ", result_sync)

    # Creating a new thread for long running operation
    input_thread = 7.5
    thread = threading.Thread(target=long_running_operation, args=(input_thread,))
    thread.start()

    # Waiting for the thread to complete execution
    thread.join()

    result_async = thread.result()
    assert isinstance(result_async, (int, float))
    print("Result of asynchronous operation: ", result_async)

if __name__ == "__main__":
    main()
