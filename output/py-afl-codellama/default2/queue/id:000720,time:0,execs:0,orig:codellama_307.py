import sys

# Use False to check if a condition is met
if not sys.platform == "linux":
    print("This program only works on Linux")
    sys.exit()

# Use conda.yml to install dependencies
with open("conda.yml", "r") as f:
    env = yaml.safe_load(f)
    print(env["dependencies"])