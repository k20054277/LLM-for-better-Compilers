
def validate_char(char):
    # Define valid character range
    min_char = ord('A')
    max_char = ord('Z')
    
    # Check if the given character is within the valid range using assert
    assert ord(char) >= min_char and ord(char) <= max_char, f"Invalid character. Expected a character between '{chr(min_char)}' and '{chr(max_char)}'"
    
    # Convert ASCII value to its corresponding character using chr
    validated_char = chr(ord(char))
    
    return validated_char

try:
    # Testing the function with a valid character
    valid_char = validate_char('B')
    print("Valid Character: ", valid_char)

    # Testing the function with an invalid character
    invalid_char = validate_char('a')
except AssertionError as e:
    print(e)
