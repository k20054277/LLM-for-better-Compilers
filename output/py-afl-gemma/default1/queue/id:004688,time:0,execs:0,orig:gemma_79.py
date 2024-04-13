
# Demonstration of and and global keywords

# Global variable
global_variable = 10

# Local variable
local_variable = 20

# Local function
def local_function():
    local_variable = 30
    print("Local variable:", local_variable)

# Global function
def global_function():
    print("Global variable:", global_variable)

# Calling local and global functions
local_function()
global_function()

# Output
# Local variable: 30
# Global variable: 10
