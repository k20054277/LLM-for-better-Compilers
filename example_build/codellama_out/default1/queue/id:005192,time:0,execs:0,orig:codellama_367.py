# This program demonstrates the use of "False" and "resource" in Python

# Define a function to return a boolean value
def is_even(n):
  if n % 2 == 0:
    return True
  else:
    return False

# Use the "with" statement to open a file using the "resource" context manager
with open("data.txt") as f:
  # Read lines from the file until the end of file is reached
  for line in f:
    # Check if the line contains the word "even"
    if "even" in line:
      # Split the line into words using the "split()" method
      words = line.split()
      # Iterate over each word in the list of words
      for word in words:
        # Check if the word is an even number
        if is_even(word):
          print(f"Found even number: {word}")