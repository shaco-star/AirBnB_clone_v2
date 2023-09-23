#!/usr/bin/python3

"""Run flask on port 5000"""
from flask import Flask

app = Flask(__name__)
"""Flask application"""


@app.route('/', strict_slashes=False)
def hello_world():
    """Home page"""
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
