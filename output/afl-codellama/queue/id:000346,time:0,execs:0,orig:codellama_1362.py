from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    name = request.args.get('name')
    assert name is not None, "Name parameter is required"
    return jsonify({'message': f"Hello, {name}!"})

if __name__ == '__main__':
    app.run(debug=True)