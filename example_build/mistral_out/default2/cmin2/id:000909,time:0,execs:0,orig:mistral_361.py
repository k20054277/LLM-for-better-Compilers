
import re

def find_pattern(input_string, pattern):
    """
    This function takes an input string and a regular expression pattern as arguments,
    and returns the first match found in the string. If no match is found, it returns None.
    """
    try:
        match = re.search(pattern, input_string)
        if match:
            return match.group()
        else:
            return None
    except Exception as e:
        print(f"Error occurred while searching for pattern: {e}")
        return None

# Test cases
input_string1 = "The quick brown fox jumps over the lazy dog"
pattern1 = r"\bfox\b"
print(find_pattern(input_string1, pattern1))  # Output: 'fox'

input_string2 = "I love programming in Python"
pattern2 = r"\bpyman\b"
print(find_pattern(input_string2, pattern2))  # Output: None
