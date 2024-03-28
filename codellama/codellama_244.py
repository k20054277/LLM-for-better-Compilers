from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return {'message': 'Welcome to my API!'}

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data['username']
    password = data['password']
    user = {'username': username, 'password': password}
    users.append(user)
    return jsonify({'message': 'User created successfully!'})

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = find_user(user_id)
    if user is None:
        return jsonify({'message': 'User not found!'})
    else:
        return jsonify(user)

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = find_user(user_id)
    if user is None:
        return jsonify({'message': 'User not found!'})
    else:
        data = request.get_json()
        username = data['username']
        password = data['password']
        user['username'] = username
        user['password'] = password
        return jsonify(user)

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = find_user(user_id)
    if user is None:
        return jsonify({'message': 'User not found!'})
    else:
        users.remove(user)
        return jsonify({'message': 'User deleted successfully!'})