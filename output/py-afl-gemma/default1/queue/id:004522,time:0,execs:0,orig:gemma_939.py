
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/hello/<string:name>')
def hello(name):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run()
