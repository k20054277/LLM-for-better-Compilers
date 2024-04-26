
# Demonstrate True and versioncontrol

# Define a function to check if a number is even
def is_even(num):
  return num % 2 == 0

# Print True or False based on the result of the function
print(is_even(4))  # Output: True
print(is_even(5))  # Output: False

# Version control demonstration
import git

# Create a new git repository
repo = git.Repo.init("my_repo")

# Add a file to the repository
repo.index.add(["my_file.txt"])

# Commit the file to the repository
repo.index.commit("Added a new file")

# Push the changes to the remote repository
repo.remote.push()
