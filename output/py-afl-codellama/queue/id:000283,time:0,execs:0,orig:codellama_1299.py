# This program uses assert and enumerate to iterate through a list and print each element

my_list = ["apple", "banana", "cherry"]

for i, fruit in enumerate(my_list):
    assert isinstance(fruit, str)
    print(f"{i+1}: {fruit}")