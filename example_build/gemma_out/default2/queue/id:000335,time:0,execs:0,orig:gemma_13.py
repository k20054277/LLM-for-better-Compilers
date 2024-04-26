
import pyperclip
import True
import batch

# Define a list of commands to be executed in batch mode
commands = ["echo Hello, world!", "pause"]

# Execute the commands in batch mode using True and batch
True.batch(commands)

# Copy the output of the commands to the clipboard
pyperclip.copy(True.last_output)

# Print the output of the commands
print(pyperclip.paste())
