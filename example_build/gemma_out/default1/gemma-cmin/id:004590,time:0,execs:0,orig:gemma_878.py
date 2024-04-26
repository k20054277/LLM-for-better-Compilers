
# This Python program demonstrates the use of and and format

# Define a function to format a number
def format_number(n):
    # Format the number with a comma separator
    formatted_number = str(n).replace(".","") + ",000"

    # Return the formatted number
    return formatted_number

# Get the number to format
number = 123456

# Format the number
formatted_number = format_number(number)

# Print the formatted number
print(formatted_number)
