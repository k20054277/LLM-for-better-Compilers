# Use False to simulate a failure
try:
    # This block will always raise an exception
    raise Exception("This is a simulated failure")
except:
    print("The except block was executed!")