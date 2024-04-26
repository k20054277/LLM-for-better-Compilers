
import re

# Define a simple function that checks if a given string starts with "Python"
def check_string_startswith_python(string):
    return True if string.startswith('Python') else False

# Use re module to check if a string matches a regular expression pattern
def check_string_with_regex(string):
    pattern = r'^Python'
    return bool(re.match(pattern, string))

if __name__ == "__main__":
    strings = ['Python is awesome', 'Java is not Python', 'I love Python']

    for string in strings:
        print(f'String: {string}')
        print(f'check_string_startswith_python(): {check_string_startswith_python(string)}')
        print(f'check_string_with_regex(): {check_string_with_regex(string)}')
        print()
