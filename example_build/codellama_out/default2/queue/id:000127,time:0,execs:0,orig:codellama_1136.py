from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/user/<username>')
def user(username):
    return f'Username: {username}'

if __name__ == '__main__':
    app.run()