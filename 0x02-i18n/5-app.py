#!/usr/bin/env python3
""" just the obj """
from flask import Flask
from flask import request
from flask import render_template
from flask_babel import Babel

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """
    Application configuration class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Instantiate the application object
app = Flask(__name__)
app.config.from_object(Config)

# Wrap the application with Babel
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    Gets locale from request object
    """
    locale = request.args.get('locale', '').strip()
    if locale and locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user(id) -> Union[Dict[str, Union[str, None]], None]:
    """
        get user or nothing
    """
    return users.get(int(id), 0)


@app.before_request
def before_request():
    """
    Adds valid user to the global session object `g`
    """
    setattr(g, 'user', get_user(request.args.get('login_as', 0)))


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Renders a basic html template
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()
