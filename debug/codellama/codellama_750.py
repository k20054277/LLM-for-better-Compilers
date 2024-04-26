def demonstrate_true_and_exception():
    try:
        # This code will raise an exception
        raise ValueError("This is a test exception")
    except Exception as e:
        # Handle the exception
        print(f"Exception occurred: {e}")
    else:
        # This code will not be executed because of the exception above
        print("This code will not run")