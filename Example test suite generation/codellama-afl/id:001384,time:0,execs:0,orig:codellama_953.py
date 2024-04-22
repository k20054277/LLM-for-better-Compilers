try:
    # code that may raise an exception
    if 1 == 2:
        print("This will never be executed")
except Exception as e:
    # handle any exception that occurs
    print(f"An exception occurred: {e}")
finally:
    # clean up or perform final actions
    print("This code always runs, regardless of whether an exception occurred or not")