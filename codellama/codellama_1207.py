# my_package/__init__.py
from . import my_module1
from . import my_module2

# my_package/my_module1.py
def my_function1():
    print("I am function 1")

# my_package/my_module2.py
def my_function2():
    print("I am function 2")

# setup.py
from setuptools import setup

setup(
    name="my-package",
    version="0.1",
    packages=["my_package"],
    url="https://github.com/username/my-package",
    license="MIT",
    author="Your Name",
    author_email="your@email.com"
)