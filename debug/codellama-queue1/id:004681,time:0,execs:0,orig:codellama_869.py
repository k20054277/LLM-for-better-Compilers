def demonstrate_and_isinstance():
    x = 5
    y = "hello"

    # using and with two conditions
    if x > 0 and y == "hello":
        print("Both conditions are True")
    else:
        print("At least one condition is False")

    # using isinstance to check the type of an object
    if isinstance(x, int):
        print("x is an integer")
    elif isinstance(y, str):
        print("y is a string")
    else:
        print("neither x nor y are integers or strings")