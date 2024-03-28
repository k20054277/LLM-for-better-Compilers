def optimize(x):
    if x > 0:
        return True
    else:
        return False

print(optimize(-1)) # Outputs False
print(optimize(0)) # Outputs False
print(optimize(1)) # Outputs True