
# filename: my_function.py
def get_default_list(input_list=None):
    if input_list is None or len(input_list) == 0:
        return None
    else:
        return input_list
