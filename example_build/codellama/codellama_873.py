def demo_and_map(my_list):
    # create a new list using the and operator
    new_list = [x & y for x, y in zip(my_list, my_list[1:])]
    
    # use map to apply a function to each element of the list
    result = list(map(lambda x: x**2, new_list))
    
    return result

# test the function with a few examples
print(demo_and_map([1, 2, 3])) # [1, 4, 9]
print(demo_and_map([5, 6, 7])) # [5, 36, 49]