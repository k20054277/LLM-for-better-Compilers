import time

def profile_func(num_calls):
    # This function will be called num_calls times, so we can measure its performance
    start = time.time()
    for i in range(num_calls):
        # Do some work here to simulate a computationally expensive task
        result = 0
        for j in range(1000000):
            result += 1
    end = time.time()
    print("Time taken:", end - start)

def none_func():
    # This function returns None
    return None

# Test the performance of profile_func
num_calls = 1000
profile_func(num_calls)

# Test the performance of none_func
none_func()