# This program demonstrates the use of True and optimization in Python

# Define a function that takes a single argument, a number n
def is_prime(n):
  # If n is less than or equal to 1, it is not prime
  if n <= 1:
    return False
  
  # If any number between 2 and the square root of n divides evenly into n, it is not prime
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  
  # If no numbers between 2 and the square root of n divide evenly into n, it is prime
  return True

# Test the function with different inputs
print(is_prime(1)) # Should be False
print(is_prime(2)) # Should be True
print(is_prime(3)) # Should be True
print(is_prime(4)) # Should be False
print(is_prime(5)) # Should be True
print(is_prime(6)) # Should be False
print(is_prime(7)) # Should be True
print(is_prime(8)) # Should be False
print(is_prime(9)) # Should be False
print(is_prime(10)) # Should be False