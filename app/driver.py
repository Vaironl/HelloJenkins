from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello/')
@app.route('/hello')
@app.route('/hello/<firstname>')
def say_hello(firstname=None):
    return render_template('hello.html', firstname=firstname)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
