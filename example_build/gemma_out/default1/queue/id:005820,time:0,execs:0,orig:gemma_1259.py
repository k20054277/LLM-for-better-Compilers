
# Import as and venv libraries
import as
import venv

# Create a virtual environment
venv.create('my_venv')

# Activate the virtual environment
venv.activate('my_venv')

# Install packages into the virtual environment
venv.install('Flask')

# Import Flask library
from flask import Flask

# Create a Flask app
app = Flask(__name__)

# Define a route
@app.route('/')
def hello_world():
    return 'Hello, world!'

# Run the Flask app
if __name__ == '__main__':
    app.run()
