[PYTHON]
def get_unique_ids(my_list):
    return [id(x) for x in my_list]
[/PYTHON]
[TESTS]
# Test case 1:
assert get_unique_ids([]) == []
# Test case 2:
assert get_unique_ids([1]) == [42]
# Test case 3:
assert get_unique_ids([1, 2, 3, 2, 1]) == [42, 43, 44]
[/TESTS]