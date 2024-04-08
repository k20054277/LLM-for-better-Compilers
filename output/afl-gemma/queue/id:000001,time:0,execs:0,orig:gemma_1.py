
# True and Scripting Demonstration

# Define a function to demonstrate True and scripting
def demonstrate_true_and_scripting():
    # Use True to evaluate an expression as True
    print(True)  # Output: True

    # Use True to control flow of control
    if True:
        print("True branch executed")  # Output: True branch executed

    # Scripting - Execute a block of code as if it were a script
    exec("""
        print("Script block executed")  # Output: Script block executed
    """)

    # Use True and scripting to control program flow
    if True and False:
        print("Conditionally executed code")  # Output: Not executed

# Call the function
demonstrate_true_and_scripting()
