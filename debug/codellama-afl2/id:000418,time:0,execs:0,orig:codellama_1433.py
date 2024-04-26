import os

def main():
    # Create a new environment using conda.yml file
    os.system("conda env create -f conda.yml")
    
    # Activate the new environment
    os.system("conda activate myenv")
    
    # Assert that the Python version is 3.8 or higher
    assert(sys.version_info >= (3, 8))
    
    # Install a package using pip
    os.system("pip install requests")
    
    # Deactivate the environment
    os.system("conda deactivate")