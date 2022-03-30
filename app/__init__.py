
from flask import Flask
from flask_cors import CORS

from app.config import Config

class App:

    flask = Flask(__name__)
    CORS(flask)

    config = flask.config
    config.from_object(Config)
    config['CORS_HEADERS'] = 'Content-Type'


    def run(debug: bool | None, load_dotenv: bool=True, **options):

        App.flask.run(
            host=App.config['HOST'],
            port=App.config['PORT'],
            debug=debug, 
            load_dotenv=load_dotenv, 
            **options
        )


    def route(rule: str, **options):

        return App.flask.route(rule, **options)

