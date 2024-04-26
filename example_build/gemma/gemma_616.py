
# True and while demonstration

# Define a function to check if a number is even
def is_even(n):
  return n % 2 == 0

# Initialize a variable to True
is_even_flag = True

# While the flag is True, continue the loop
while is_even_flag:
  # Get the number from the user
  number = int(input("Enter a number: "))

  # Check if the number is even
  if is_even(number):
    # Print the number is even
    print(f"The number {number} is even")
  else:
    # Print the number is not even
    print(f"The number {number} is not even")

  # Check if the user wants to continue
  continue_flag = input("Do you want to continue? (Y/N): ").lower()

  # If the user does not want to continue, set the flag to False
  if continue_flag != "y":
    is_even_flag = False

# Print a goodbye message
print("Goodbye!")
