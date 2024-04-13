my_list = ["apple", "banana", "cherry"]
for i, fruit in enumerate(my_list):
    if i % 2 == 0 and fruit.startswith("a"):
        print(f"Index {i}: {fruit}")