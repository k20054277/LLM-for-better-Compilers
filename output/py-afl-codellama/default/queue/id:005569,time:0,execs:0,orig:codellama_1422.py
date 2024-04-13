import time

def test_function():
    # This function will take some time to execute
    time.sleep(5)
    return True

# Use assert to check the result of the function
assert test_function() == True

# Use cProfile to profile the execution time of the function
import cProfile
cProfile.run('test_function()')