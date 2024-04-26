def demonstrate_none_and_reversed():
    # using None
    print("Using None:")
    x = 5
    if x is not None:
        print(x)

    # using reversed()
    print("\nUsing reversed():")
    list1 = [1, 2, 3, 4, 5]
    for i in reversed(list1):
        print(i)

demonstrate_none_and_reversed()