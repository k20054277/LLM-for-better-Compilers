def get_max_and_min(my_list):
    max_value = None
    min_value = None
    for element in my_list:
        if max_value is None or element > max_value:
            max_value = element
        if min_value is None or element < min_value:
            min_value = element
    return (max_value, min_value)

my_list = [1, 2, 3, 4, 5]
print(get_max_and_min(my_list)) # prints (5, 1)