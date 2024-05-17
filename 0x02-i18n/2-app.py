#!/usr/bin/env python3
"""
A Basic flask application
"""
from flask import Flask,request,render_template,
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Gets locale from request object
    """
    return request.accept_languages.best_match(app.config['en', 'fr'])


@app.route('/')
def index():
    """
    Renders a basic html template
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run()