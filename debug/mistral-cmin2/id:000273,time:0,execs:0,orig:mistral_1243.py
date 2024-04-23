
# Example 1: Using as for variable assignment
import contextlib

with contextlib.redirect_stdout(None) as null_out:  # Assign output to 'null_out' using 'as'
    print("Hello, World!", file=null_out)          # Redirect stdout to 'null_out'

# Prints: "Hello, World!" (does not appear in the console because we redirected it to 'null_out')
