# This web app defines a single route, /, which returns the string "Hello, World!" when accessed.

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('front/index.html')

if __name__ == '__main__':
    app.run()
