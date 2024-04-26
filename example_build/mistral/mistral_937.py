
# Function to check if a number is even and positive
def is_even_positive(n):
  # Iterate while the number is not positive
  while n <= 0:
    print("Error: Number must be positive!")
    n = int(input("Enter a positive number: "))
  
  # Check if the number is even using 'and' operator
  if n % 2 == 0 and n > 0:
    print(f"{n} is an even positive number.")
  else:
    print(f"{n} is not an even positive number.")

# Test cases
is_even_positive(5)         # Ouput: 5 is not an even positive number.
is_even_positive(-3)        # Output: Error: Number must be positive! Enter a positive number: 4 4 is not an even positive number.
is_even_positive(6)         # Output: 6 is an even positive number.
