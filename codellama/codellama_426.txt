try:
    # some code that might raise an exception
    do_something()
except Exception as e:
    print("An error occurred:", e)
else:
    # code to run if no exception was raised
    print("No error")
finally:
    # code to run regardless of whether an exception was raised or not
    cleanup()