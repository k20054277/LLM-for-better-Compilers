import os

# create a new virtual environment
os.system("python -m venv myenv")

# activate the virtual environment
os.system(". myenv/bin/activate")

# install pip and setuptools in the virtual environment
os.system("pip install pip setuptools")

# use pip to install a package
os.system("pip install requests")

# run a program using the installed packages
os.system("python myprogram.py")