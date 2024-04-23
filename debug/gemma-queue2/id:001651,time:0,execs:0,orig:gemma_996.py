
# Import necessary libraries
import os
import git

# Define the directory containing the code
directory = "/path/to/your/directory"

# Initialize a git object
git_repo = git.Repo(directory)

# Make changes to the code
# For example, edit a file in the directory
with open("my_file.py", "w") as f:
    f.write("print('Hello, world!')")

# Commit the changes to the git repository
git_repo.index.add(["my_file.py"])
git_repo.index.commit("Added a message to my file")

# Push the changes to the remote repository
git_repo.remote.push()

# Print a message to the console
print("Changes committed and pushed successfully!")
