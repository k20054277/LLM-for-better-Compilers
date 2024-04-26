
# This Python program demonstrates the use of and and format

# Define a function to format a number
def format_number(n):
    # Format the number with a decimal point
    formatted_number = str(n) + ".2f"
    # Return the formatted number
    return formatted_number

# Get the number to format
number = 12.5

# Format the number
formatted_number = format_number(number)

# Print the formatted number
print(formatted_number)
