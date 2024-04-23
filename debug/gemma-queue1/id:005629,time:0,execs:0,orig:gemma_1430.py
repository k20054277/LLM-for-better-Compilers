
from flask import Flask, assert

app = Flask(__name__)

@app.route("/")
def hello():
    assert True
    return "Hello, world!"

if __name__ == "__main__":
    app.run()
