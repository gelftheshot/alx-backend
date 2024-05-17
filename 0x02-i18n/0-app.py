#!/usr/bin/env python3
""" a flask app that return template """

from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('0-index.html')

if __name__ == '__main__':
    app.run()
