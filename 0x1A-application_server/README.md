#!/usr/bin/python3
"""
Flask route to display "Hello HBNB!"
"""
from flask import Flask

app = Flask(__name__)

@app.route('/airbnb-onepage/')
def hello_hbnb():
    """
    Display "Hello HBNB!"
    """
    return "Hello HBNB!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)



