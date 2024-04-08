
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/none', methods=['GET'])
def none_endpoint():
    # This endpoint just returns 'None' when called
    return jsonify(data=None)

@app.route('/echo', methods=['POST'])
def echo_endpoint():
    # Get the request data, if any, and return it back
    data = request.get_json() or None
    return jsonify(data=data)

if __name__ == '__main__':
    app.run(debug=True)
