def check_if_all_elements_are_positive(my_list):
    assert all(x > 0 for x in my_list), "Not all elements are positive"

my_list = [-1, -2, -3]
check_if_all_elements_are_positive(my_list)