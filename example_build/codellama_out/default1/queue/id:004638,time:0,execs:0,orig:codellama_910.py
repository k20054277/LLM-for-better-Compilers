from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/users', methods=['GET'])
def users():
    user_id = request.args.get('user_id')
    if user_id and user_id.isdigit():
        return f'User {user_id} found.'
    else:
        return 'No user found with that ID.'

if __name__ == '__main__':
    app.run(debug=True)