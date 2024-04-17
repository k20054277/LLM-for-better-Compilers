# Create a new Python project
$ mkdir my_project
$ cd my_project

# Initialize a new virtual environment
$ python3 -m venv .venv

# Activate the virtual environment
$ source .venv/bin/activate

# Install the package manager
$ pip install --upgrade pip setuptools wheel

# Create a requirements.txt file that specifies the dependencies for your project
$ echo "numpy==1.20.3" > requirements.txt
$ echo "pandas==1.3.5" >> requirements.txt

# Install the dependencies specified in requirements.txt
$ pip install -r requirements.txt

# Use the package manager to update the dependencies for your project
$ pip freeze > requirements.txt