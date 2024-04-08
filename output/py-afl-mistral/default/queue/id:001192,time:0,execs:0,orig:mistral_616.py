
# Import Flask module
from flask import Flask, jsonify, render_template_string

app = Flask(__name__)  # Create a new Flask web server instance

@app.route('/')  # Define the route for the root URL ("/")
def index():
    # Define a variable with a True value
    is_greeting_displayed = True
    
    # If the route is accessed, return the "Hello, World!" message
    if is_greeting_displayed:
        return render_template_string('Hello, World!')

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
