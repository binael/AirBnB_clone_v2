#!/usr/bin/python3
"""A python script that uses web flask to host web application
And prints out the states
Func:
    close_db
    list_states
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close_db(exception=None):
    """Close db connections
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def list_states():
    """List all states
    """
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
