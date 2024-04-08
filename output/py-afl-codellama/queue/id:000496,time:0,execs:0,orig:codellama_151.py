from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    name = request.args.get('name')
    if name and len(name) > 0:
        return f'Hello, {name}!'
    else:
        return 'Please provide a name.'

if __name__ == '__main__':
    app.run()