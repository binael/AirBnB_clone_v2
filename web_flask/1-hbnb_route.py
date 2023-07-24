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


if __name__ == '__main__':
    os.environ['FLASK_ENV'] = 'development'
    app.run(host='0.0.0.0', port=5000)
