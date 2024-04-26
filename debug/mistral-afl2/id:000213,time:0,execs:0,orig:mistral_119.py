
from flask import Flask, jsonify, abort

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to my Flask application!"

# Define an unauthorized route with a False value as the condition for access
@app.route("/unauthorized")
def unauthorized():
    abort(403) # 403 Forbidden status code represents unauthorized access
    
if __name__ == "__main__":
    app.run()
