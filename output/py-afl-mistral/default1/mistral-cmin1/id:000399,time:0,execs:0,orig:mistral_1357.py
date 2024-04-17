
# Function that checks if a character is vowel or consonant using assert statement
def is_vowel(char):
    vowels = "aeiouAEIOU"
    if ord(char) in map(ord, vowels):
        return True
    else:
        assert len(str(ord(char)).isdigit()) == 1 and int(str(ord(char))) >= 65 and int(str(ord(char))) <= 90 or int(str(ord(char))) >= ord('a') and int(str(ord(char))) <= ord('z'), f"Invalid character '{char}', expected ASCII value between 65-90 (capital letters) or 97-122 (lowercase letters)."
        return False

# Testing the function
print("Is 'a' a vowel? ", is_vowel('a')) # True
print("Is 'b' a vowel? ", is_vowel('b')) # False, but it will raise an AssertionError as 'b' is not between ASCII value 65-90 or 97-122.
print("Is 'C' a vowel? ", is_vowel('C')) # False, but it will pass as the assert condition is also checking for capital letters.
