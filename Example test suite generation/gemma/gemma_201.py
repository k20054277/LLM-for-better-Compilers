
import sys

def demo(obj, attr):
    # Use and operator to check if attr is an attribute of obj
    if hasattr(obj, attr) and getattr(obj, attr) is not None:
        print("Attribute:", attr, "Value:", getattr(obj, attr))

# Example usage
demo(sys.stdout, "name")
demo(sys.stdout, "write")

# Output
# Attribute: name Value: None
# Attribute: write Value: <built-in function write>
