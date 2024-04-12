from flask import Flask, render_template, request

doubletriple_app = Flask(__name__)

@doubletriple_app.route('/two-times', methods=['POST'])
def two_times():
    if request.method == 'POST':
        number = int(request.form['numberInput'])
        result = number * 2
        return str(result)  # Return result as plain text

@doubletriple_app.route('/three-times', methods=['POST'])
def three_times():
    if request.method == 'POST':
        number = int(request.form['numberInput'])
        result = number * 3
        return str(result)  # Return result as plain text

@doubletriple_app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    doubletriple_app.run(debug=True)



