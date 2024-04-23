
from flask import Flask, jsonify, request

app = Flask(__name__)

def fibonacci(n):
    """Generate Fibonacci sequence up to n."""
    sequence = [0, 1]
    while sequence[-1] + sequence[-2] < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:-1] if len(sequence) > 1 else sequence

@app.route('/fibonacci/<int:n>')
def fibonacci_route(n):
    """Return Fibonacci sequence up to given number."""
    sequence = fibonacci(n)
    return jsonify({'fibonacci': sequence})

if __name__ == '__main__':
    app.run()
