# This web app defines a single route, /, which returns the string "Hello, World!" when accessed.

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()