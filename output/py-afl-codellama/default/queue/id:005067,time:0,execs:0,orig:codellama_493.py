from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/users', methods=['GET'])
def get_users():
    users = [{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Jane'}]
    return jsonify(users)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = None
    for u in users:
        if u['id'] == user_id:
            user = u
            break
    if user is not None:
        return jsonify(user)
    else:
        return 'User with id {} not found.'.format(user_id),