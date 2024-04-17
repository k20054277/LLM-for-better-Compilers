def get_unique_elements(my_list):
    unique_elements = []
    for element in my_list:
        if element not in unique_elements:
            unique_elements.append(element)
    return unique_elements

print(get_unique_elements([1, 2, 3, 4, 5, 6, 7])) # Output: [1, 2, 3, 4, 5, 6, 7]