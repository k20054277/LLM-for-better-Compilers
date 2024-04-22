
from flask import Flask, render_template, request, flash

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        num1 = float(request.form.get('num1'))
        num2 = float(request.form.get('num2'))

        if num1 > 0 and num2 > 0:
            result = num1 + num2
            return render_template('index.html', result=result)
        else:
            flash('Both numbers must be positive!')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
