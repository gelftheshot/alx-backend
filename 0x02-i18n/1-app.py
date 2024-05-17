#!/usr/bin/python3
""" Using Babel for the first time in my life """

from flask import Flask, render_template
from flask_babel import Babel
from datetime import datetime
import pytz

class Config():
    """ The class to configure Babel """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

@app.route('/')
def main():
    """ A function to return a template """
    return render_template('1-index.html')

if __name__ == '__main__':
    app.run()