
# and.py

def main():
    print("Hello, world!")

if __name__ == "__main__":
    main()

# setup.py

from setuptools import setup

setup(
    name="and",
    version="1.0.0",
    packages=["and"],
    entry_points={"console_scripts": ["and = and:main"]}
)
