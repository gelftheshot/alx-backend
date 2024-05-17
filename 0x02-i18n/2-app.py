#!/usr/bin/env python3
"""
A Basic flask application
"""
from flask import Flask,request
from flask import render_template
from flask_babel import Babel

class Config(object):
    """
    Application configuration class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)



@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Renders a basic html template
    """
    return render_template('1-index.html')


@babel.localeselector
def get_locale():
    """ get the best language """
    return request.accept_languages.best_match(['fr', 'en'])

if __name__ == '__main__':
    app.run()
