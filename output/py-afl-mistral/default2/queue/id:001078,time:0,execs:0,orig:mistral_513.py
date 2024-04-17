
# Function to check if a number is even or odd
def check_even_odd(number):
    try:
        # Check if the number is even
        if number % 2 == 0:
            result = "Even"
        else:
            result = "Odd"
     except Exception as e:
         print("An error occurred:", e)
         result = "Unknown"
     finally:
         # This will always be executed
         print(f"The number {number} is {result}")

# Test cases
check_even_odd(5)
check_even_odd(6)
check_even_odd("Hello")
