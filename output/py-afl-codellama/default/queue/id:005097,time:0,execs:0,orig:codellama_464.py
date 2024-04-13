def demo_none_and_locals():
    x = 10
    y = None
    z = 20

    print(x) # Output: 10
    print(y) # Output: None
    print(z) # Output: 20

    local_variables = locals()
    for key, value in local_variables.items():
        print(f"{key} = {value}")

demo_none_and_locals()