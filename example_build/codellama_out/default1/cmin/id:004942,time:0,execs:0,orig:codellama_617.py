try:
    # code that may raise an exception
    if some_condition:
        raise SomeException("Some error message")

except SomeException as e:
    # handle the exception
    print(f"An exception occurred: {e}")

else:
    # code to be executed if no exceptions were raised
    print("No exceptions were raised.")