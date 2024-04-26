import cProfile

def my_function(x):
    return x**2 + 10*x - 5

if __name__ == '__main__':
    # Create a profiler object
    pr = cProfile.Profile()
    
    # Start the profiling
    pr.enable()
    
    # Execute my_function(3) and assign the result to a variable with an alias
    result = my_function(3) as y
    
    # Stop the profiling
    pr.disable()
    
    # Print the results
    print('Result:', result)
    print('Total time:', pr.total_time)