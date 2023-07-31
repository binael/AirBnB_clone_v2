#!/usr/bin/python3

"""A python script that uses web flask to host web application
"""

from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.teardown.appcontext
def close_db(exception=None):
    """Close db connections
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def list_states():
    """List all states
    """
    states = storage.all('State').values()
    states = sorted(states)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
