# Demonstrate the use of True and environment variables in Python

import os

print("True:", True)

print("Environment Variables:")
for key, value in os.environ.items():
    print(f"\t{key}: {value}")