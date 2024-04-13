def demonstrate_as_and_any():
    # Example 1: Using 'as' to cast a value to a specific type
    print("Example 1:")
    num = "123"
    print(type(num))  # Output: <class 'str'>
    num_as_int = int(num)
    print(type(num_as_int))  # Output: <class 'int'>

    # Example 2: Using 'any' to check if an item is present in a list
    print("\nExample 2:")
    fruits = ["apple", "banana", "cherry"]
    print("Is 'orange' in the list of fruits?")
    print(any(x == "orange" for x in fruits))  # Output: False
    print("Is 'apple' in the list of fruits?")
    print(any(x == "apple" for x in fruits))  # Output: True