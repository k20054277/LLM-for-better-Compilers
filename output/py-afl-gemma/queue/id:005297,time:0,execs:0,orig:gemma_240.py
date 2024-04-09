
# Demonstrating the use of and and vars

# Define a function
def demonstrate_and_vars(name, age):
  # Declare variables
  my_name = name
  my_age = age

  # Use and operator to check if the name is "John" and age is greater than 18
  if my_name == "John" and my_age > 18:
    print("Hello, John. You are eligible to vote.")

# Call the function with different parameters
demonstrate_and_vars("John", 20)
demonstrate_and_vars("Jane", 16)
