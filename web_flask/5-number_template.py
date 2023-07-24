#!/usr/bin/python3

"""A python script that uses web flask to host web application
"""

from flask import Flask
from flask import render_template
import os

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """A function that displays greetings"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """A function that displays hbnb"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """A function that uses variable"""
    ar = text.split('_')
    return f'C {" ".join(ar)}'


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pyth(text='is_cool'):
    """Displays python is cool as default or any other text"""
    ar = text.split('_')
    return f'Python {" ".join(ar)}'


@app.route('/number/<int:n>', strict_slashes=False)
def num(n):
    """Shows numbers that are only integers"""
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def n_template(n):
    """Renders a html template when integer is imputted"""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    os.environ['FLASK_ENV'] = 'development'
    app.run(host='0.0.0.0', port=5000)
