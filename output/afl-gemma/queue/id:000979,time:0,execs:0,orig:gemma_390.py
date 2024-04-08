
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', message='Hello, world!')

@app.route('/check_truth')
def check_truth():
    truth = False
    return render_template('check_truth.html', message='The truth is:', truth=truth)

if __name__ == '__main__':
    app.run()
