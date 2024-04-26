# Importing the necessary modules
from typing import List, Tuple

# Defining a function to demonstrate the use of "as"
def get_tuple() -> Tuple[int, int]:
    return (10, 20)

# Defining a function to demonstrate the use of "dependency"
def get_list(my_tuple: Tuple[int, int]) -> List[int]:
    return [x for x in my_tuple]

# Demonstrating the use of "as" and "dependency"
print(get_list(get_tuple()))  # Output: [10, 20]