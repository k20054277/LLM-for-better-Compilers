
def check_number(num):
    # Logic with bugs
    if num > 9 and num < 21:  # Check if the number is between 10 and 20 (bug #1)
        print("The number is within the range.")
        
        # Bug #2: Missing check for evenness
        #if num % 2 == 0:
        #    print("The number is even.")

        # Print a message with incorrect information
        print("The number is odd.")

# Test cases (with and without bugs)
print("\nTesting with correct number...")
check_number(15)

# Test case with bug #1 (out of range number)
print("\nTesting with out-of-range number...")
check_number(8)

# Test case with bug #2 (in-range even number)
print("\nTesting with in-range even number...")
check_number(12)
