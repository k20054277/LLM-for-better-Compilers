
# Demonstration of and and global keywords in Python

# Global variable
global_var = 10

# Local variable
local_var = 20

# Local function
def local_function():
    # Local variable
    local local_variable = 30

    # Global variable
    print("Global variable:", global_var)

    # Local variable
    print("Local variable:", local_var)

    # Local variable within function
    print("Local variable within function:", local_variable)

# Calling local function
local_function()

# Output
# Global variable: 10
# Local variable: 20
# Local variable within function: 30
