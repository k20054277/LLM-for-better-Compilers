
def process_data(input_list):
    """
    This function processes a list by checking if each element is a number, and if so, adds it to a new list.
    """
    valid_numbers = []
    
    for num in input_list:
        assert isinstance(num, (int, float)), "Each element in the list should be a number."
        valid_numbers.append(num)
        
    print("Valid Numbers: ", valid_numbers)

input_list = [1, 2, 3, 4, "five"]
process_data(input_list)
