from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello/<firstname>')
def hello(firstname):
    return '<h1>Hello %s</h1>\n' % escape(firstname)

if __name__ == '__main__':
    app.run()
