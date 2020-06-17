from flask import Flask, request
from pprint import pformat

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<pre>' + pformat(list(request.headers)) + '</pre>'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
