
def get_first_letter(my_list):
    try:
        return my_list[0][0]
    except IndexError:
        print("The list is empty or does not have an index 0")
        return None

my_list = [["A", "Apple"], ["B", "Banana"], ["C", "Cherry"]]
print(get_first_letter(my_list)) # prints: 'A'

my_empty_list = []
print(get_first_letter(my_empty_list)) # prints: The list is empty or does not have an index 0, and returns None.
