#!/usr/bin/python3
"""
    a script that starts a Flask web application:
"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    """
        a hello function
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_route():
    """
        display hbnb
    """
    return "HBNB"


@app.route("/c/<text>")
def c_route(text, strict_slashes=False):
    return f"C {escape(text)}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
