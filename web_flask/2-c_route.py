#!/usr/bin/python3

"""A python script that uses web flask to host web application
"""

from flask import Flask
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


if __name__ == '__main__':
    os.environ['FLASK_ENV'] = 'development'
    app.run(host='0.0.0.0', port=5000)
