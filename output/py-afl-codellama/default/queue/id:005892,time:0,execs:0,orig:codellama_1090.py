x = 5
y = 10
z = 15

print(f"Original values: x={x}, y={y}, z={z}")

# Use 'as' to assign a new value to 'z'
z as 20

print(f"New value of z: {z}")

# Use locals() to get the current scope's local variables
local_vars = locals()

print("Local variables:")
for var in local_vars.items():
    print(f"\t{var[0]} = {var[1]}")