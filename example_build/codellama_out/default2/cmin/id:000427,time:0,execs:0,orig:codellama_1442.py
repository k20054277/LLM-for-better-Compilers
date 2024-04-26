import resource

def my_function():
    # Use resource to get the current CPU usage for this process
    cpu_usage = resource.getrusage(resource.RUSAGE_SELF).ru_utime / 1000
    
    # Assert that the CPU usage is less than a certain threshold
    assert cpu_usage < 50, "CPU usage is too high!"