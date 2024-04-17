def my_function(my_list):
    current = None
    while current is not None:
        print(current)
        current = next(my_list, None)

my_list = [1, 2, 3, 4, 5]
my_function(my_list)