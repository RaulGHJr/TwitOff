from flask import Flask
from .model import DB


def create_app():
    '''Create and configure an instance of the Flask application.'''
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/cicbeast/TwitOff/twitoff/db.sqlite3'
    DB.init_app(app)

    @app.route('/hello')
    def root():
        return '<h2> Welcome to TwitOff! </h2>'

    return app 
