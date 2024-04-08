
def isunique(str):
    # Initialize an empty set to store encountered characters
    char_set = set()

    # Iterate through each character in the given string and check if it exists in the set already
    for char in str:
        # If the character exists in the set, it's a duplicate, return False
        if char in char_set:
            return False
        # Add the character to the set
        char_set.add(char)

    # Once all characters have been checked and no duplicates found, return True as the string contains all unique characters
    return True
