# Demonstrate the use of False and garbage collection

# Define a function to demonstrate False
def test_false(x):
  if x == False:
    print("False was found!")
  else:
    print("No False was found.")

# Test the function with a value that is not False
test_false(True)

# Test the function with a value that is False
test_false(False)

# Demonstrate garbage collection
print("Before garbage collection:")
print(gc.get_objects())

# Collect garbage
gc.collect()

# Print objects again after garbage collection
print("After garbage collection:")
print(gc.get_objects())