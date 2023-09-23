#!/usr/bin/python3

"""Run flask on port 5000"""
from flask import Flask, render_template

app = Flask(__name__)
"""Flask application"""


@app.route('/', strict_slashes=False)
def hello_world():
    """Home page"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """hbnb page"""
    return 'HBNB'


@app.route('/c/<text>')
def c_page(text):
    '''C  page.'''
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/')
@app.route('/python/<text>')
def python_page(text="is_cool"):
    '''python  page.'''
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number_page(n):
    '''Number  page.'''
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def number_page_template(n):
    '''HTML Template  page.'''
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
