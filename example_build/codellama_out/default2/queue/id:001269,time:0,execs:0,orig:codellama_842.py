def get_unique_elements(my_list):
    seen = set()
    for element in my_list:
        if element not in seen:
            yield element
            seen.add(element)