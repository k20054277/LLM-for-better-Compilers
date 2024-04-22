
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Define a variable
    my_variable = "Hello, world!"

    # Render a template
    return render_template('index.html', variable=my_variable)

if __name__ == '__main__':
    app.run()
