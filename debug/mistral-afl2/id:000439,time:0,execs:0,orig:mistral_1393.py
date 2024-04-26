
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/validate_number')
def validate_number():
    try:
        number_str = request.args.get('number')
        number = int(number_str)
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

    assert number >= 1 and number <= 10, "Number should be between 1 and 10"

    return jsonify({'message': 'Valid number'})

if __name__ == '__main__':
    app.run(debug=True)
