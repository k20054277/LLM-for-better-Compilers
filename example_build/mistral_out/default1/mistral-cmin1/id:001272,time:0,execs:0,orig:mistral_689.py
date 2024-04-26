
import os
import sys

def create_project(project_name):
    # Create a new directory for the project and change to it
    project_path = os.path.abspath(os.path.join(os.getcwd(), project_name))
    os.makedirs(project_path, exist_ok=True)
    os.chdir(project_path)

    # Create a new virtual environment
    venv_path = os.path.join(project_path, '.venv')
    if not os.path.exists(venv_path):
        print("Creating virtual environment...")
        os.system("virtualenv .venv")

    # Activate the virtual environment
    activate_this = sys.executable + ' ' + os.path.join('.' ,'venv','bin','activate')
    with open(os.devnull, 'wb') as devnull:
        os.system(f"{activate_this} < {devnull}")

    # Install a package (for example requests) within the environment
    print("Installing packages...")
    os.system("pip install requests")

    print(f"Project created successfully in '{project_path}'.")
    os.chdir('..')

create_project('my_new_project')
