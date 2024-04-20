def demo_none_and_filter():
    numbers = [1, 2, 3, 4, 5]
    none_numbers = [None, None, None, None, None]
    filtered_numbers = list(filter(lambda x: x is not None, numbers))
    return "Filtered numbers:", filtered_numbers