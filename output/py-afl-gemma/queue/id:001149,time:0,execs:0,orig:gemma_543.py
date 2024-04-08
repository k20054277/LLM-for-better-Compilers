
# Demonstrate the use of None and resource in Python

# Define a function to demonstrate resource usage
def use_resource(resource):
    # Use the resource
    print("Using resource:", resource)

    # Release the resource
    resource = None

# Create a resource
resource = "My precious resource"

# Demonstrate the use of resource
use_resource(resource)

# Check if the resource is None
if resource is None:
    print("Resource is None")

# Output:
# Using resource: My precious resource
# Resource is None
