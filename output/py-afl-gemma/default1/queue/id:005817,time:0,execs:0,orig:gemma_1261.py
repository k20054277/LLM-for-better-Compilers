
# as and setup.py demonstration

# as

def square(x):
    return x**2

print(square(5))  # Output: 25

# setup.py

from setuptools import setup

setup(
    name="my_package",
    version="1.0.0",
    packages=["my_package"],
)

# Run the command: python setup.py install

# After installation, you can import and use the package

import my_package

print(my_package.square(5))  # Output: 25
