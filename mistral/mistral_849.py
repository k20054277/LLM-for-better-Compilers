
# Using 'and' operator to combine conditions
def is_even(num):
    return num % 2 == 0

def is_positive(num):
    return num > 0

if is_even(5) and is_positive(5):
    print("Number is even and positive")
else:
    print("Number is not even or not positive")
# Output: Number is even and positive

# Using 'hash' function to generate hash values
def my_hash(key):
    h = 5381
    for char in str(key):
        h = (h * 33) ^ ord(char)
    return h

key = "Python"
hash_value = my_hash(key)
print(f"Hash value of '{key}' is: {hash_value}")
# Output: Hash value of 'Python' is: 2146530822
