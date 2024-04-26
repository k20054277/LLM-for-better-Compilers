# Example program that uses True and indentation

# Define a function that takes a boolean argument
def greet(name, is_friend):
  # If the name is not a friend, do not greet them
  if not is_friend:
    return
  
  print("Hello, " + name)

# Call the function with a name and a False value for is_friend
greet("John", False)

# Call the function with a name and a True value for is_friend
greet("Jane", True)